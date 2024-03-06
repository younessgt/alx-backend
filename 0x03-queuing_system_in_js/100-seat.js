import redis from "redis";
import kue from "kue";
const { promisify } = require("util");
import express from "express";

const app = express();
const queue = kue.createQueue();
const client = redis.createClient();

client.on("error", (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

const getAsync = promisify(client.get).bind(client);
let reservationEnabled = true;

// const obj = { numberOfAvailableSeats: "50" };

const reserveSeat = function (number) {
  client.set("available_seats", number);
};

const getCurrentAvailableSeats = async function () {
  const curr_number = await getAsync("available_seats");
  return curr_number;
};

app.get("/available_seats", async (req, resp) => {
  const seats = await getCurrentAvailableSeats();
  resp.json({ numberOfAvailableSeats: `${seats}` });
});

app.get("/reserve_seat", async (req, resp) => {
  let curr_seats = await getCurrentAvailableSeats();
  if (curr_seats === null) {
    curr_seats = Number(obj.numberOfAvailableSeats);
  }

  if (reservationEnabled === false) {
    resp.json({ status: "Reservation are blocked" });
    return;
  }

  const job = queue.create("reserve_seat").save((err) => {
    if (!err) {
      resp.json({ status: "Reservation in process" });
    } else {
      resp.json({ status: "Reservation failed" });
      return;
    }
  });

  job.on("complete", () =>
    console.log(`Seat reservation job ${job.id} completed`)
  );
  job.on("failed", (err) =>
    console.log(`Seat reservation job ${job.id} failed: ${err}`)
  );
});

app.get("/process", async (req, resp) => {
  resp.json({ status: "Queue processing" });
  queue.process("reserve_seat", async (job, done) => {
    const avSeats = await getCurrentAvailableSeats();
    console.log("hello");
    reservationEnabled = avSeats < 1 ? false : true;
    if (avSeats >= 1) {
      reserveSeat(avSeats - 1);
      done();
    } else {
      done(new Error("Not enough seats available"));
    }
  });
});

app.listen(1245, () => {
  reserveSeat(50);
});

import redis from "redis";

const client = redis.createClient();

client.on("connect", () => console.log("Redis client connected to the server"));
client.on("error", (err) =>
  console.log(`Redis client not connected to the server: ${err}`)
);

const setNewSchool = function (schoolName, value) {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = function (schoolName) {
  client.get(schoolName, (err, value) => {
    console.log(value);
  });
};

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");

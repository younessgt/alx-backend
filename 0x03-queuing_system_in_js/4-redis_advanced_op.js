import redis from "redis";

const client = redis.createClient();
client.on("connect", () => console.log("Redis client connected to the server"));
client.on("error", (err) =>
  console.log(`Redis client not connected to the server: ${err}`)
);

const data = {
  Portland: 50,
  Seattle: 80,
  NewYork: 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (const [key, val] of Object.entries(data)) {
  client.hset("HolbertonSchools", key, val, redis.print);
}

client.hgetall("HolbertonSchools", (err, value) => console.log(value));

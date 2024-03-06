import express from "express";
import redis from "redis";
const { promisify } = require("util");

const app = express();
const client = redis.createClient();

client.on("error", (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

const getAsync = promisify(client.get).bind(client);

const listProducts = [
  {
    itemId: 1,
    itemName: "Suitcase 250",
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: "Suitcase 450",
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: "Suitcase 650",
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: "Suitcase 1050",
    price: 550,
    initialAvailableQuantity: 5,
  },
];

const getItemById = function (id) {
  return listProducts.find((ele) => ele.itemId === id);
};

const reserveStockById = function (itemId, stock) {
  client.set(`item.${itemId}`, stock);
};

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock;
}

app.get("/list_products", (req, resp) => {
  resp.json(listProducts);
});

app.get("/list_products/:itemId", async (req, resp) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    resp.json({ status: "Product not found" });
    return;
  }

  const curr_stock = await getCurrentReservedStockById(itemId);

  const stock =
    curr_stock === null ? item.initialAvailableQuantity : curr_stock;

  item.currentQuantity = stock;
  resp.json(item);
});

app.get("/reserve_product/:itemId", async (req, resp) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    resp.json({ status: "Product not found" });
    return;
  }

  let curr_stock = await getCurrentReservedStockById(itemId);
  if (curr_stock === null) {
    curr_stock = item.initialAvailableQuantity;
  }
  if (curr_stock < 1) {
    resp.json({ status: "Not enough stock available", itemId: itemId });
    return;
  }

  reserveStockById(itemId, curr_stock - 1);
  resp.json({ status: "Reservation confirmed", itemId: itemId });
});

app.listen(1245);

import redis from 'redis';
const { promisify } = require('util');


const client = redis.createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

const setNewSchool = function (schoolName, value) {
  client.set(schoolName, value, redis.print);
};

const getAsync = promisify(client.get).bind(client);

const displaySchoolValue = function (schoolName) {
  getAsync(schoolName).then((data) => console.log(data));
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

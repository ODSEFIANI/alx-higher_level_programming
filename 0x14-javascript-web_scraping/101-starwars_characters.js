#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
const opt = { method: 'GET' };
const id = process.argv[2];


const getName = (url) => new Promise((resolve, reject) => {
  request(url, opt, (err, { statusCode: code, body: res }) => {
    if (err) reject(console.log(err));
    if (code === 200) {
      resolve(JSON.parse(res).name);
    } else {
      resolve(console.log(`Error code: ${code}`));
    }
  });
});

request(url, opt, (err, { statusCode, body }) => {
  if (err) return console.log(err);
  if (statusCode === 200) {
    const { characters } = JSON.parse(body);
    const names = characters.map(url => getName(url));
    Promise.all(names)
      .then(names => names.forEach(name => console.log(name)));
  } else {
    console.log(`Error code: ${statusCode}`);
  }
});

#!/usr/bin/node

const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
const id = process.argv[2];
const request = require('request');
request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const chars = JSON.parse(response.body).characters;
    chars.forEach(char => {
      request(char, (err, resp) => {
        if (err) {
          console.log(err);
        } else {
          const data = JSON.parse(resp.body);
          console.log(data.name);
        }
      });
    });
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});

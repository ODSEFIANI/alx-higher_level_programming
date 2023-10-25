#!/usr/bin/node
const fs = require('fs');
const filename = process.argv[3];
const url = process.argv[2];
const request = require('request');


request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const data = response.body;
    fs.writeFile(filename, data, (err) => {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});

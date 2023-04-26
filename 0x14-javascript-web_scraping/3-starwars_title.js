#!/usr/bin/node

const args = process.argv;
const request = require('request');

request.get(`https://swapi-api.alx-tools.com/api/films/${args[2]}`,
  function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const jsonBody = JSON.parse(body);
      console.log(jsonBody.title);
    }
  }
);

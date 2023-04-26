#!/usr/bin/node

const request = require('request');
const args = process.argv;
request.get(args[2], function (error, response) {
  if (!error) {
    console.log(`code: ${response.statusCode}`);
  }
});

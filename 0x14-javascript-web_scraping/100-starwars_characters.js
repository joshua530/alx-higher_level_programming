#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    body = JSON.parse(body);
    for (const i in body.characters) {
      request(body.characters[i], function (err, response, body) {
        if (err) {
          console.log(err);
        } else if (response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  } else {
    console.log('Erorr Code:' + res.statusCode);
  }
});

#!/usr/bin/node
const request = require('request');
const apiURL = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
  request(`${apiURL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charactersList = JSON.parse(body).characters;
    const characterNames = charactersList.map(
      url => new Promise((resolve, reject) => {
        request(url, (reqErr, _, reqBody) => {
          if (reqErr) {
            reject(reqErr);
          }
          resolve(JSON.parse(reqBody).name);
        });
      }));
    Promise.all(characterNames)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}

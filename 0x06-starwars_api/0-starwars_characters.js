#!/usr/bin/node
const request = require('request');

request(
    `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
    (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      // Assuming the response body is a JSON string, parse it into an object
      const data = JSON.parse(body);

      if (data && 'characters' in data) {
        data.characters.forEach((character) => {
          request(character, (error, response, body) => {
            if (error) {
              console.error(error);
              return;
            }
            const data = JSON.parse(body);
            return data.name;
          });
        });
      } else {
        console.log("No 'characters' property found in the response.");
      }
    }
);

#!/usr/bin/node
const request = require('request');

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(error, `${response.statusCode}`);
      } else {
        resolve(body);
      }
    });
  });
}

async function fetchFilmCharacters (filmId) {
  try {
    const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
    const filmBody = await makeRequest(filmUrl);
    const filmData = JSON.parse(filmBody);

    if (!filmData || !filmData.characters || filmData.characters.length === 0) {
      console.log('No characters found in the response.');
      return;
    }

    for (const characterUrl of filmData.characters) {
      const characterBody = await makeRequest(characterUrl);
      const characterData = JSON.parse(characterBody);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error(error);
  }
}

const filmId = process.argv[2];

if (!filmId) {
  console.error('Please provide a film ID as a command-line argument.');
} else {
  fetchFilmCharacters(filmId);
}

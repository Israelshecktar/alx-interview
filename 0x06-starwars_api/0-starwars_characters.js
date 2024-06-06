#!/usr/bin/node

const request = require('request');

// Fetch the Movie ID from command-line arguments
const movieID = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieID}/`;

// Function to make a request to the API
function fetchCharacters (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (error, res, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body.characters);
      }
    });
  });
}

// Function to fetch the character names
async function fetchAllCharacters () {
  try {
    const characterUrls = await fetchCharacters(apiUrl);

    for (const url of characterUrls) {
      await new Promise((resolve, reject) => {
        request(url, { json: true }, (error, res, body) => {
          if (error) {
            reject(error);
          } else {
            console.log(body.name);
            resolve();
          }
        });
      });
    }
  } catch (error) {
    console.error('An error occurred:', error);
  }
}

// Start fetching characters
fetchAllCharacters();

#!/usr/bin/node

const axios = require('axios');

// Define the base URL for the Star Wars API
const BASE_URL = 'https://swapi.dev/api/';

// Function to fetch characters of a specific movie
async function getMovieCharacters(movieId) {
  try {
    // Make a GET request to the /films/ endpoint with the provided movieId
    const response = await axios.get(`${BASE_URL}films/${movieId}/`);
    const filmData = response.data;

    // Extract the character URLs from the film data
    const characterUrls = filmData.characters;

    // Iterate through character URLs and fetch character data
    for (const characterUrl of characterUrls) {
      const characterResponse = await axios.get(characterUrl);
      const characterData = characterResponse.data;
      console.log(characterData.name);
    }
  } catch (error) {
    if (error.response) {
      console.error(`Error: ${error.response.status} - ${error.response.statusText}`);
    } else {
      console.error(`An unexpected error occurred: ${error.message}`);
    }
  }
}

if (process.argv.length !== 3) {
  console.log('Usage: node starWarsCharacters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

// Call the function to get and print characters of the specified movie
getMovieCharacters(movieId);

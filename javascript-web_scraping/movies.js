// const getMovies = async () => {
//     const response = await fetch('https://swapi-api.alx-tools.com/api/films/');
//     const data = await response.json();
//     return data;
// }

// getMovies().then(data => {
//     console.log(data.results[4].title)
// }).catch(error => {
//     console.error(error);
// })

const request = require('request');

let index = process.argv.slice(2)[0];
index -= 1;
request('https://swapi-api.alx-tools.com/api/films/', (error, response, body) => {
    if (error) {
        console.log(error);
    } else {
        const data = JSON.parse(body);
        console.log(data.results[index].title);
    }
})
// promises.. : help in handling asynchronous code..

// const getNames = (url) => {
//     return new Promise((resolve, reject) => {

//         const request = new XMLHttpRequest();

//         request.addEventListener('readystatechange', () => {
//             if (request.readyState === 4 && request.status === 200) {
//                 const data = JSON.parse(request.responseText);
//                 resolve(data);
//             } else if (request.readyState === 4) {
//                 reject('Error occured')
//             }
//         })

//         request.open('GET', url);
//         request.send();
//     })
// }

// getNames("index.json").then(data => {
//     console.log(data);
//     return getNames('index1.json');
// }).then(data => {
//     console.log(data);
// }).catch(error => {
//     console.log(error);
// })

// fetch api..: it has promises implemented under the hood
const url = 'index.json';

// fetch url returns a response when successfull
fetch(url).then((response) => {
  if (response.status === 200) {
    console.log(response);
    console.log(response.json()); // returns a promise ..parsed.
  } else {
    console.log('failed');
  }
}).then(data => {
  console.log(data);
}).catch((error) => {
  console.log('rejected', error);
});

// fetch only fails when there is a network failure..

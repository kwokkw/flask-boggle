# Springboard - Flask Boggle Game Exercise

## Table of contents

- [Springboard - Flask Boggle Game Exercise](#springboard---flask-boggle-game-exercise)
  - [Table of contents](#table-of-contents)
  - [Overview](#overview)
    - [The challenge](#the-challenge)
    - [Links](#links)
  - [My process](#my-process)
    - [Built with](#built-with)
    - [What I learned](#what-i-learned)
    - [Continued development](#continued-development)
    - [Useful resources](#useful-resources)
  - [Author](#author)
  - [Acknowledgments](#acknowledgments)
  - [Time estimate](#time-estimate)

## Overview

The goal of the game is to get the highest point total. 

To gain points, players create words from a random assortment of letter in a 5X5 grid. The functionality to generate the grid is provided.  

Words can be created from adjacent letters - letters which are horizontal or vertical neighbors of each other as well as diagonals. 

The letters must connect to each other in the proper sequence to spell the word correctly. This means that the next letter in the word can be above, below, left or right of the previous letter in the word (excluding any letters previously used to construct the word). Functionality to determine if a word can be constructed from a boggle board is also provided. 

The main focus of this exercise is on testing Flask. Ensure writing tests **for all views functions added to app.py**.

### The challenge

-   The page should not refresh when the users submits the form.
  - *Attach an event listener to the form's submit button* 
  - *Prevent default form submission*

-   Make an AJAX requests and send form value using axios to the server. 
    -   Difference between the two approaches.
```js
    const respOne = await axios.post("http://127.0.0.1:5000/submit-guess", {
      guess: data,
    });
```
```js
    const respTwo = await axios({
      method: "POST",
      url: "http://127.0.0.1:5000/submit-guess",
      data: data,
    });
```

-   How to pass the form value from `app.js` to server side?
    -   Pass form value from `app.js` vs from `html`?
    -   How to verify data is sent to server?
  

### Links

## My process

1.  Planning and Reading Code
    -   Backend (Flask and Python)
        -   Set Up Flask App
        -   Backen Logic (`boggle.py` provided)
    -   Frontend (HTML, CSS, JS)
    -   Testing

### Built with

### What I learned

### Continued development

### Useful resources

## Author

## Acknowledgments

## Time estimate 

Springboard: 6 - 8 hours
Expectation: 12 - 16 hours

First session: 2 hrs 
Second session: 6 hurs
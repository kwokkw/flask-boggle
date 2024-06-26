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
    - [Questions - Sonia Recording](#questions---sonia-recording)

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
    // Object destructuring 
    //    -   Simple, more concise.
    const respOne = await axios.post("http://127.0.0.1:5000/submit-guess", {
      guess: data,
    });
```
```js
    // Explicit Configuration Object
    //    -   More control over the request configuration.
    const respTwo = await axios({
      method: "POST",
      url: "http://127.0.0.1:5000/submit-guess",
      data: data,
    });
```

-   How to pass the form value from `app.js` to server side?
    -   Pass form value from `app.js` vs from `html`?
        -   Set up a post route where form data is sent to, and process the data inside the route.
        -   Then, redirect to a page that is a `GET` request, and show confirmation/proof that form data was used.
        -   Server then respond with JSON instead of HTML
- 
    -   How to verify data is sent to server?

-   When using JS to send a `POST` request, is there any way to see the `POST variables`?
  
-   Consistently running into `INTERNAL SERVER ERROR` when passing the form value from frontend to backend. 
    -    Handling the error in JS with `try...catch`, checking the type error object to identify the specific error that occurring. 
         -    The request was made and the server responded with a status code that falls out of the range of 2xx.
         -    Checked Form Data on Frontend:
              -    Submitted a `guess` through the form.
              -    Inspected "Network" tab.
              -    In the "Payload", verified the `keyword` field contains the guess value.
                   -    `{keyword: "hello"} keyword: "hello"`
                   -    I confirmed the request reaches the backend and the form data seems correct, the value of `guess` is `None`.
         -    Inspect Backend Code:
              -    The value of `request.form` equals `ImmutableMultiDict([])`, but empty
              -    `guess = request.form.get("keyword")`,  The key matches frontend data, and has a value of `None`.

  

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

How do I know if the form data was passed via JavaScript or directly from HTML?

In this specific scenario, 

- **Standard Form Behavior:** When a user submits a form using the submit button, the browser sends an HTTP request to the server-side route specified in the `action` attribute of the form tag. 

- **Flask Request Handling:** The Flask framework, in this case, interceptes this request and parses the form data. It doesn't matter whether the form submission was triggered by JS or a direct user click. 

- **`request.form` Access:** `request.form` dictionary in Flask provides access to all the form data submitted with the request, regardless of the submission method. 

### Continued development

**AJAX Request:**

- AJAX (Asynchronous JavaScript and XML) is a technique that allows websites to send requests to the server **without refreshing the whole page**. Traditionally, the entire page would reload to show any changes. This makes things feel faster and more responsive. 

**JSON Response:**

- When server (Python code) receives an AJAX request, it needs to send back a response. Often, you want to send data back to the JavaScript code that made the request. 

- **JSON (JavaScript Obbject Notation)** is a format for storing and transmitting data. It's lightweight and easy for **both** JavaScript and Python to understand.

- Instead of sending back a whole HTML page, you can use Flask's ``jsonify` function to create a JSON response containing the information you want to send back. 

### Useful resources

## Author

## Acknowledgments

## Time estimate 

Springboard: 6 - 8 hours
Expectation: 12 - 16 hours

First session: 2 hrs 
Second session: 6 hrs
Thrid session: 6 hrs

### Questions - Sonia Recording 

- 00:46, Why do I need to give it a `key word`?
  
```js
let formData = {guess: $guessInput.val()}
```

- 03:04
  
```python

# Endpoint
@app.route('/submit-guess', methods=['POST'])
def submit():
  guess = request.json['guess']
  ...
  return jsonify({})

```
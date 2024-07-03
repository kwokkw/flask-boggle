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
    - [Debug](#debug)

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
    - **Mistake**
          - In ths particular case, data is being sent from a JavaScript function using Axios, not HTML form. 
              - **Data Sending Method**: `app.js` uses `axios.post` which indicates sending data through the **`POST` request method.**
              - **`request.form` vs `request.json`**
                  - `request.form` is used for data submitted through HTML forms. This data is typically sent using the GET or POST methods, but with the data encoded in the URL (for GET) or the body (for POST) of the request, **not as JSON**.
                  - `request.json` is specifically used for data sent in JSON format, which is the case with the `axios.post` request.
    - **Remember**
        - Use `request.json.get` for data sent in JSON format (like with Axios.post).
        - Use `request.form.get` for data submitted through HTML forms.


**Design the Frontend in an Object Oriented Way**

- 


### Links

[jQuery disable/enable submit button](https://stackoverflow.com/questions/1594952/jquery-disable-enable-submit-button)

## My process

1.  Planning and Reading Code
    -   Backend (Flask and Python)
        -   Set Up Flask App
        -   Backend Logic (`boggle.py` provided)
    -   Frontend (HTML, CSS, JS)
    -   Testing
2.  Displaying the board
3.  Checking for a valid word
4.  Posting a score
5.  Adding a timer
   -  `setInterval()`
6.  Keep track of user gameplay frequency . 
    - `localStorage` (Frontend)
7.  Keep track of high score . 
    - `Session` (Backend)
8.  Design the frontend in an object oriented way.

### Built with

### What I learned

**How do I know if the form data was passed via JavaScript or directly from HTML?**

In this specific scenario, 

- **Standard Form Behavior:** When a user submits a form using the submit button, the browser sends an HTTP request to the server-side route specified in the `action` attribute of the form tag. 

- **Flask Request Handling:** The Flask framework, in this case, interceptes this request and parses the form data. It doesn't matter whether the form submission was triggered by JS or a direct user click. 

- **`request.form` Access:** `request.form` dictionary in Flask provides access to all the form data submitted with the request, regardless of the submission method. 

**Why both `request.json` on the server side and `data` sent by Axios on the frontend are needed to unpack data.**

1.  Frontend
   -  `Axios` to send a `POST` request to the erver with data. 
   -  Axios automatically converts the data provided into JSON format before sending it. 

2. Backend
   -  The server receives the request through Flask.
   -  Flask provides access to the request details through the `request` object.
   -  Even though the data was sent as JSON on the frontend, it arrives as part of the overall request on the server.
   -  To access the actual content (data/value) from the JSON data, the server uses `request.json`. This extracts the JSON portion of the request and allows the server to work with it as a dictionary.

**`action` attribute in the HTML while using Axios**

-   With Axios, the `action` attribute is not essential for sending data.
-   It can be useful as a fallback or for clarity.

**Disable Form Element**

Use jQuery methods to target the submit button and input field element and set their `disabld` property to `true`. This will prevent users from interacting with the elements. 

```js
function disableFutureGuesses() {
  $("#submit-btn").prop("disabled", true);
  $("input").prop("disabled", true);
}
```

**Data Structure differences between `request.json` and `request.form`**

- `request.json`: It can be an object, array, or a combination of both, depending on how the data was formatted on the client-side (frontend). This attribute typically holds data sent in JSON format within the request body. 
- `request.form`: It's a key-value structure (dictionary-like object), where keys (strings) from form field names and values are the submitted data from those fields. 
  - Values are typically strings (user input in the fields), depends on the form configuration, values could also be lists (e.g., multiple selection checkboxes).

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

### Debug

```js

async function sendToServer(data) {
  try {
    const resp = await axios({
      method: "POST",
      url: "/submit-guess",
      data: data,
    });
    // Check for submission status
    if (resp.status === 200) {
      console.log("Guess submitted successfully.");
    } else {
      console.log("Guess submitting error: ", resp.status);
    }
  } catch (error) {
    // Check for Axios specific errors
    if (error.isAxiosError) {
      if (error.response) {
        // The request was made and the server responded with a status code
        // that falls out of the range of 2xx.
        console.error(
          "Error submitting guess: ",
          error.response.data || error.response.statusText
        );
      } else if (error.request) {
        // The request was made but no response was received
        // (e.g., server error or network problem)
        console.error(
          "Error submitting guess: No response received from server."
        );
      } else {
        // Something happened in setting up the request that triggered an Error
        console.error("Error submitting guess: ", error.message);
      }
    } else {
      // Not an Axios error, handle other errors generically
      console.error("Error submitting guess:", error.message || error);
    }
  }
}
```
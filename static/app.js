$(document).ready(function () {
  // 60-second timer to limit the guess window

  // Initializing the Timer
  let remainingTime = 10;

  // Starts with the initial value
  $("#timer").html(remainingTime);

  // Starting the countdown
  let interval = setInterval(function countDown() {
    remainingTime -= 1;

    // Updating the UI
    $("#timer").html(remainingTime);

    // Clearing the timer
    if (remainingTime === 0) {
      clearInterval(interval);
      disableFutureGuesses();
    }
  }, 1000);

  renderPageStats();
});

$("form").on("submit", async function (e) {
  e.preventDefault();

  let $formData = { keyword: $("input").val() };
  const resp = await sendToServer("/submit-guess", $formData);
  handleResponse(resp);
});

async function sendToServer(url, data) {
  const resp = await axios({
    method: "POST",
    url: url,
    data: data,
  });

  if (resp.status === 200) {
    console.log("Guess submitted successfully.");
  }
  return resp;
}

function handleResponse(resp) {
  const result = resp.data.result;

  // use libraries (jQuery) manipulation
  // techniques to update the HTML
  // content based on the response.
  console.log("Result: ", result);
  $("#server-resp").html(result);

  postingScore(result);
}

let currentScore = 0;

function postingScore(result) {
  if (result === "ok") {
    // Score for a word is equal to its length.
    let score = $("input").val().length;
    currentScore += score;
  }
  $("#score").text(currentScore);

  // score tracking
  localStorage.setItem("score", currentScore);

  $("input").val("");
}

// Disabling guesses after timeout
function disableFutureGuesses() {
  $("#submit-btn").prop("disabled", true);
  $("input").prop("disabled", true);
}

async function renderPageStats() {
  // send an Ajax request to the server with
  //  - the score stored on the frontend
  //  - increment the number of times have played on the backend.
  const score = Number(localStorage.getItem("score"));

  const data = { score: score };
  const resp = await sendToServer("/post-score", data);

  const gamePlayed = resp.data["gamePlayed"];
  const highScore = resp.data["highScore"];

  $("#game-played").html(gamePlayed);
  $("#high-score").html(highScore);
}

class BoggleGame {
  constructor() {
    this.seconds = 6;
    this.score = 0;
    this.highScore = this.highScore;
    this.words = new Set();

    this.showTime();
    this.countDown();

    // submit even attach to form elemnent.
    $("#submit-guess").on("submit", this.handleSubmit.bind(this));
    $("#highscore").html(this.highScore);
  }

  showTime() {
    $("#timer").html(this.seconds);
  }

  showResult(result, cls) {
    $("#server-resp").html(result).addClass(cls);
  }

  showScore(score) {
    $("#score").html(score);
  }

  countDown() {
    const interval = setInterval(
      function () {
        this.seconds -= 1;
        this.showTime();

        if (this.seconds === 0) {
          clearInterval(interval);
          this.submitScore();
          $("#submit-btn").prop("disabled", true);
          $("input").prop("disabled", true);
        }
      }.bind(this),
      1000
    );
  }

  async handleSubmit(e) {
    e.preventDefault();

    const $input = $("input");
    const $word = $input.val();
    const $formData = { keyword: $word };

    if (this.words.has($word)) {
      this.showResult(`Already found "${$word}"`, "wrong-guess");
      return;
    }

    const resp = await axios({
      method: "POST",
      url: "/submit-guess",
      data: $formData,
    });

    const result = resp.data.result;

    if (result === "ok") {
      this.score += $word.length;
      this.words.add($word);
      this.showResult(result, "ok");
      this.showScore(this.score);
    } else {
      this.showResult(result, "wrong-guess");
    }

    $input.val("");
    console.log(this.words);
  }

  async submitScore() {
    const resp = await axios({
      method: "POST",
      url: "/post-score",
      data: { score: this.score },
    });

    const highScore = resp.data.highScore;
    const gamePlayed = resp.data.gamePlayed;

    this.highScore = highScore;
    $("#game-played").html(gamePlayed);
  }
}

const newGame = new BoggleGame();

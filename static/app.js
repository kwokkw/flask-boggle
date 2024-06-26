const $form = $("form");

$form.on("submit", function (e) {
  e.preventDefault();
  // sendToServer($("input").val());

  let $formData = { keyword: $("input").val() };

  sendToServer($formData);

  console.log("Submit btn clicked");
});

// TODO
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

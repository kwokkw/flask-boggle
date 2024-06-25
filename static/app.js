const $form = $("form");

$form.on("submit", function (e) {
  e.preventDefault();
  // sendToServer($("input").val());

  $formData = { keyword: $("input").val() };
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
    console.log("ERROR: ", error);
  }
}

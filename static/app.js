const $form = $("form");

$form.on("submit", function (e) {
  e.preventDefault();
  sendToServer($("input").val());
});

// TODO
async function sendToServer(data) {
  try {
    const resp = await axios({
      method: "POST",
      url: "http://127.0.0.1:5000/submit-guess",
      data: data,
    });
    // console.log(resp);
  } catch (error) {
    console.log("ERROR: ", error);
  }
}

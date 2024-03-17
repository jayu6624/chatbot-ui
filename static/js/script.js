async function postData(url = "", data = {}) {
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify(data),
  });

  return response.json();
}
sendbutton.addEventListener("click", async () => {
  questionInput = document.getElementById("questionInput").value;
  document.getElementById("questionInput").value = "";
  document.querySelector(".right").style.display = "none";
  document.querySelector(".right1").style.display = "block";
  question1.innerHTML = questionInput;
  let result = await postData("/api", { question: questionInput });
  solution.innerHTML = result.result;
});

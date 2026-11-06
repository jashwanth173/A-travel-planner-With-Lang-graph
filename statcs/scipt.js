const form = document.querySelector("#travel-form");
const messageInput = document.querySelector("#message");
const submitButton = document.querySelector("#submit-button");
const statusMessage = document.querySelector("#status");
const resultSection = document.querySelector("#result-section");
const resultOutput = document.querySelector("#result");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const message = messageInput.value.trim();
  if (!message) {
    messageInput.focus();
    return;
  }

  submitButton.disabled = true;
  statusMessage.dataset.error = "false";
  statusMessage.textContent = "Planning your trip... This can take a little while.";
  resultSection.hidden = true;

  try {
    const response = await fetch("/api/travel", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });
    const data = await response.json();

    if (!response.ok || !data.success) {
      throw new Error(data.error || `Request failed (${response.status}).`);
    }

    resultOutput.innerHTML = data.answer_html;
    resultSection.hidden = false;
    statusMessage.textContent = "Your trip plan is ready.";
  } catch (error) {
    statusMessage.dataset.error = "true";
    statusMessage.textContent = `Could not create your trip plan: ${error.message}`;
  } finally {
    submitButton.disabled = false;
  }
});

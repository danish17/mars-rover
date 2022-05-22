const roverUpperCornerXField = document.querySelector(
  "#rover_upper_right_corner_x"
);

const roverUpperCornerYField = document.querySelector(
  "#rover_upper_right_corner_y"
);

const roverCurrentPosXField = document.querySelector("#rover_current_pos_x");

const roverCurrentPosYField = document.querySelector("#rover_current_pos_y");

const roverCurrentDirField = document.querySelector("#rover_current_direction");

const instructionErrorMessage = document.querySelector(
  "#instruction-error-msg"
);

const currentPosErrorMessage = document.querySelector("#position-error-msg");

const rover_instructions_field = document.querySelector("#rover_instructions");

rover_instructions_field.addEventListener("keydown", (event) => {
  if (["L", "M", "R", "l", "m", "r", "Backspace"].indexOf(event.key) === -1) {
    instructionErrorMessage.classList.add("show");
    event.preventDefault();
    return;
  }
  instructionErrorMessage.classList.remove("show");
});

roverCurrentDirField.addEventListener("keydown", () => {
  if (
    ["N", "S", "E", "W", "n", "s", "e", "w", "Backspace", "Tab"].indexOf(
      event.key
    ) === -1
  ) {
    currentPosErrorMessage.innerText = "Valid directions: 'N', 'E', 'W', 'S'";
    currentPosErrorMessage.classList.add("show");
    event.preventDefault();
    return;
  }
  currentPosErrorMessage.classList.remove("show");
});

const currentPosHandler = (event) => {
  if (
    roverCurrentPosXField.value > roverUpperCornerXField.value ||
    roverCurrentPosYField.value > roverUpperCornerYField.value
  ) {
    currentPosErrorMessage.innerText =
      "x or y cannot be greater than upper right values";
    currentPosErrorMessage.classList.add("show");
    event.preventDefault();
    return;
  }
  currentPosErrorMessage.classList.remove("show");
};

roverCurrentPosXField.addEventListener("change", (event) => {
  currentPosHandler(event);
});

roverCurrentPosYField.addEventListener("change", (event) => {
  currentPosHandler(event);
});

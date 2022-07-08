// Short forms of the days of the week
let days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

// Function to give a string form of a given date
export function displayDate(date) {
  let string = "";
  string += days[date.getDay()] + " ";
  string += date.getDate().toString().padStart(2, "0") + "/";
  string += (date.getMonth() + 1).toString().padStart(2, "0") + "/";
  string += date.getFullYear();
  return string;
}

// Function to give a string form of a given time
export function displayTime(time) {
  let string = "";
  string += time.getHours().toString().padStart(2, "0") + ":";
  string += time.getMinutes().toString().padStart(2, "0");
  return string;
}

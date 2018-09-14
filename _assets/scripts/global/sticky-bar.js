// When the user scrolls the page, execute myFunction 
window.onscroll = function() {myFunction()};

// Get the navbar
var thing_to_stick = document.getElementById("alert-bar");

// Get the offset position of the navbar
var sticky = thing_to_stick.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    thing_to_stick.classList.add("sticky")
  } else {
    thing_to_stick.classList.remove("sticky");
  }
}
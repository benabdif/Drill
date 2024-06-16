// my_script.js

console.log("JavaScript file loaded correctly.");

document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM fully loaded and parsed.");
    function myFunction() {
        alert("Hello! I am an alert box!");
      }
});


function myFunction() {
  const cells = document.querySelectorAll('.rig-row_months div');
  cells.forEach(cell => {
      cell.style.width = '15%';
      cell.style.padding = '20px';
  });
}



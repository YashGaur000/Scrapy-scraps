const toggleButton = document.getElementById('toggleButton');
const myDiv = document.getElementById('myDiv');

// Add a click event listener to the button
toggleButton.addEventListener('click', function() {
    // Toggle the visibility of the div by changing its display style
    if (myDiv.style.display === 'none' || myDiv.style.display === '') {
        myDiv.style.display = 'block'; // Show the div
    } else {
        myDiv.style.display = 'none'; // Hide the div
    }
});
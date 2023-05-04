

var img1 = document.getElementById('img1');
var matrix = [];

var div1 = document.getElementById('originalimg1');
var div2 = document.getElementById('modified1');

img1.addEventListener('change', function(event) {
  // Get the selected file
  var file = event.target.files[0];

  // Read the file as a data URL
  var reader = new FileReader();
  reader.onload = function(event) {
    // Send the data URL to the Flask server using an AJAX request
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({image_data: event.target.result}));
  };
  reader.readAsDataURL(file);
});
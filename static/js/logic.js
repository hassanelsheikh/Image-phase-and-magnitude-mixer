

var img1 = document.getElementById('img1');
var img2 = document.getElementById('img2');

var div1 = document.getElementById('originalimg1');
var div2 = document.getElementById('modified1');

var div3 = document.getElementById('originalimg2');
var div4 = document.getElementById('modified2');

img1.addEventListener('change', function(event) {
  // Get the selected file
  div1.setAttribute('src', '');
  div2.setAttribute('src', '');

  var file = event.target.files[0];

  // Read the file as a data URL
  var reader = new FileReader();
  reader.onload = function(event) {
    // Send the data URL to the Flask server using an AJAX request
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({image_data: event.target.result}));

    div1.setAttribute("src",'/image1?' +  new Date().getTime());


  };
  reader.readAsDataURL(file);

});

function showcomponent() {
  var dropdown1 = document.getElementById("component");
var selectedOption = dropdown1.options[dropdown1.selectedIndex].value;
  if (selectedOption === "imag") {
    div2.setAttribute('src', '');
    div2.setAttribute("src",'/imag1?' +  new Date().getTime());

  } else if (selectedOption === "real") {
    div2.setAttribute('src', '');
    div2.setAttribute("src",'/real1?' +  new Date().getTime());

  } else if (selectedOption === "phase") {
    div2.setAttribute('src', '');
    div2.setAttribute("src",'/phase1?' +  new Date().getTime());

  } else if (selectedOption ==="magnitude"){
    div2.setAttribute('src', '');
    div2.setAttribute("src",'/magnitude1?' +  new Date().getTime());

  }
}

img2.addEventListener('change', function(event) {
  // Get the selected file
  div3.setAttribute('src', '');
  div4.setAttribute('src', '');

  var file = event.target.files[0];

  // Read the file as a data URL
  var reader = new FileReader();
  reader.onload = function(event) {
    // Send the data URL to the Flask server using an AJAX request
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload2', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({image_data: event.target.result}));

    div1.setAttribute("src",'/image1?' +  new Date().getTime());


  };
  reader.readAsDataURL(file);

});
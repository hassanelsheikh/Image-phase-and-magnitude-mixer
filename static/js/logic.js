

var img1 = document.getElementById('img1');

var div1 = document.getElementById('originalimg1');
var div2 = document.getElementById('modified1');
var div3 = document.getElementById('test1');

img1.addEventListener('change', function(event) {
  // Get the selected file
  div1.setAttribute('src', '');
  div2.setAttribute('src', '');
  div3.setAttribute('src', '');

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
    div2.setAttribute("src",'/real1?' +  new Date().getTime());
    div3.setAttribute("src",'/imag1?' +  new Date().getTime());


  };
  reader.readAsDataURL(file);

});


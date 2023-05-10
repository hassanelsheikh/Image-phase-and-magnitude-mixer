

const img1 = document.getElementById('img1');
var img2 = document.getElementById('img2');

var div1 = document.getElementById('originalimg1');
var div2 = document.getElementById('modified1');

var div3 = document.getElementById('originalimg2');
var div4 = document.getElementById('modified2');

var slider1 = document.getElementById("ratio1");
var SROutput = document.getElementById("percent1");

var outdiv1 = document.getElementById("out1");
var outdiv2 = document.getElementById("out2");


SROutput.innerHTML = slider1.value;
SROutput.innerHTML = slider1.value + " %";
///showing sampling rate
slider1.oninput = () => {
  SROutput.innerHTML = slider1.value + " %";
};
var slider2 = document.getElementById("ratio2");
var SROutput2 = document.getElementById("percent2");

SROutput2.innerHTML = slider2.value;
SROutput2.innerHTML = slider2.value + " %";
///showing sampling rate
slider2.oninput = () => {
  SROutput2.innerHTML = slider2.value + " %";
};





img1.addEventListener('change', function (event) {
  // Get the selected file
  div1.setAttribute('src', '');
  div2.setAttribute('src', '');

  var file = event.target.files[0];

  // Read the file as a data URL
  var reader = new FileReader();
  reader.onload = function (event) {

    div1.src = event.target.result;
    // Send the data URL to the Flask server using an AJAX request
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({ image_data: event.target.result }));

    // div1.setAttribute("src", '/image1?' + new Date().getTime());

    


    var uploaded_image = reader.result;
  };
  reader.readAsDataURL(file);

});

function showcomponent() {
  var dropdown1 = document.getElementById("component");
  var selectedOption = dropdown1.options[dropdown1.selectedIndex].value;
  if (selectedOption === "imag") {
    div2.setAttribute('src', '');
    div2.setAttribute("src", '/imag1?' + new Date().getTime());

  } else if (selectedOption === "real") {
    div2.setAttribute('src', '');
    div2.setAttribute("src", '/real1?' + new Date().getTime());

  } else if (selectedOption === "phase") {
    div2.setAttribute('src', '');
    div2.setAttribute("src", '/phase1?' + new Date().getTime());

  } else if (selectedOption === "magnitude") {
    div2.setAttribute('src', '');
    div2.setAttribute("src", '/magnitude1?' + new Date().getTime());

  }
}

img2.addEventListener('change', function (event) {
  // Get the selected file
  div3.setAttribute('src', '');
  div4.setAttribute('src', '');

  var file = event.target.files[0];

  // Read the file as a data URL
  var reader = new FileReader();
  reader.onload = function (event) {
    // Send the data URL to the Flask server using an AJAX request
    div3.src = event.target.result;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload2', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({ image_data: event.target.result }));

    //div3.setAttribute("src", '/image2?' + new Date().getTime());


  };
  reader.readAsDataURL(file);

});

function showcomponent2() {
  var dropdown2 = document.getElementById("component2");
  var selectedOption = dropdown2.options[dropdown2.selectedIndex].value;
  if (selectedOption === "imag2") {
    div4.setAttribute('src', '');
    div4.setAttribute("src", '/imag2?' + new Date().getTime());

  } else if (selectedOption === "real2") {
    div4.setAttribute('src', '');
    div4.setAttribute("src", '/real2?' + new Date().getTime());

  } else if (selectedOption === "phase2") {
    div4.setAttribute('src', '');
    div4.setAttribute("src", '/phase2?' + new Date().getTime());

  } else if (selectedOption === "magnitude2") {
    div4.setAttribute('src', '');
    div4.setAttribute("src", '/magnitude2?' + new Date().getTime());

  }
}
var dropdownddiv = document.getElementById("outputdiv");
var dropdown1 = document.getElementById("wantedcomponent1");
var dropdown2 = document.getElementById("wantedcomponent2");
var dropdownimage1 = document.getElementById("imagepart1");
var dropdownimage2 = document.getElementById("imagepart2");

function on_parameters_change() {
  var outdiv = dropdownddiv.options[dropdown1.selectedIndex].value;

  let mixingr1 = slider1.value;
  let mixingr2 = slider2.value;

  var component1 = dropdown1.options[dropdown1.selectedIndex].value;

  var component2 = dropdown2.options[dropdown2.selectedIndex].value;

  var part1 = dropdownimage1.options[dropdown1.selectedIndex].value;

  var part2 = dropdownimage2.options[dropdown1.selectedIndex].value;




  if (outdiv === "one") {
    outdiv1.setAttribute('src', '');
    outdiv1.setAttribute("src", '/real2?' + new Date().getTime());
  } else if (outdiv === "two") {
    outdiv2.setAttribute('src', '');
    outdiv2.setAttribute("src", '/real2?' + new Date().getTime());
  }
}

slider1.addEventListener("mouseup", async function () {
  on_parameters_change();
})

slider2.addEventListener("mouseup", async function () {
  on_parameters_change();
})

dropdownddiv.addEventListener('click', function () {
  on_parameters_change();
});

dropdown1.addEventListener('click', function () {
  on_parameters_change();
});

dropdown2.addEventListener('click', function () {
  on_parameters_change();
});

dropdownimage1.addEventListener('click', function () {
  on_parameters_change();
});

dropdownimage2.addEventListener('click', function () {
  on_parameters_change();
});
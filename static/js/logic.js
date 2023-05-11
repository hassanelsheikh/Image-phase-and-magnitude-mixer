

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
var size_img1x;
var size_img1y;
var x1;var y1; var x2;var y2;
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
  var isImageLoaded = false; // Flag to indicate if the image has finished loading

  var file = event.target.files[0];
  var img = new Image();
img.onload = function() {
  size_img1x = img.naturalWidth;
  size_img1y = img.naturalHeight;
  isImageLoaded = true; // Set the flag to true when the image has finished loading
  handleImageDimensions(size_img1x, size_img1y); 
}

img.src = URL.createObjectURL(file);
function handleImageDimensions(width, height) {
  // You can perform additional operations with the dimensions here
  x1=width;
  y1=height;
  
}

// Check if the image has finished loading and the dimensions are available
if (isImageLoaded) {
  handleImageDimensions(size_img1x, size_img1y);
} else {
  console.log('Image is still loading...');
}

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
  var errorflag=false;

  div3.setAttribute('src', '');
  div4.setAttribute('src', '');
  var isImageLoaded = false; // Flag to indicate if the image has finished loading

  var file = event.target.files[0];
  var img = new Image();
  img.onload = function() {
    size_img1x = img.naturalWidth;
    size_img1y = img.naturalHeight;
    isImageLoaded = true; // Set the flag to true when the image has finished loading
    handleImageDimensions(size_img1x, size_img1y); 
  }
  
  img.src = URL.createObjectURL(file);
  function handleImageDimensions(width, height) {
    // You can perform additional operations with the dimensions here
    x2=width;
    y2=height;
    
  }
  
  // Check if the image has finished loading and the dimensions are available
  if (isImageLoaded) {
    handleImageDimensions(size_img1x, size_img1y);
    

    
  } else {
    console.log('Image is still loading...');
  }
  // Read the file as a data URL
  setTimeout(function() {
    // Code to execute after the delay
    if (x1 !=x2  || y1 !=y2){
       errorflag=true;  div3.setAttribute('src', '');
    }
  }, 1000); // Delay of 2000 milliseconds (2 seconds)
  var reader = new FileReader();
  reader.onload = function (event) {
    // Send the data URL to the Flask server using an AJAX request
    if(errorflag==true){
      div3.setAttribute('src', '');
      return;
    }

    
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
  var outdiv = dropdownddiv.selectedIndex;

  let mixingr1 = slider1.value;
  let mixingr2 = slider2.value;

  var component1 = dropdown1.selectedIndex;

  var component2 = dropdown2.selectedIndex;

  var part1 = dropdownimage1.selectedIndex;

  var part2 = dropdownimage2.selectedIndex;

  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/mixer');
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onload = function() {
    if (xhr.status === 200) {-
      console.log('Indices updated successfully!');
    } else {
      console.log('Error updating indices.');
    }
  };
  var data = {
    slider1_val:mixingr1,
    slider2_val:mixingr2,
    index1: component1,
    index2: component2,
    Im1: part1,
    Im2: part2,
    type1: dropdown1.options[dropdown1.selectedIndex].value,
    type2: dropdown2.options[dropdown2.selectedIndex].value
  };
  xhr.send(JSON.stringify(data));


  if (outdiv === 0) {
    outdiv1.setAttribute('src', '');
    outdiv1.setAttribute("src", '/final_image?' + new Date().getTime());
  } else if (outdiv === "two") {
    outdiv2.setAttribute('src', '');
    outdiv2.setAttribute("src", '/final_image?' + new Date().getTime());
  }
}

slider1.addEventListener("mouseup", async function () {
  on_parameters_change();
})

slider2.addEventListener("mouseup", async function () {
  on_parameters_change();
})


dropdown1.addEventListener('change', function () {
  on_parameters_change();
});

dropdown2.addEventListener('change', function () {
  on_parameters_change();
});

dropdownimage1.addEventListener('change', function () {
  on_parameters_change();
});

dropdownimage2.addEventListener('change', function () {
  on_parameters_change();
});




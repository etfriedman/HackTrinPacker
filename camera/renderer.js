// Main Selection Code
$(document).ready(function () {
    $('input[type=radio]').click(function () {
        console.log(this.value);
    });
});

const webcamElement = document.getElementById('webcam');
const canvasElement = document.getElementById('canvas');
const webcam = new Webcam(webcamElement, 'user', canvasElement);
// start the webcam
webcam.start()
  .then(result =>{
    //console.log("webcam started");
  })
  .catch(err => {
    console.log(err);
});

//image capture button
document.getElementById('capture').addEventListener('click', function () {

    // var canvasElement = document.getElementById("canvas");
    // canvasElement.toBlob(function(blob) {
    //     saveAs(blob, "lookin good Swag.png");
    // });
    
    let picture = webcam.snap();
    var mydiv = document.getElementById("download");
    var downloadLink = document.createElement('a');
    downloadLink.setAttribute('href',picture);
    downloadLink.setAttribute('download','imagename');
    downloadLink.innerText = "Download Image";
    mydiv.appendChild(downloadLink);    
});

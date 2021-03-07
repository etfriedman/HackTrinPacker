function captureImage() {
    console.log('capture clicked')
};



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
    console.log("webcam started");
  })
  .catch(err => {
    console.log(err);
});

//image capture button
document.getElementById('capture').addEventListener('click', function () {
    let picture = webcam.snap();
    document.querySelector('#download-photo').href = picture;
});

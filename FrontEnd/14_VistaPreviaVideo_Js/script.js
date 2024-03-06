console.log("page loaded...");

function startPreview() {
    video.muted = true;
    video.currentTime = 1;
    video.play();
  }
  
  function stopPreview() {
    video.muted= false; 
    video.currentTime = 0;
    video.pause();
  }
  

var vid = document.getElementById("video");

function enableMute() { 
  vid.muted = true;
} 

var x = document.getElementById("video");

function out() {
  x.play();
}

function over() {
  x.pause();
}
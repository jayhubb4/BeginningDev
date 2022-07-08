function getRndInteger(min, max) {
        return Math.floor(Math.random() * (max - min + 1) ) + min;
      }
      var video = document.getElementById("video");
      video.setAttribute('src', getRndInteger(1,4) + '.mov');
      video.load();
function speak() {
  var text = document.getElementById('inputText').value;
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/speak', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var audioUrl = JSON.parse(xhr.responseText).audio_url;
      var audio = new Audio(audioUrl);
      audio.play();
    }
  };
  xhr.send(JSON.stringify({ text: text }));
}

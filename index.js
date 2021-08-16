function backend() {

    var command = document.getElementById("input").value;
    var xhr = new XMLHttpRequest();
    xhr.open("GET","http://192.168.99.101//cgi-bin/backend.py?cmd="+command,true);
    xhr.send();
    xhr.onload = function() {
        var output = xhr.responseText;
        document.getElementById("div3").innerHTML=output;
        }
}

function record()
        {
            var recognition = new webkitSpeechRecognition();
            recognition.lang = "en-GB";

            recognition.onresult = function(event) {
                console.log(event);
                document.getElementById('input').value = event.results[0][0].transcript;
            }

            recognition.start();
        }

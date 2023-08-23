var submit = document.getElementById('submit')

function sendData() {
    var textbox = document.getElementById('body')
    var title = document.getElementById('title')
    ttitle = title.value
    body = textbox.value
    var JsonData = {"title": ttitle, "body": body, "type": "journal-entry"}
    fetch("#" , {
        method: "POST",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(JsonData)
        }
    ).then(res => res.json())
     .then(data => console.log(data))
     .then(error => console.error(error))
    title.value = ""
    textbox.value = ""
    window.location.replace('http://127.0.0.1:5000/journal/')
}

submit.addEventListener('click', sendData)
var submit = document.getElementById('submit')


async function waitTime() {
    await sleep(0.5);
    window.location.reload()
}

function sendData() {
    var textbox = document.getElementById('textareabody')
    var title = document.getElementById('title')
    ttitle = title.value 
    body = textbox.value
    if (ttitle.length > 5) {
        var error_division = document.getElementById('error-division-title')
        error_division.classList.add('hidden')
        if (body.length > 40) {
            var error_division = document.getElementById('error-division-body')
            error_division.classList.add('hidden')
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
            waitTime()
            window.location.replace('/journal/')
        }else {
            var error_span = document.getElementById('error-message-body')
            error_span.innerHTML = "Title must be atleast 5 charecters"
            var error_division = document.getElementById('error-division-body')
            error_division.classList.remove('hidden')
        }
    }else {
        var error_span = document.getElementById('error-message-title')
        error_span.innerHTML = "Title must be atleast 5 charecters"
        var error_division = document.getElementById('error-division-title')
        error_division.classList.remove('hidden')
    }

}

async function sleep(seconds) {
    return new Promise((resolve) => setTimeout(resolve, seconds*1000))
}

submit.addEventListener('click', sendData)

function addEntry() {
    window.location.replace('/journal/entry/create')
}
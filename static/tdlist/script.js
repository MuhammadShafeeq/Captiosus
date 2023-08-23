var submit = document.getElementById('submit')

async function waitTime() {
    await sleep(0.5);
    window.location.reload()
}
function sendRequest(session) {
    var input = document.getElementById('taskname')
    var JsonData = {user: session, "taskname": input.value}
    if (input.value != '') {
        fetch("http://127.0.0.1:5000/create" , {
            method: "POST",
            headers: {'Content-Type': "application/json"},
            body: JSON.stringify(JsonData)
            }
        ).then(res => res.json())
        .then(data => console.log(data))
        .then(error => console.log(error))
        waitTime()

    }else {
        var error_span = document.getElementById('error-span')
        error_span.innerHTML = "Taskname cannot be empty"
        var error_division = document.getElementById('error-division')
        error_division.classList.remove('hidden')
    }
}
async function sleep(seconds) {
    return new Promise((resolve) => setTimeout(resolve, seconds*1000))
}

function remove(id, session, status) {
    var JsonData = {"username": session, "taskid": id, "taskstatus": status}
    fetch("http://127.0.0.1:5000/remove" , {
        method: "POST",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(JsonData)
        }
    ).then(res => res.json())
     .then(data => console.log(data))
     .then(error => console.log(error))
     window.location.reload()
}
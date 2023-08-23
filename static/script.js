
function func1(id, session) {
    console.log(session)
    console.log(id)
    var JsonData = {"Session": session, "TaskName": id}
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
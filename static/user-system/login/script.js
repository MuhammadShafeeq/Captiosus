var submit_btn = document.getElementById('submit-btn')

function send_req () {
    var username = document.getElementById('username')
    var password = document.getElementById('password')
    var JsonData = {"username": username, "password": password, "perma_session": "false"}
    fetch("/login" , {
        method: "POST",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(JsonData)
        }
    ).then(res => console.log(res))
    .then(data => console.log(data))
    .then(error => console.log(error))
}

submit_btn.addEventListener('click', send_req)

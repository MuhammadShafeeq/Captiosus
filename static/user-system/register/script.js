var name1 = document.getElementById('name')
var password = document.getElementById('password')
var submit = document.getElementById('submit')
var username = document.getElementById('username')
var email = document.getElementById('email')
function actionRegister() {
    console.log('Hey!')
    var usernameregex = new RegExp(/[A-Z0-9a-z]/g)
    var mailregex = new RegExp(/[A-Z0-9a-z._]+@[A-Za-z]+\.[A-Za-z]+/g)
    usernameregex.test(username.value)
    mailregex.test(username.value)
    console.log('Hey1')
    console.log(usernameregex.test(username.value))
    if (usernameregex.test(username.value)) {
        if (mailregex.test(email.value)) {
            JsonData = {"Username": username.value, "Name": name1.value, "Password": password.value}
            fetch("#" , {
                method: "POST",
                headers: {'Content-Type': "application/json"},
                body: JSON.stringify(JsonData)
                }
            ).then(res => res.json())
            .then(data => console.log(data))
            .then(error => console.log(error))
            window.location.replace("/login")
        }
    }
}
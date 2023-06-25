

function login() {
    
    var csrf_token = document.getElementById("csrf").value
    var username = document.getElementById("username").value
    var password = document.getElementById("password").value
    console.log(csrf_token, username, password)
    if (username == "" && password == "") {
        alert("You must enter both")
    }

    var data = {
        "username": username,
        "password": password
    }
    console.log(data)

    fetch("/api/login/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFTOKEN": csrf_token,
        },

        body: JSON.stringify(data)
    }).then(result => {
        console.log("Response status:", result.status);
        return result.json();
    }).then(response => {
        if (response.status == 200) {
            window.location.href = "/";
        } else {
            alert(response.message);
        }
    });
    return false;
}


function register() {
    var csrf_token = document.getElementById("csrf").value
    var username = document.getElementById("username").value
    var password = document.getElementById("password").value

    if (username == "" && password == "") {
        alert("You must enter both")
    }

    var data = {
        "username": username,
        "password": password
    }

    console.log(data)

    fetch("/api/register/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFTOKEN": csrf_token,
        },


        body: JSON.stringify(data)
    }).then(result => {
        console.log("Response status:", result.status);
        return result.json();
    }).then(response => {
        if (response.status == 200) {
            window.location.href = "/";
        } else {
            alert(response.message);
        }
    });
    return false;

}
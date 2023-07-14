function setFooterText() {
    var currentYear = new Date().getFullYear();
    var footerText =
        "Copyright &copy; " + currentYear + " All rights reserved";
    document.getElementById("footer").innerHTML = footerText;
}
document.addEventListener("DOMContentLoaded", setFooterText);

function LoginForm_validation() {

    const username = document.getElementById('username');
    const password = document.getElementById('password');

    document.getElementById('myLoginForm').addEventListener('submit', e => {
        e.preventDefault();
        checkInputsLogin();
    });


    function checkInputsLogin() {
        // trim to remove the whitespaces
        var csrf_token = document.getElementById("csrf").value;
        const usernameValue = username.value;
        const passwordValue = password.value;


        if (usernameValue === '') {
            setErrorFor(username, 'Username cannot be blank');
        } else {
            setSuccessFor(username);
        }

        if (passwordValue === '') {
            setErrorFor(password, 'Password cannot be blank');
        } else {
            setSuccessFor(password);
        }

        if (usernameValue !== '' && passwordValue !== '') {

            var data = {
                "username": usernameValue,
                "password": passwordValue
            }

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
                    return response;
                } else {
                    const msg = response.message;
                    const search_invalidpass = "invalid password"
                    if (msg.includes(search_invalidpass)) {
                        setErrorFor(password, msg);
                    }
                    else {
                        setErrorFor(username, msg);
                    }
                }
            });
            return false;
        }
    }

    function setErrorFor(input, message) {
        const formGroup = input.parentElement;
        const small = formGroup.querySelector('small');
        formGroup.className = 'form-group error';
        small.innerText = message;
    }

    function setSuccessFor(input) {
        const formGroup = input.parentElement;
        formGroup.className = 'form-group success';
    }

}

function RegistrationForm_validation() {

    const reg_username = document.getElementById('reg-username');
    const reg_password = document.getElementById('reg-password');
    const reg_cpassword = document.getElementById('reg-cpassword');
    const reg_email = document.getElementById('reg-email');

    document.getElementById('myRegistrationForm').addEventListener('submit', e => {
        e.preventDefault();
        checkInputsRegister();
    });

    function checkInputsRegister() {
        // trim to remove the whitespaces
        var csrf_token = document.getElementById("csrf").value;
        const usernameValue = reg_username.value;
        const passwordValue = reg_password.value;
        const cpasswordValue = reg_cpassword.value;
        const emailValue = reg_email.value;

        if (usernameValue === '') {
            setErrorFor(reg_username, 'Username cannot be blank');
        } else {
            setSuccessFor(reg_username);
        }

        if (passwordValue === '') {
            setErrorFor(reg_password, 'Password cannot be blank');
        } else {
            setSuccessFor(reg_password);
        }

        if (cpasswordValue === '') {
            setErrorFor(reg_cpassword, 'Confirm password cannot be blank');
        } else {
            setSuccessFor(reg_cpassword);
        }
        if (emailValue === '') {
            setErrorFor(reg_email, 'Email cannot be blank');
        } else {
            setSuccessFor(reg_email);
        }

        if (passwordValue !== cpasswordValue) {
            setErrorFor(reg_password, 'Password should be same');
            setErrorFor(reg_cpassword, 'Password should be same');
        } else {
            setSuccessFor(reg_password);
            setSuccessFor(reg_cpassword);
        }

        if (usernameValue !== '' && passwordValue !== '' && passwordValue === cpasswordValue) {

            var data = {
                "reg-username": usernameValue,
                "reg-password": passwordValue,
                "reg-email": emailValue
            }

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
                    const msg = response.message;
                    const search_username = "username"
                    if (msg.includes(search_username)) {
                        setErrorFor(reg_username, msg);
                    }
                    else {
                        alert(response.message);
                    }

                }
            });
            return false;
        }
    }

    function setErrorFor(input, message) {
        const formGroup = input.parentElement;
        const small = formGroup.querySelector('small');
        formGroup.className = 'form-group error';
        small.innerText = message;
    }

    function setSuccessFor(input) {
        const formGroup = input.parentElement;
        formGroup.className = 'form-group success';
    }

}

function autoExpand(textarea) {
    textarea.style.height = 'auto'; // Reset the height to auto
    textarea.style.height = textarea.scrollHeight + 'px'; // Set the height to match the content
}

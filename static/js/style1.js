function initializeRegistrationForm() {
    const reg_username = document.getElementById('reg-username');
    const reg_password = document.getElementById('reg-password');
    const reg_cpassword = document.getElementById('reg-cpassword');
    const reg_email = document.getElementById('reg-email');
  
    document.getElementById('myRegistrationForm').addEventListener('submit', e => {
      e.preventDefault();
      checkInputsRegister();
    });
  
    function checkInputsRegister() {
      // Rest of the code for input validation and form submission
    }
  
    function setErrorFor(input, message) {
      // Rest of the code for setting error state
    }
  
    function setSuccessFor(input) {
      // Rest of the code for setting success state
    }
  }
  
  // Call the function to initialize the registration form
  initializeRegistrationForm();
  
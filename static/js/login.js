const passwordInput = document.getElementById('password');
const showPasswordCheckbox = document.getElementById('remember-me');

showPasswordCheckbox.addEventListener('change', function () {
  if (showPasswordCheckbox.checked) {
    passwordInput.type = 'text';
  } else {
    passwordInput.type = 'password';
  }
});

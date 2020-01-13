const inputs = document.querySelectorAll('.input');

function focusFunc() {
    let parent = this.parentNode.parentNode;
    parent.classList.add('focus');
}

function blurFunc() {
    let parent = this.parentNode.parentNode;
    if (this.value == "") {
        parent.classList.remove('focus');
    }
}

inputs.forEach(input => {
    input.addEventListener('focus', focusFunc);
    input.addEventListener('blur', blurFunc);
});

$(function () {
    // Custom password validators
    $.validator.addMethod("passLength", function (value, element) {
        return value.length >= 8;
    }, "Your password must be at least 6 character long");

    $.validator.addMethod("charNum", function (value, element) {
        return /\d/.test(value)
            && /[a-z]/i.test(value);
    }, "Your password must contain at least one number and one character");

    // Custom phone and email validators
    $.validator.addMethod("emailPhone", function (value, element) {
        return this.optional(element)
            || /^\d{10}$/.test(value)
            || /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(value);
    }, "Please enter a valid phone number or email");

    $.validator.addMethod("onlyEmail", function (value, element) {
        return this.optional(element)
            || /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(value);
    }, "Please enter a <em>valid</em> email address");
    $("#auth-form").validate({
        rules: {
            email: {
                required: true,
                onlyEmail: true
            },
            email_phone: {
                required: true,
                emailPhone: true
            },
            pass: {
                required: true
            },
            password: {
                required: true,
                passLength: true,
                charNum: true
            },
            password1: {
                required: true,
                equalTo: "#password"
            },
            fname: {
                required: true,
                lettersonly: true
            },
            lname: {
                required: true,
                lettersonly: true
            },
        },
        messages: {
            email: {
                required: "Please enter an email address",
            },
            email_phone: {
                required: "Please enter an email address or phone number",
            },
            pass: {
                required: "Please enter the password"
            },
            password: {
                required: "Please enter the password"
            },
            password1: {
                required: "Please enter the password",
            },
            fname: {
                required: "Please enter your first name"
            },
            lname: {
                required: "Please enter your last name"
            }
        }
    });
    $('#changePassword').validate({
        rules: {
            old_password: {
                required: true
            },
            new_password1: {
                required: true,
                passLength: true,
                charNum: true
            },
            new_password2: {
                required: true,
                equalTo: "#newPassword"
            }
        },
        messages: {
            old_password: {
                required: "Please enter your old password"
            },
            new_password1: {
                required: "Please enter your new password"
            },
            new_password2: {
                required: "Please enter your new password again"
            }
        }
    });
});


setTimeout(function () {
    $('#message').fadeOut('slow');
}, 3000);
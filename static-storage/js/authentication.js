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

// Forms Validations
$(function () {
    // Custom password validators
    $.validator.addMethod("passLength", function (value, element) {
        return value.length >= 6;
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

    $.validator.addMethod('lettersonly', function (value, element) {
        return /^[a-zA-Z-,]+(\s{0,1}[a-zA-Z-, ])*$/.test(value);
    }, "Letters only please")

    $.validator.addMethod("numbersOnly", function (value, element) {
        return /^\d+$/.test(value);
    }, 'Intergers only please');

    $.validator.addMethod('fixedLength', function (value, element) {
        return /^\d{10}$/.test(value);
    }, "Please enter a <em>Valid Phone Number");


    // Login and register form validations
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
                required: "* Please enter an email address",
            },
            email_phone: {
                required: "* Please enter an email address or phone number",
            },
            pass: {
                required: "* Please enter the password"
            },
            password: {
                required: "* Please enter the password"
            },
            password1: {
                required: "* Please enter the password",
            },
            fname: {
                required: "* Please enter your first name"
            },
            lname: {
                required: "* Please enter your last name"
            }
        }
    });

    // Change password form validations
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

    // Order Address selection validations
    $("#addForm").validate({
        rules: {
            address_id: {
                required: true
            }
        },
        messages: {
            address_id: "* Please select your delivery address"
        }
    });

    // Update personal details validation
    $("#personaldetails").validate({
        rules: {
            first_name: {
                required: true,
                lettersonly: true
            },
            last_name: {
                required: true,
                lettersonly: true
            },
            dob: {
                required: true
            },
            gender: {
                required: true
            }
        },
        messages: {
            first_name: {
                required: "* Please enter your first name"
            },
            last_name: {
                required: "* Please enter your last name"
            },
            dob: {
                required: "* Please select your date of birth"
            },
            gender: {
                required: "* Please select your gender"
            }
        }
    });

    // Update address validation
    $("#addressdetails").validate({
        rules: {
            address_type: {
                required: true
            },
            address: {
                required: true
            },
            country: {
                required: true
            },
            state: {
                required: true
            },
            city: {
                required: true
            },
            zip_code: {
                required: true,
                numbersOnly: true
            }
        },
        messages: {
            address_type: {
                required: "* Please select address type"
            },
            address: {
                required: "* Please enter your address"
            },
            country: {
                required: "* Please select your country"
            },
            state: {
                required: "* Please select your state"
            },
            city: {
                required: "* Please select your city"
            },
            zip_code: {
                required: "* Please enter the zip code"
            }
        }
    });

    // Update email validations
    $("#emailAddresses").validate({
        rules: {
            email: {
                required: true,
                onlyEmail: true
            }
        },
        messages: {
            email: {
                required: "* Please enter your email address"
            }
        }
    });

    // Update phone number validation
    $("#phone").validate({
        rules: {
            phone: {
                required: true,
                numbersOnly: true,
                fixedLength: true
            }
        },
        messages: {
            phone: {
                required: "* Please enter your phone number"
            }
        }
    });

    // Product customizations validation
    $("#customize-product").validate({
        rules: {
            line1: {
                required: true
            },
            line2: {
                required: true
            },
            line3: {
                required: true
            },
            line4: {
                required: true
            },
            line5: {
                required: true
            },
            top_outer_circle_text: {
                required: true
            },
            monogram_initial: {
                required: true
            },
            center_text: {
                required: true
            },
            bottom_outer_circle_text: {
                required: true
            },
            below_arrow: {
                required: true
            }
        },
        messages: {
            line1: {
                required: "* Please fill the above input"
            },
            line2: {
                required: "* Please fill the above input"
            },
            line3: {
                required: "* Please fill the above input"
            },
            line4: {
                required: "* Please fill the above input"
            },
            line5: {
                required: "* Please fill the above input"
            },
            top_outer_circle_text: {
                required: "* Please fill the above input"
            },
            monogram_initial: {
                required: "* Please fill the above input"
            },
            center_text: {
                required: "* Please fill the above input"
            },
            bottom_outer_circle_text: {
                required: "* Please fill the above input"
            },
            below_arrow: {
                required: "* Please fill the above input"
            }
        }
    });
});

setTimeout(function () {
    $('#message').fadeOut('slow');
}, 3000);
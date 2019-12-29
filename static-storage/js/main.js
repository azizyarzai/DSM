const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

$(".avatar span").hover(function () {
    $(this).css("cursor", "pointer");
});

setTimeout(function () {
    $('#message').fadeOut('slow');
}, 5000);


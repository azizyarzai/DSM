$(document).ready(function () {
    setTimeout(function () {
        $('#message').fadeOut('slow');
    }, 5000);

    // Toggle dropdown menu on click of trigger element
    $(".edit-link").click(function () {
        // Hide other dropdown menus in case of multiple dropdowns
        $(".edit-menu").not($(this).next()).slideUp("fast");

        // Toggle the current dropdown menu
        $(this).next(".edit-menu").slideToggle("fast");
    });

    // Hide dropdown menu on click outside
    $(document).on("click", function (event) {
        if (!$(event.target).closest(".add-edit").length) {
            $(".edit-menu").slideUp("fast");
        }
    });
});


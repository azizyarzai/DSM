$(document).ready(function () {
    setTimeout(function () {
        $('#message').fadeOut('slow');
    }, 5000);


    // Address modal
    // Adding a new address
    $(".add-address").click(function () {
        console.log("clicked");
        $('#address-details-modal .add-btn').html("Add Address");
        $('#address-details-modal .modal-title').html("Add New Address");
        $('#address-details-modal input[name=address]').val('');
        $('#address-details-modal select[name=address_type]').val('').find("option[value='']").attr('selected', true);
        $('#address-details-modal select[name=country]').val('').find("option[value='']").attr('selected', true);
        $('#address-details-modal select[name=state]').val('').find("option[value='']").attr('selected', true);
        $('#address-details-modal select[name=city]').val('').find("option[value='']").attr('selected', true);
        $('#address-details-modal input[name=zip_code]').val('');
        $('#address-details-modal input[name=address_id]').val('').prop("disabled", true);
        $('#address-details-modal form').attr('action', "/accounts/profile/address/add-address/");
    });

    // Editing an existing address
    $(".edit-btn").click(function () {
        $('#address-details-modal .add-btn').html("Save Changes");
        $('#address-details-modal .modal-title').html("Address Details");
        addressType = $(this).find(".address-type").html();
        addressId = $(this).find(".address-id").html();
        address = $(this).find(".address").html();
        country = $(this).find(".country").html();
        state = $(this).find(".state").html();
        city = $(this).find(".city").html();
        zipCode = $(this).find(".zip-code").html();
        $('#address-details-modal select[name=address_type]').val(addressType).find("option[value=" + addressType + "]").attr('selected', true);
        $('#address-details-modal input[name=address]').val(address);
        $('#address-details-modal select[name=country]').val('').find("option[value='']").attr('selected', true);
        $('#address-details-modal select[name=state]').val('').find("option[value='']").attr('selected', true);
        $('#address-details-modal select[name=city]').val('').find("option[value='']").attr('selected', true);
        $('#address-details-modal input[name=zip_code]').val(zipCode);
        $('#address-details-modal input[name=address_id]').val(addressId).prop("disabled", false);
        $('#address-details-modal form').attr('action', "/accounts/profile/address/" + addressId + "/update-address/");
    });
});


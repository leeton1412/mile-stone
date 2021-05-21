// Stripe Vars
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

// Stripe Styles

var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Validation Errors
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span> 
                <i class="fas fa-times" role="alert"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Stripe Submisson.
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    stripe.confirmCardPayment(client_secret, {
        payment_method: {
            card: card,
            billing_details:{
                name: $.trim(form.full_name.value),
                email:$.trim(form.email.value),
                phone:$.trim(form.phone_number.value),
                address:{
                    line1:$.trim(form.street_address1.value),
                    line2:$.trim(form.street_address2.value),
                    city:$.trim(form.town_or_city.value),
                    county:$.trim(form.county.value),
                    country:$.trim(form.country.value),
                }
            }
        },
        shipping: {
                name: $.trim(form.full_name.value),
                phone:$.trim(form.phone_number.value),
                address:{
                    line1:$.trim(form.street_address1.value),
                    line2:$.trim(form.street_address2.value),
                    city:$.trim(form.town_or_city.value),
                    postcode:$.trim(form.postcode.value),
                    county:$.trim(form.county.value),
                    country:$.trim(form.country.value),
                }
        },
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});
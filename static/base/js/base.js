    $.ajax({
        type: "POST",
        url: "{% url 'accounts:login' %}",
        data: $('#login_form').serialize(),
        success: function (response) {
            // do something with response
            response['email'];
            response['password']
        }
    });
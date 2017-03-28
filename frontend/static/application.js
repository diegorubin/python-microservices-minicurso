$(document).ready(function(){

  $('#login').click(function(event) {
    event.preventDefault();
    $('#login-modal').modal('show');
  });

  $('#login-button').click(function(event) {
    event.preventDefault();

    var data = {
      email: $('#email-input').val(),
      password: $('#password-input').val()
    };

    $.ajax({ 
      url: '/auth', 
      method: 'post', 
      data: data
    }).done( function() {
      $('#login-modal').modal('hide');
    }).fail( function(response) {
      var responseData = response.responseJSON;
      $('#login-error').html(responseData.data.message);
    });
  });
});


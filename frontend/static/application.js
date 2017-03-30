$(document).ready(function(){

  $('#login').click(function(event) {
    event.preventDefault();
    $('#login-modal').modal('show');
  });

  $('#new-user').click(function(event) {
    event.preventDefault();
    $('#user-modal').modal('show');
  });

  $('#login-button').click(function(event) {
    event.preventDefault();

    var data = {
      email: $('#email-input').val(),
      password: $('#password-input').val()
    };

    $.ajax({ 
      url: '/sessions', 
      method: 'post', 
      data: data
    }).done( function() {
      $('#login-modal').modal('hide');
      window.location.reload();
    }).fail( function(response) {
      var responseData = response.responseJSON;
      $('#login-error').html(responseData.data.message);
    });
  });

  $('#logout').click(function(event) {
    event.preventDefault();

    $.ajax({ 
      url: '/sessions', 
      method: 'delete'
    }).done( function() {
      console.log("teste");
      window.location.reload();
    });
  });

  $('#user-button').click(function(event) {
    event.preventDefault();

    var data = {
      name: $('#user-name-input').val(),
      email: $('#user-email-input').val(),
      password: $('#user-password-input').val()
    };

    $.ajax({ 
      url: '/api/users', 
      method: 'post', 
      data: data
    }).done( function() {
      $('#user-modal').modal('hide');
      window.location.reload();
    }).fail( function(response) {
      var responseData = response.responseJSON;
      $('#user-error').html(responseData.data.message);
    });
  });

});



function pushToDB() {
  var fname = document.getElementById('firstName');
  var pushData = {
    FirstName: fname,
    LastName: document.getElementById('lastName'),
    Email: document.getElementById('email'),
    SJSUID: document.getElementById('sjsuid'),
    Username: document.getElementById('user'),
    Password: document.getElementById('pass')
  };
  var url = '/dbUpdate';
  $.post({
        contentType: 'application/json',
        dataType: 'json',
        data: JSON.stringify(pushData),
        url: url,
        error:function() {
            alert('Sorry, an error occurred. Please contact Nick, and try again later.');
        },
        success:function(response) {
            alert("Thanks "+ fname +"! You've been added to our user database! If you have any questions, please ask Nick.");
        }
    });
}

function submitSignup() {
  if(document.getElementById('sjsuid').value.length!=9){
    alert("Please enter your nine digit ID, or nine zeroes for ID if you're not a student.");
    return false;
  } else if (document.getElementById('pass') != document.getElementById('passconfirm')) {
    alert("Passwords do not match.");
    return false;
  }
  var request = $.ajax({'url': '/formValidationQuery'});
  request.done(function(response){
    var data = JSON.parse(response);
    var uname = document.getElementById('user');
    var email = document.getElementById('email');
    var id = document.getElementById('sjsuid');
    if(data.usernames.indexOf(uname)>=0){
      alert("Username already taken. Please try another!");
      return false;
    } else if(data.emails.indexOf(email)>=0) {
      alert("Email already registered. Please contact Nick for assistance with account recovery!");
      return false;
    } else if(data.sjsuids.indexOf(id)>=0) {
      alert("SJSU ID already registered. Please contact Nick for assistance with account recovery!");
      return false;
    }
    pushToDB();
    return true;
  });
  request.fail(function(jqXHR, textStatus){
    alert("Request failed, contact Nick with the following: " + textStatus);
    return false;
  });
}

$(document).ready(function() {
  $(".navbar-nav li").on("click", function(){
    $(".nav").find(".active").removeClass("active");
    if($(this).parent().parent().className == "dropdown") {
      $(this).parent().parent().addClass("active");
    } else {
      $(this).addClass("active");
    }
  });
});

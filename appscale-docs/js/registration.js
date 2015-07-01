$(document).ready(function(){
  $(function () {
    $('#first_name').focus();
    $('#c_password').keyup(function () {
      if($(this).val() != $('#password1').val()){
        $('#passwords_match').show();
        $('#signup').prop('disabled', true);
      }
      else{
        $('#passwords_match').hide();
        $('#signup').prop('disabled', false);
      }
    });             
  });
  function registerUser(username) {
    $.ajax({
      url: "/checkusername",
      cache: false,
      data:{'username' : username},
      success: function(result){
        alert("Ajax request success");
    }});
  }

});
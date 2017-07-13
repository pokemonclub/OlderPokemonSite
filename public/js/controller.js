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

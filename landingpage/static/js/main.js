$(document).ready(function () {
  $('nav a').on('click', function (e) {
    var href = $(this).attr('href');
    if (href !== '/login' && href !== '/logout' && href !== '/home' && href !== '/' && href !== "/profile") {
      e.preventDefault();
      var target = $(href);
      var offset = target.offset().top;
      $('html, body').animate({
        scrollTop: offset
      }, 700);
    }
  });
});




$(document).ready(function () {
  // Add click event handler for scroll-to-top button
  $('#scrollToTop').on('click', function () {
    $('html, body').animate({
      scrollTop: 0
    }, 800);
  });
});


// create a function to get class messages and remove all of its elements 
function clearMsg() {
  console.log("message cleared")
  var messages = document.getElementsByClassName("messages");
  messages.remove()
}



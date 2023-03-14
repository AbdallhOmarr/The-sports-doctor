$(document).ready(function() {
  $('nav a').on('click', function(e) {
    var href = $(this).attr('href');
    if (href !== '/login' && href !== '/logout' && href !== '/home' && href !=='/') {
      e.preventDefault();
      var target = $(href);
      var offset = target.offset().top;
      $('html, body').animate({
        scrollTop: offset
      }, 700);
    }
  });
});




$(document).ready(function() {
  // Add click event handler for scroll-to-top button
  $('#scrollToTop').on('click', function() {
    $('html, body').animate({
      scrollTop: 0
    }, 800);
  });
});


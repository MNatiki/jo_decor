jQuery(document).ready(function($) {
  $(".scroll a, .navbar-brand, .gototop").click(function(event){   
      event.preventDefault();
      
      // Check if this.hash is defined and not empty
      if (this.hash !== "" && $(this.hash).length) {
          $('html,body').animate({scrollTop:$(this.hash).offset().top}, 600,'swing');
          $(".scroll li").removeClass('active');
          $(this).parents('li').toggleClass('active');
      }
  });
});

var wow = new WOW({
  boxClass:     'wowload',
  animateClass: 'animated',
  offset:       0,
  mobile:       true,
  live:         true
});
wow.init();

$('.carousel').swipe({
  swipeLeft: function() {
      $(this).carousel('next');
  },
  swipeRight: function() {
      $(this).carousel('prev');
  },
  allowPageScroll: 'vertical'
});

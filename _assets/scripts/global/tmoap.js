(function($) {
  "use strict"; // Start of use strict

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: (target.offset().top - 70)
        }, 750, "easeInOutExpo"); // The -70 stops the bouncing effect...
        return false;
      }
    }
  });

  // Closes burger menu by unchecking the checkbox when a scroll trigger link is clicked
  $('.js-scroll-trigger').click(function() {
    $('#menu-burger').prop("checked", false);
  });

})(jQuery); // End of use strict


// FANCY BOX
$(document).ready(function(){
  $(".fancybox").fancybox({ // All parameters available at http://fancybox.net/api
        openEffect: "fade",
        closeEffect: "fade",
        padding: 0,
        scrolling: "yes"
    });
    
    $(".zoom").hover(function(){
		
		$(this).addClass('transition');
	}, function(){
        
		$(this).removeClass('transition');
	});
});


// Initialise Swiper
var galleryThumbs = new Swiper('.gallery-thumbs', {
  spaceBetween: 10,
  slidesPerView: 5,
  freeMode: true,
  watchSlidesVisibility: true,
  watchSlidesProgress: true,
});
var galleryTop = new Swiper('.gallery-top', {
  spaceBetween: 20,
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  thumbs: {
    swiper: galleryThumbs
  }
});

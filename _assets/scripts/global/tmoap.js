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

  	//https://css-tricks.com/snippets/jquery/shuffle-dom-elements/
      $.fn.shuffle = function() {
 
        var allElems = this.get(),
            getRandom = function(max) {
                return Math.floor(Math.random() * max);
            },
            shuffled = $.map(allElems, function(){
                var random = getRandom(allElems.length),
                    randEl = $(allElems[random]).clone(true)[0];
                allElems.splice(random, 1);
                return randEl;
           });
 
        this.each(function(i){
            $(this).replaceWith($(shuffled[i]));
        });
 
        return $(shuffled);
 
    };
 

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

$(document).ready(function(){
		var list_to_hide = $('.list_to_hide_or_not_hide');
		var selected_cards = list_to_hide.find(".cards__item");
		selected_cards.shuffle();


        selected_cards = list_to_hide.find(".cards__item");
		all_cards = selected_cards.toArray();
		var counter = 0;
   		var numberOfPosts = list_to_hide.data('limit');
		while (counter < all_cards.length)
	    {
	        if (counter >= numberOfPosts){
	        	all_cards[counter].remove();
	        }
	        counter++;
	    }
	    list_to_hide.removeAttr("style");
	});

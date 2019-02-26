$(document).ready(function() {
   
  var lastScrollTop = 0;
$(window).scroll(function(event){
   var st = $(this).scrollTop();
   var scrollH =  $(window).scrollTop();
   if (scrollH > 50){
       // downscroll code
       //alert('down');
       $('.main-menu').addClass('sticky');
    $('.full-menu').addClass('sticky');
     
       
   } else {
      // upscroll code
    
    $('.main-menu').removeClass('sticky');
       $('.full-menu').removeClass('sticky');
   }
   lastScrollTop = st;
});


});



$('.owl-carousel').owlCarousel({
    loop:true,
    margin:30,
    nav:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:4
        }
    }
});
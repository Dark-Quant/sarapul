$(function(){ 
    let navigation_list = $("#navigation__list"); 
    let navigation_arrow = $("#navigation__arrow");

    function replaceClass(object, oldClass, newClass) {
        object.removeClass(oldClass);
        object.addClass(newClass);
    }


    // Menu right
    $("#navigation__arrow").on("click", function(event) {
        event.preventDefault();
        console.log("test");
        if(navigation_arrow.hasClass("left")){
            replaceClass(navigation_arrow, "left", "right");
            $(navigation__list).toggleClass("show");
        }else {
            replaceClass(navigation_arrow, "right", "left");
            $(navigation__list).toggleClass("show");
        }
    });

    /* Testimonials: https://kenwheeler.github.io/slick/ */
    slider = $("#testimonialsSlider");    

    slider.slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        fade: true,
        arrows: false,
        dots: true
      });
      
    
});
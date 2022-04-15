$(function(){
    let profile = $("#profile");
    let profile_items = $("#profile__items");
    profile_items.offset({top: profile.offset().top-75, left: profile.offset().left-25});
    profile.on("click", function(event) {
        event.preventDefault();
        profile_items.toggleClass("on");
        if(profile_items.hasClass("on")){
            profile_items.show();
        }else{
            profile_items.hide();
        }
    });
});
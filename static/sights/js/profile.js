$(function(){
    let profile = $("#profile");
    let profile_items = $("#profile__items");
    console.log(profile.offset().left)
    profile_items.position = "absolute";
    profile_items.offset({top: profile.offset().top+45, left: profile.offset().left});
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
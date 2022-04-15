$(document).ready(function() {
    $('#popup').hide();
});

$('#popup__cross').on('click', function(event){
    $('#popup').hide();
});

function printContent(content){
    $('#popup__content').text(content);
}
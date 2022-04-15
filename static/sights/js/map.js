var map = L.map(
    "map",
    {
        center: [56.461218, 53.803687],
        crs: L.CRS.EPSG3857,
        zoom: 10,
        zoomControl: true,
        preferCanvas: false,
    }
);


var tile_layer = L.tileLayer(
    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    {
        "attribution": "Data by \u0026copy; \u003ca href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca href=\"http://www.openstreetmap.org/copyright\"\u003eODbL\u003c/a\u003e.",
        "detectRetina": false,
        "maxNativeZoom": 18,
        "maxZoom": 18,
        "minZoom": 0,
        "noWrap": false,
        "opacity": 1,
        "subdomains": "abc",
        "tms": false
    }
).addTo(map);

function printContent(content){
    console.log(content)
}

var sights = new Array()


function onMapClick(e) {
    console.log("You clicked the map at " + e.latlng);
    $.ajax({
        url: '/api/v1/get_sights/',
        method: 'get',
        dataType: 'json',
        success: function (data) {
            $('#popup').show();
            let sight = data[sights.indexOf(e.target)];
            $('#popup__title').text(sight.title);
            $('#popup__text').text('{{' + sight.description +'|linebreaks|truncatewords:1}}');
            $('#popup__photo').attr('src', sight.photo);
        }

    });
}


$.ajax({
    url: '/api/v1/get_sights/',
    method: 'get',
    dataType: 'json',
    success: function (data) {
        for (i in data){
            sights.push(L.marker([data[i].latitude, data[i].longitude]).addTo(map).on('click', onMapClick));
        }
    }

});


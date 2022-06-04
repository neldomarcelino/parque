var map
$(window).on('map:init', function (e) {
    var detail = e.originalEvent ? e.originalEvent.detail : e.detail;
    map = detail.map;
    L.marker([50.5, 30.5]).addTo(map);
    map.addControl(new L.Control.Fullscreen());
    L.control.locate().addTo(map);
    L.control.browserPrint().addTo(map);
    var searchLayer = L.layerGroup().addTo(map);
    map.addControl( new L.Control.Search({layer: searchLayer}) );

    let specieData = new L.GeoJSON.AJAX("{% url 'speciegeo' %}",{

    });
    specieData.addTo(map);

});


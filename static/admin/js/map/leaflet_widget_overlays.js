window.addEventListener("map:init", function (event) {
    var map = event.detail.map; // Get reference to map

    // Other modifications, e.g. fullscreen control:
    map.addControl(new L.Control.Fullscreen());
    // Note, this requires the Leaflet fullscreen CSS, JS,
    // and image assets to be present as static files,
    // and configured in LEAFLET_SETTINGS
});
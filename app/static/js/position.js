
function centerMap(position) {
    var center = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
    };

    map.panTo(center);
}

function getPosition() {
    return {lat: 70, lng: -30};
}
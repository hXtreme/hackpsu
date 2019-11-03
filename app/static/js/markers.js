function placeMarker(map, person) {

    var icon_person = '<i class="fas fa-user-md"></i>';

    if(person.type == 'requester')
    {
        icon_person = '<i class="fas fa-star-of-life"></i>';
    }

    var marker = new google.maps.Marker({
            position: person.position,
            icon: icon_person,
            map: map
          });

}


function clearMarkers() {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(null);
    }
    markers = [];
}

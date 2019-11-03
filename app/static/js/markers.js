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

      var infowindow = getInfoWindow(person);

      marker.addListener('click', function() {
        infowindow.open(map, marker);
      });

}

function getInfoWindow(person) {
    var content = '<div class="infowindow">'+
              '<p>'+
              person.first_name +" "+ person.last_name +"<br>"+
              person.phone +" "+ person.email +"<br>"+
              '</p>'
              '</div>';
    if(person.type == 'requester')
    {
          var content = '<div class="infowindow">'+
              '<p>'+
              person.username +
              '</p>' +
              '<p>' +
               person.message +
              '</p>' +
              '<button onclick="respond()">Respond!</button>'+
              '</div>';
    }
  var infowindow = new google.maps.InfoWindow({content: content});
  return infowindow;
}

function respond() {

// TODO
// Change the persons status to serviced - delete from queue


}


function clearMarkers() {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(null);
    }
    markers = [];
}

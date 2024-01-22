

document.addEventListener("DOMContentLoaded", function () {
  var map = L.map("map").setView([51.505, -0.09], 13);

  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 19,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
  }).addTo(map);

  // Sample ATM and Bank Branch data (replace this with your actual data)
  var locations = [
      {lat: 51.5, lng: -0.09, name: 'ATM 1'},
      {lat: 51.52, lng: -0.1, name: 'Bank Branch 1'},
      // Add more locations as needed
  ];

  // Loop through locations and add markers to the map
  locations.forEach(function (location) {
      var marker = L.marker([location.lat, location.lng]).addTo(map);
      marker.bindPopup('<b>' + location.name + '</b>');
  });
});

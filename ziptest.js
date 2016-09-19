var ChipsAndGuac = require('chipsandguac');

ChipsAndGuac.getNearbyLocations("37129").then(function(locations) {
  console.log(JSON.stringify(locations));
});
var ChipsAndGuac = require('./chipsandguac.js');

var cag = new ChipsAndGuac({email:'jacobquatier@gmail.com', password:'travis01', locationId: '512', phoneNumber:'503.970.3621'});

ChipsAndGuac.getNearbyLocations("97229").then(function(locations) { console.log(JSON.stringify(locations));});

/*console.log("loggedin=" + cag.isLoggedIn());
cag.login().then(function() {
  cag.getOrders().then(function(orders) {
    console.log("orders: " + JSON.stringify(orders));
    cag.submitPreviousOrderWithId(41531521, true).then(function(orderDetails) {
      console.log(orderDetails);
    });
  });
});*/


  
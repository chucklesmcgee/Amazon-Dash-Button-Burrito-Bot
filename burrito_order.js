var ChipsAndGuac = require('chipsandguac');

// instantiate a new ChipsAndGuac object, passing in required configuration and credentials.
var cag = new ChipsAndGuac({
  email:'YOUR CHIPOTLEEMAIL', 
  password:'YOURCHIPOTLEPASSWORD', 
  locationId: '2067', 
  phoneNumber:'123.456.7890' // must match user profile
});

cag.submitPreviousOrderWithId(57072187, false).then(function(orderDetails) {

});

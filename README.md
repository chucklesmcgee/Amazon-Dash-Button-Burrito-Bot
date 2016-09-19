# First off
This is a program cobbled together using Aaron Bell's code and method to crack the Amazon Dash button and subvert it to non-Amazon purchases (bwahahaha).
1. Follow instructions here: http://www.aaronbell.com/how-to-hack-amazons-wifi-button/ to get your hardware up and running. "dashifttt.py" incorporates his code.
2. Follow readme taken from ChipsAndGuac below to get the chipotle end up and running. You'll need to use the test script to pull your Chipotle location number and order and stick that into the burrito order script.
3. I used something to make python call java and run the script, which I think was the Naked Shell library.
4. Script gives an error after a successful Chipotle order, but doesn't crash script or disupt monitoring.
5. When everything's good to go, run dashifttt.py and click.


# ChipsAndGuac


Node.js API for programmatically ordering from the Chipotle website. This module can be used for locating nearby Chipotle restaurants, looking up favorite and recent orders, checking available pickup times, and of course, placing orders. 

[![NPM](https://nodei.co/npm/chipsandguac.png)](https://nodei.co/npm/chipsandguac/)

### Usage

#### Find nearby locations (useful for getting location ID)
Note: This method is static and must be called using the class name, instead of off an instance of the class.
```javascript
var ChipsAndGuac = require('chipsandguac');

ChipsAndGuac.getNearbyLocations("80123").then(function(locations) {
  console.log(JSON.stringify(locations));
});

// output (Array)
[ 
  { id: 1430, name: '8100 W. Crestline Ave' },
  { id: 644, name: '3170 S. Wadsworth' },
  { id: 970, name: '5699 S. Broadway' },
  { id: 71, name: '12512 W. Ken Caryl Ave.' },
  { id: 390, name: '333 W. Hampden Ave.' } 
]
```

#### Create a new instance of ChipsAndGuac with required configuration.
```javascript
var ChipsAndGuac = require('chipsandguac');

// instantiate a new ChipsAndGuac object, passing in required configuration and credentials.
var cag = new ChipsAndGuac({
  email:'EMAIL_GOES_HERE', 
  password:'PASSWORD_GOES_HERE', 
  locationId: 'LOCATION_ID', 
  phoneNumber:'555.555.5555' // must match user profile
});
```

Note: All methods below require an instance of ChipsAndGuac. "cag" is the instance used in these examples.

#### Look up recent orders (useful for getting previous order ID)
```javascript
cag.getOrders().then(function(orders) {
  console.log(orders);
});

// output (Array)
[
  {
    "id": 123456789,
    "name":"Recent Order #1",
    "items":[
      {
        "name":"1 x Chicken Burrito Bowl",
        "details":"Brown Rice, Black Beans, Extra Chicken, Fresh Tomato Salsa, Tomatillo-Red Chili Salsa, Cheese"
      }
    ]
  }
]
```

#### Place an order (using a previous order ID)
Note: passing `true` for the second argument in this call will NOT place an order. This is useful for previewing the order and looking up the next available pickup time. If this parameter is left off, or if `false` is passed, the order WILL be placed.
```javascript
cag.submitPreviousOrderWithId(123456789, true).then(function(orderDetails) {
  console.log(orderDetails);
});

// output
{
  pickupTimes: [ '5/14/2015 9:30:00 PM', '5/14/2015 9:45:00 PM' ],
  items:     '10/24/2015 8:45:00 PM',

   [ { name: 'Your Name',
       itemName: 'Chicken Burrito Bowl',
       itemDetails: '...' }],
  location: '8100 W Crestline Ave, Denver, CO 80123' 
}
```


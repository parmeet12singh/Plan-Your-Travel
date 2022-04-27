// This example adds an animated symbol to a polyline.
function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 23.5, lng: 82.3 },
        zoom: 5,
    });

    source = ['New Delhi', 28.624244969987007, 77.20644188699403,]

    createMarker(map, source);

    destination = [
        ['Bhubaneswar', 20.28105765, 85.81140263163533],
        ['Tashkent', 41.3123363, 69.2787079],
        ['Kyiv', 50.4500336, 30.5241361],
        ['Zurich', 47.3744489, 8.5410422],
        ['Jaisalmer', 27.02801615, 70.7785056232077],
        ['Shirdi', 19.7668121, 74.4754386],
        ['Pakyong', 27.2475715, 88.6197175267062],
        ['Kushinagar', 26.7438272, 83.9162322],
        ['Kanpur', 26.4609135, 80.3217588],
        ['Kandla', 58.36972845, 22.29574379119859],
        ['Jharsuguda', 21.87705125, 84.00905063735019],
        ['Darbhanga', 26.08314325, 86.03257096612822],
        ['Belgaum', 15.8572666, 74.5069343],
        ['Ajmer', 26.4691, 74.639],
        ['Adelaide', -34.9281805, 138.5999312],
        ['Munich', 48.1371079, 11.5753822],
        ['Warsaw', 52.2319581, 21.0067249],
        ['Seoul', 37.5666791, 126.9782914],
        ['Amsterdam', 52.3727598, 4.8936041],
        ['Tiruchirappalli', 10.804973, 78.6870296],
        ['Pantnagar', 29.0264162, 79.4859989],
        ['Mangalore', 12.8698101, 74.8430082],
        ['Kuala Lumpur', 3.1516964, 101.6942371],
        ['Jorhat', 26.7577925, 94.2079645],
        ['Jeddah', 21.5810088, 39.1653612],
        ['Istanbul', 41.0091982, 28.9662187],
        ['Durgapur', 23.5350475, 87.3380425],
        ['Dimapur', 25.9136459, 93.7283456],
        ['Chengdu', 30.6598628, 104.0633717],
        ['Phuket', 7.9366015, 98.3529292],
        ['Malé', 4.1779879, 73.5107387],
        ['Aizawl', 23.7435236, 92.7382905],
        ['Helsinki', 60.1674881, 24.9427473],
        ['Addis Ababa', 9.0107934, 38.7612525],
        ['Taipei', 25.0375198, 121.5636796],
        ['Dhaka', 23.7861979, 90.4026151],
        ['Pathankot', 32.2692452, 75.6528858],
        ['Nashik', 20.0112475, 73.7902364],
        ['Kullu', 32.00186325, 77.37899639741332],
        ['Jabalpur', 23.1608938, 79.9497702],
        ['Gorakhpur', 26.6711433, 83.36457243864551],
        ['Dharamshala', 32.2143039, 76.3196717],
        ['Dehradun', 30.3255646, 78.0436813],
        ['Bilaspur', 28.8680526, 79.29838501460121],
        ['Bikaner', 28.0159286, 73.3171367],
        ['Bareilly', 28.4157769, 79.45264865437258],
        ['Allahabad', 25.4381302, 81.8338005],
        ['Janakpur', 26.7281124, 85.93643035322714],
        ['Madurai', 9.9261153, 78.1140983],
        ['Washington', 38.8950368, -77.0365427],
        ['Visakhapatnam', 17.7231276, 83.3012842],
        ['Vijayawada', 16.5087586, 80.6185102],
        ['Varanasi', 25.3356491, 83.0076292],
        ['Vadodara', 22.2973142, 73.1942567],
        ['Udaipur', 24.578721, 73.6862571],
        ['Tokyo', 35.6828387, 139.7594549],
        ['Tirupati', 13.6316368, 79.4231711],
        ['Thiruvananthapuram', 8.5241122, 76.9360573],
        ['Tel Aviv', 32.0852997, 34.7818064],
        ['Sydney', -33.8548157, 151.2164539],
        ['Srinagar', 34.0747444, 74.8204443],
        ['Singapore', 1.357107, 103.8194992],
        ['San Francisco', 37.7790262, -122.419906],
        ['Riyadh', 24.638916, 46.7160104],
        ['Ranchi', 23.3700501, 85.3250387],
        ['Rajkot', 22.3053263, 70.8028377],
        ['Pune', 18.521428, 73.8544541],
        ['Port Blair', 11.6645348, 92.7390448],
        ['Patna', 25.6093239, 85.1235252],
        ['New York', 40.7127281, -74.0060152],
        ['Newark', 40.735657, -74.1723667],
        ['Nanded', 19.09400875, 77.48319215130235],
        ['Nagpur', 21.1498134, 79.0820556],
        ['Muscat', 23.61515, 58.5912467],
        ['Mumbai', 19.0759899, 72.8773928],
        ['Melbourne', -37.8142176, 144.9631608],
        ['Lucknow', 26.8381, 80.9346001],
        ['London', 51.5073219, -0.1276474],
        ['Kuwait  City', 29.3797091, 47.9735629],
        ['Kozhikode', 11.2450558, 75.7754716],
        ['Kolkata', 22.5414185, 88.35769124388872],
        ['Kochi', 9.931308, 76.2674136],
        ['Kathmandu', 27.708317, 85.3205817],
        ['Kannur', 11.8763391, 75.3737987],
        ['Kabul', 34.5260109, 69.1776838],
        ['Jodhpur', 26.2967719, 73.0351433],
        ['Jammu', 32.7185614, 74.8580917],
        ['Jaipur', 26.9154576, 75.8189817],
        ['Indore', 22.7203616, 75.8681996],
        ['Hyderabad', 17.360589, 78.4740613],
        ['Hong Kong', 22.2793278, 114.1628131],
        ['Guwahati', 26.1578514, 91.69164600906831],
        ['Goa', 15.3503192, 74.10178169795284],
        ['Gaya', 24.7964355, 85.0079563],
        ['Frankfurt', 50.1106444, 8.6820917],
        ['Dubai', 25.2653471, 55.2924914],
        ['Doha', 25.2856329, 51.5264162],
        ['Dibrugarh', 27.4844597, 94.9019447],
        ['Dammam', 26.4367824, 50.1039991],
        ['Colombo', 6.9387469, 79.8541134],
        ['Coimbatore', 11.0018115, 76.9628425],
        ['Chicago', 41.8755616, -87.6244212],
        ['Chennai', 13.0836939, 80.270186],
        ['Chandigarh', 30.7334421, 76.7797143],
        ['Leh', 34.1642029, 77.5848133],
        ['Raipur', 21.2379469, 81.6336833],
        ['Imphal', 24.7991162, 93.9364419],
        ['Moscow', 55.7504461, 37.6174943],
        ['Abu Dhabi', 24.4538352, 54.3774014],
        ['Sharjah', 25.3461498, 55.4210633],
        ['Almaty', 43.2363924, 76.9457275],
        ['Montreal', 45.5031824, -73.5698065],
        ['Toronto', 43.6534817, -79.3839347],
        ['Vancouver', 49.2608724, -123.113952],
        ['Paris', 48.8588897, 2.3200410217200766],
        ['Agartala', 23.8312377, 91.2823821],
        ['Ahmedabad', 23.0216238, 72.5797068],
        ['Amritsar', 31.6343083, 74.8736788],
        ['Aurangabad', 19.877263, 75.3390241],
        ['Bagdogra', 26.6988847, 88.3200303],
        ['Bahrain', 26.1551249, 50.5344606], 
        ['Bangalore', 12.9767936, 77.590082], 
        ['Bangkok', 13.7525438, 100.4934734],
        ['Bhopal', 23.2584857, 77.401989]
    ]

    for (i = 0; i < destination.length; i++) {
        createPath(map, source, destination[i]);
    }
}

function createMarker(map, coordinates) {

    marker = new google.maps.Marker({
        map,
        animation: google.maps.Animation.DROP,
        position: { lat: coordinates[1], lng: coordinates[2] },
        title: coordinates[0],
    });

    // const contentString = '<div><h5>'+coordinates[2]+'</h5><img src="https://img.icons8.com/fluency/48/000000/red-fort.png/"></div>'

    const infowindow = new google.maps.InfoWindow({
        content: coordinates[0],
        maxWidth: 200,
        position: { lat: coordinates[1], lng: coordinates[2] },
      });

      marker.addListener("click", () => {
        infowindow.open({
          map,
          shouldFocus: false,
        });
      });

      google.maps.event.addListener(map, "click", function(event) {
        infowindow.close();
    });

}

function createPath(map, source, destination) {

    // Define the symbol, using one of the predefined paths ('FORWARD_CLOSED_ARROW')
    // supplied by the Google Maps JavaScript API.
    const lineSymbol = {
        path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW,
        scale: 4,
        strokeColor: "#393",
        strokeOpacity: 4.0,
        strokeWeight: 2,
    };

    const symbol = {
            path: "M362.985,430.724l-10.248,51.234l62.332,57.969l-3.293,26.145 l-71.345-23.599l-2.001,13.069l-2.057-13.529l-71.278,22.928l-5.762-23.984l64.097-59.271l-8.913-51.359l0.858-114.43 l-21.945-11.338l-189.358,88.76l-1.18-32.262l213.344-180.08l0.875-107.436l7.973-32.005l7.642-12.054l7.377-3.958l9.238,3.65 l6.367,14.925l7.369,30.363v106.375l211.592,182.082l-1.496,32.247l-188.479-90.61l-21.616,10.087l-0.094,115.684",
            scale: 4,
            strokeColor: "#393",
            strokeOpacity: 4.0,
            strokeWeight: 2,
        }
        // Create the polyline and add the symbol to it via the 'icons' property.
    const line = new google.maps.Polyline({
        path: [
            { lat: source[1], lng: source[2] },
            { lat: destination[1], lng: destination[2] },
        ],
        icons: [{
            icon: lineSymbol,
            offset: "100%",
        }, ],
        map: map,
        geodesic: true,
        strokeColor: "#FF0000",
        strokeOpacity: 2.0,
        strokeWeight: 1,
    });

    createMarker(map, destination);

    animateSymbol(line);
}

// Use the DOM setInterval() function to change the offset of the symbol
// at fixed intervals.
function animateSymbol(line) {
    let count = 0;

    window.setInterval(() => {
        count = (count + 1) % 300;

        const icons = line.get("icons");

        icons[0].offset = count / 3 + "%";
        line.set("icons", icons);
    }, 20);
}
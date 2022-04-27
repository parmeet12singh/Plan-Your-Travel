// This example adds an animated symbol to a polyline.
function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 23.5, lng: 82.3 },
        zoom: 5,
    });
    // Define the symbol, using one of the predefined paths ('FORWARD_CLOSED_ARROW')
    // supplied by the Google Maps JavaScript API.
    const lineSymbol = {
        path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW,
        scale: 4,
        strokeColor: "#393",
        strokeOpacity: 4.0,
        strokeWeight: 2,
    };
    // Create the polyline and add the symbol to it via the 'icons' property.
    const line = new google.maps.Polyline({
        path: [
            { lat: 28.624244969987007, lng: 77.20644188699403 },
            { lat: 34.152889453733664, lng: 77.57703492681053 },
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

    const line1 = new google.maps.Polyline({
        path: [
            { lat: 28.624244969987007, lng: 77.20644188699403 },
            { lat: 11.62363527561463, lng: 92.7294094732801 },
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

    const line2 = new google.maps.Polyline({
        path: [
            { lat: 28.624244969987007, lng: 77.20644188699403 },
            { lat: 15.402130205788042, lng: 73.80355648515068 },
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

    const line3 = new google.maps.Polyline({
        path: [
            { lat: 28.624244969987007, lng: 77.20644188699403 },
            { lat: 26.45316769646645, lng: 80.3260231309282 },
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

    animateCircle(line);
    animateCircle(line1);
    animateCircle(line2);
    animateCircle(line3);
}

// Use the DOM setInterval() function to change the offset of the symbol
// at fixed intervals.
function animateCircle(line) {
    let count = 0;

    window.setInterval(() => {
        count = (count + 1) % 500;

        const icons = line.get("icons");

        icons[0].offset = count / 5 + "%";
        line.set("icons", icons);
    }, 20);
}
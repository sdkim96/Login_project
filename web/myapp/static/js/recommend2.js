let recommend2_competitor = document.getElementById('competitor');
let recommend2_bus = document.getElementById('bus');
let recommend2_subway = document.getElementById('subway');
let recommend2_population = document.getElementById('population');
let recommend2_attraction = document.getElementById('attraction');
let recommend2_shopping = document.getElementById('shopping');
  
function calculateHotelLocation() {
    let competitor = recommend2_competitor.value;
    let bus = recommend2_bus.value;
    let subway = recommend2_subway.value;
    let population = recommend2_population.value;
    let attraction = recommend2_attraction.value;
    let shopping = recommend2_shopping.value;

    console.log(competitor)
    console.log(bus)
    console.log(subway)
    console.log(population)
    console.log(attraction)
    console.log(shopping)

    let data = {
        'competitor': competitor,
        'bus': bus,
        'subway': subway,
        'population': population,
        'attraction': attraction,
        'shopping': shopping,
    };

    fetch('/recommend_02/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('hotel-location-result').innerHTML = data.location;
    });
}




  
  

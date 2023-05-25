document.addEventListener("DOMContentLoaded", function() {
    generateHotelName();
  });

function generateHotelName(){
    var recommend3Content1 = document.getElementById("hotel-grade-result");
    var recommend3Content2 = document.getElementById("hotel-location-result");

    let recommend3Content1ToEndpoint = recommend3Content1.textContent
    let recommend3Content2ToEndpoint = recommend3Content2.textContent

    let data2 = {
        'content1': recommend3Content1ToEndpoint,
        'content2': recommend3Content2ToEndpoint
    }

    console.log(data2);

    fetch('/recommend_03/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data2)
    })
    .then(response => response.json())
    .then(data2 => {
        document.getElementById('hotel-name-result').innerHTML = data2.data2;
    });
}


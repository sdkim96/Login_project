const hotelTags = {
    "1-star": { "wifi": 10, "luggageStorage": 9, "amenities": 8, "desk24": 7, "parking": 6, "nonSmokingRooms": 5, "laptopRental": 4, "paidLaundry": 3, "coffeeShop": 2, "business": 1 },
    "2-star": { "wifi": 10, "nonSmokingRooms": 9, "desk24": 8, "luggageStorage": 7, "amenities": 6, "parking": 5, "coffeeShop": 4, "laptopRental": 3, "business": 2, "smokingArea": 1 },
    "3-star": { "wifi": 10, "nonSmokingRooms": 9, "desk24": 8, "business": 7, "amenities": 6, "luggageStorage": 5, "parking": 4, "fitness": 3, "paidLaundry": 2, "breakfast": 1 },
    "4-star": { "wifi": 10, "parking": 9, "fitness": 8, "amenities": 7, "desk24": 6, "nonSmokingRooms": 5, "business": 4, "paidLaundry": 3, "restaurant": 2, "luggageStorage": 1 },
    "5-star": { "parking": 10, "wifi": 9, "fitness": 8, "desk24": 7, "pool": 6, "sauna": 5, "nonSmokingRooms": 4, "business": 3, "amenities": 2, "breakfast": 1 },
};

  
const capitalRequirements = {
    "1-star": 100000000, // 1억원
    "2-star": 300000000,
    "3-star": 500000000,
    "4-star": 900000000,
    "5-star": 1500000000,
};

function getSelectedTags() {
    let selectedTags = [];
    let checkboxes = document.querySelectorAll('input[name="tags"]:checked');

    checkboxes.forEach((checkbox) => {
        selectedTags.push(checkbox.value);
    });

    return selectedTags;
}
  
function calculateHotelGrade() {
    let userCapital = parseInt(document.getElementById('capital').value);
    let userTags = getSelectedTags();

    let possibleGrades = Object.keys(capitalRequirements).filter(grade => userCapital >= capitalRequirements[grade]);

    if (possibleGrades.length === 0) {
        document.getElementById('hotel-grade-result').innerText = `Your capital doesn't meet the requirements of any hotel grade.`;
        return;
    }

    let scores = possibleGrades.reduce((scores, grade) => {
        scores[grade] = userTags.reduce((score, tag) => {
            if (hotelTags[grade][tag]) {
                // 태그가 호텔 성급에 있는 경우, 해당 태그의 점수를 합산
                return score + hotelTags[grade][tag];
            } else {
                // 태그가 호텔 성급에 없는 경우, 점수에 변화 없음
                return score;
            }
        }, 0);
        return scores;
    }, {});

    // 가장 높은 점수를 가진 호텔 성급을 추천
    let recommendedGrade = Object.keys(scores).reduce((a, b) => scores[a] > scores[b] ? a : b);

    document.getElementById('hotel-grade-result').innerText = `Recommended hotel grade: ${recommendedGrade}`;
}


  
  

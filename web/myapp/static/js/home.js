
$(document).ready(function(){
    $('.carousel').carousel({
    interval: 1000
    })
});



// const sections = document.querySelectorAll('.section');

// const options = {
//   root: null,  // 브라우저 viewport를 root로 사용
//   threshold: 0.1,  // 타겟 요소의 10%가 보이면 callback 함수 실행
// };

// const observer = new IntersectionObserver(function(entries, observer) {
//   entries.forEach(entry => {
//     if(!entry.isIntersecting) {
//       return;
//     }
//     const img = entry.target.querySelector('img');
//     img.src = img.dataset.src;  // 실제 이미지 URL을 data-src에서 가져옴
//     observer.unobserve(entry.target);
//   });
// }, options);

// sections.forEach(section => {
//   observer.observe(section);
// });
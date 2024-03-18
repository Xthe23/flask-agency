// mobile-menu.js
document.addEventListener('DOMContentLoaded', function() {
    const menuBtn = document.querySelector('.menu-btn');
    const navLinks = document.querySelector('.nav-links');
    menuBtn.addEventListener('click', function() {
        // console.log('Menu button clicked!');
        navLinks.classList.toggle('is-active');
        // console.log('Toggle is-active class on navigation links.');
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const menuBtn = document.querySelector('.menu-btn');
    const navLinks = document.querySelector('.mobile-nav'); // Updated selector to match your HTML structure
    menuBtn.addEventListener('click', function() {
        navLinks.classList.toggle('hidden'); // Toggle 'hidden' class for Tailwind CSS
    });

    // Initialize navbar state based on initial scroll position as soon as the DOM is fully loaded
    handleScroll();
});

/**
 * Throttles the execution of a function.
 *
 * @param {Function} func - The function to be throttled.
 * @param {number} limit - The time limit (in milliseconds) between function invocations.
 * @returns {Function} - The throttled function.
 */
function throttle(func, limit) {
    let lastFunc;
    let lastRan;
    return function() {
        const context = this;
        const args = arguments;
        if (!lastRan) {
            func.apply(context, args);
            lastRan = Date.now();
        } else {
            clearTimeout(lastFunc);
            lastFunc = setTimeout(function() {
                if ((Date.now() - lastRan) >= limit) {
                    func.apply(context, args);
                    lastRan = Date.now();
                }
            }, limit - (Date.now() - lastRan));
        }
    }
}

var navbar = document.getElementById("navbar");
var lastScrollTop = 0; // Keep track of last scroll position

function handleScroll() {
    var currentScroll = window.scrollY || document.documentElement.scrollTop;
    
    // Logic to show/hide navbar based on scroll direction
    if (currentScroll <= 0) {
        navbar.classList.add("show"); // Always show the navbar when at the top of the page
        navbar.classList.add("sticky");
    } else if (currentScroll < lastScrollTop) {
        navbar.classList.add("show"); // Show the navbar when scrolling up
        navbar.classList.add("sticky");
    } else {
        navbar.classList.remove("sticky");
        navbar.classList.remove("show"); // Hide the navbar when scrolling down
    }
    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
}

// Apply the throttle function to the scroll event
window.addEventListener("scroll", throttle(handleScroll, 300), false);


// Smooth scroll function
function smoothScroll(targetId) {
    const target = document.getElementById(targetId);
    if (target) {
      window.scrollTo({
        top: target.offsetTop,
        behavior: 'smooth' ,// Smooth scroll behavior
        duration: 2000
      });
    }
  }
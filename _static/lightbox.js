document.addEventListener('DOMContentLoaded', function() {
  const body = document.body;

  // Select all img tags within the div with ID 'content'
  document.querySelectorAll('#content img').forEach(item => {
    item.addEventListener('click', event => {
      event.preventDefault();
      const lightbox = document.getElementById('lightbox');
      let lightboxImage = document.querySelector('#lightbox img');
      if (!lightboxImage) {
        lightboxImage = document.createElement('img');
        lightbox.appendChild(lightboxImage);
      }
      lightboxImage.src = item.getAttribute('src');
      lightboxImage.alt = item.getAttribute('alt');
      lightboxImage.src = item.getAttribute('src');
      const viewportHeight = window.innerHeight;
      const maxWidth = window.innerWidth * 0.99;
      const imgHeight = item.naturalHeight;
      const imgWidth = item.naturalWidth;
      const displayedWidth = Math.min(imgWidth, maxWidth);
      const displayedHeight = (displayedWidth / imgWidth) * imgHeight;

      if (displayedHeight <= window.innerHeight) {
          // Center image if it fits within the viewport height
          lightbox.style.alignItems = 'center';
      } else {
          // Align to top if the image is taller than the viewport
          lightbox.style.alignItems = 'flex-start';
      }

      body.style.overflowY = 'hidden';
      lightbox.style.display = 'flex';
    });
  });

  // Close the lightbox when the close button is clicked
  document.querySelector('.close').addEventListener('click', () => {
    document.getElementById('lightbox').style.display = 'none';
    body.style.overflowY = '';
  });

  const clickClose = () => {
    document.querySelector('.lightbox .close').click();
  };

  // Close lightbox when clicking outside the image
  document.getElementById('lightbox').addEventListener('click', function(e) {
    if (event.target === event.currentTarget) {
      clickClose();
    }
  });

  // Close lightbox on "Escape" key press
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && lightbox.style.display === 'flex') {
      clickClose()
    }
  });
});

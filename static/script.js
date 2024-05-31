document.addEventListener('DOMContentLoaded', function () {
    const threeDotsIcons = document.querySelectorAll('.three-dots');

    threeDotsIcons.forEach(icon => {
      icon.addEventListener('click', function () {
        const deleteIcon = this.nextElementSibling;
        if (deleteIcon.style.display === 'none' || deleteIcon.style.display === '') {
          deleteIcon.style.display = 'inline';
        } else {
          deleteIcon.style.display = 'none';
        }
      });
    });
  });
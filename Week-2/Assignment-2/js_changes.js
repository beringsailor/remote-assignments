const h2 = document.querySelector('h2');

h2.addEventListener('click', () => {
  h2.textContent = "Have a Good Time!";
});


const callToAction = document.querySelector('div#button');

callToAction.addEventListener('click', () => {
    const container2 = document.querySelector('div.container-2');

    if ( container2.style.display = 'none' ) {
        container2.style.display = "flex";
    }
});
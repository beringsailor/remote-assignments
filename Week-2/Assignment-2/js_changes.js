const welcomemsg = document.querySelector('.welcome.middle');
welcomemsg.addEventListener('click', () => {
  welcomemsg.textContent = "Have a Good Time!";
});


const btnClick = document.querySelector('#button');
btnClick.addEventListener('click', () => {
    const container2 = document.querySelector('div.container-2');
    container2.style.display = 'flex';
});

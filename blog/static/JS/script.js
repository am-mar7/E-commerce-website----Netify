const cards = document.querySelectorAll(".toggle")
const sidebarEl = document.querySelector('.sidebar')
cards.forEach(card => {
    card.addEventListener('click' , () => {
        cards.forEach(c => {
            c.classList.remove('active');

        });
        card.classList.add('active');
    })
})
function showSideBar(){
    sidebarEl.style.display = 'flex'
}
function closeSideBar(){
    sidebarEl.style.display = 'none'
}
var selectedOption = document.getElementById("selected");
var options = document.querySelectorAll('.dropdown-item');
const colors = ['btn-success', 'btn-warning', 'btn-danger', 'btn-dark']

options.forEach((option, index) => {
    option.addEventListener('click', () => {
        selectedOption.innerText = option.innerText;
        
        colors.forEach((color) => {
            selectedOption.classList.remove(color);
        })

        selectedOption.classList.add(colors[index]);
    })
});

function begin()
{
    url = "http://localhost:8000/solo-mode/battle" + "/" + selectedOption.innerText
    window.location.replace(url);
}
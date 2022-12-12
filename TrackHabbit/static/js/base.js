let buttons = document.querySelectorAll(".records")

for (let button of buttons)
{
    let check = document.querySelector('.check')
    button.addEventListener("click", event =>{
        event.check.textColor = "white"


    })
}
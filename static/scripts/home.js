

/*header_-----------------------------------------------*/


function openlist(){
    document.getElementById("content2").style.left = "0";
    document.getElementById("content2").style.opacity = "1";
}
function closelist(){
    document.getElementById("content2").style.left = "-100%";
    document.getElementById("content2").style.opacity = "0";
}



/*header_-----------------------------------------------*/







/*popup login------------------------------*/

const modals = document.querySelectorAll("[data-modal]");

modals.forEach(function (trigger) {
  trigger.addEventListener("click", function (event) {
    event.preventDefault();
    const modal = document.getElementById(trigger.dataset.modal);
    modal.classList.add("open");
    const exits = modal.querySelectorAll(".modal-exit");
    exits.forEach(function (exit) {
      exit.addEventListener("click", function (event) {
        event.preventDefault();
        modal.classList.remove("open");
      });
    });
  });
});

/*popup login------------------------------*/
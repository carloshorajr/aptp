let modalCallback = null;

function showModal(options){

    document
        .getElementById("modal-title")
        .textContent = options.title;

    document
        .getElementById("modal-message")
        .textContent = options.message;

    modalCallback = options.onConfirm;

    document
        .getElementById("modal-overlay")
        .classList.add("show");

}

function hideModal(){

    document
        .getElementById("modal-overlay")
        .classList.remove("show");

}

window.addEventListener(

    "DOMContentLoaded",

    () => {

        document
            .getElementById("modal-cancel")
            .onclick = hideModal;

        document
            .getElementById("modal-confirm")
            .onclick = async () => {

                hideModal();

                if(modalCallback){

                    await modalCallback();

                }

            };

        document
            .getElementById("modal-overlay")
            .addEventListener(

                "click",

                event => {

                    if(event.target.id === "modal-overlay"){

                        hideModal();

                    }

                }

            );

        document
            .addEventListener(

                "keydown",

                event => {

                    if(event.key === "Escape"){

                        hideModal();

                    }

                }

            );

    }

);
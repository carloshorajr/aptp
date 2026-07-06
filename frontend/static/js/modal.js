let modalCallback = null;

function showModal(options) {

    const title =
        document.getElementById("modal-title");

    const message =
        document.getElementById("modal-message");

    const cancelButton =
        document.getElementById("modal-cancel");

    const confirmButton =
        document.getElementById("modal-confirm");

    title.textContent = options.title;

    message.textContent = options.message;

    modalCallback = options.onConfirm ?? null;

    cancelButton.style.display =
        options.showCancel === false
            ? "none"
            : "";

    confirmButton.textContent =
        options.confirmText ?? "Confirmar";

    document
        .getElementById("modal-overlay")
        .classList.add("show");

}

function hideModal() {

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

                if (modalCallback) {

                    await modalCallback();

                }

            };

        document
            .getElementById("modal-overlay")
            .addEventListener(

                "click",

                event => {

                    if (event.target.id === "modal-overlay") {

                        hideModal();

                    }

                }

            );

        document
            .addEventListener(

                "keydown",

                event => {

                    if (event.key === "Escape") {

                        hideModal();

                    }

                }

            );

    }

);
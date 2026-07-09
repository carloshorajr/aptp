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

    if (options.allowHtml) {

        message.innerHTML = options.message.trim();

        message.className = "modal-message";

        if (options.messageClass){

            message.classList.add(options.messageClass);

        }

    }

    else {

        message.textContent = options.message;

        message.className = "modal-message";

        if (options.messageClass){

            message.classList.add(options.messageClass);

        }

    }

    const modalIcon =
    document.getElementById("modal-icon");

    const modalIconSymbol =
    document.getElementById("modal-icon-symbol");

    modalIcon.className = `modal-icon modal-icon-${options.iconClass ?? "danger"}`;

    modalIconSymbol.className = `fa fa-${options.icon ?? "trash"}`;

    modalCallback = options.onConfirm ?? null;

    cancelButton.style.display =
        options.showCancel === false
            ? "none"
            : "";
    
    cancelButton.textContent =
        options.cancelText ?? "Cancelar";

    cancelButton.className =
        `btn ${options.cancelClass ?? "btn-outline"}`;

    confirmButton.textContent = options.confirmText ?? "Confirmar";

    confirmButton.className = `btn ${options.confirmClass ?? "btn-danger"}`;

    document
        .getElementById("modal-overlay")
        .classList.add("show");

    if (options.onShow) {

        options.onShow();

    }
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
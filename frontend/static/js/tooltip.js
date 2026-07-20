const Tooltip = {

    popup: null,

    init() {

        this.popup =
            document.getElementById("tooltip");

        document.addEventListener(

            "mouseover",

            event => {

                const target =
                    event.target.closest("[data-tooltip]");

                if (!target) {

                    return;

                }

                this.popup.innerHTML =
                    target.dataset.tooltip;

                const rect =
                    target.getBoundingClientRect();

                this.popup.style.left =
                    `${rect.right + 10}px`;

                this.popup.style.top =
                    `${rect.top}px`;

                this.popup.classList.add("show");

            }

        );

        document.addEventListener(

            "mouseout",

            event => {

                if (
                    event.target.closest("[data-tooltip]")
                ) {

                    this.popup.classList.remove("show");

                }

            }

        );

    }

};

window.addEventListener(

    "DOMContentLoaded",

    () => Tooltip.init()

);
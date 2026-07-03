const Events = {

    init() {

        const form = document.querySelector("form");

        if (!form) {
            return;
        }

        form.addEventListener("submit", this.submit);

    },

    async submit(event) {

        event.preventDefault();

        const currentContent = document.getElementById("app-content");

        currentContent.classList.add("is-loading");

        showLoader();

        await new Promise(resolve => setTimeout(resolve, 180));

        const form = event.target;

        const params = new URLSearchParams(
            new FormData(form)
        );

        const response = await fetch(
            `/events?${params.toString()}`
        );

        const html = await response.text();

        const parser = new DOMParser();

        const documentHtml = parser.parseFromString(
            html,
            "text/html"
        );

        const newContent =
            documentHtml.getElementById("app-content");

        if (!newContent) {
            return;
        }

        currentContent.innerHTML =
            newContent.innerHTML;

        PageManager.init("events");

        requestAnimationFrame(() => {

            currentContent.classList.remove("is-loading");

            hideLoader();

        });

    }

};
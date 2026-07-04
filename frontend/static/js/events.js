const Events = {

    init() {

        const form = document.querySelector("form");

        if (!form) {
            return;
        }

        form.addEventListener("submit", this.submit);

    },

    async refreshStatistics() {

        try {

            const response =
                await fetch("/events/data");

            if (!response.ok) {
                throw new Error(
                    `HTTP ${response.status}`
                );
            }

            const data = await response.json();

            document.getElementById("stat-total").textContent =
                data.statistics.total;

            document.getElementById("stat-info").textContent =
                data.statistics.info;

            document.getElementById("stat-warning").textContent =
                data.statistics.warning;

            document.getElementById("stat-error").textContent =
                data.statistics.error;

            document.getElementById("stat-24h").textContent =
                data.statistics.last_24h;

            document.getElementById("stat-today").textContent =
                data.statistics.today;

        } catch (error) {

            console.error(
                "Falha ao atualizar estatísticas.",
                error
            );

        }

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

        await this.refreshStatistics();

        requestAnimationFrame(() => {

            currentContent.classList.remove("is-loading");

            hideLoader();

        });

    }

};
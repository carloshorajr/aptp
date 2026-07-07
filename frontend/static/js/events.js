const Events = {

    interval: null,

    init() {

        const form = document.querySelector("form");

        if (!form) {
            return;
        }

        form.addEventListener(
            "submit",
            event => this.submit(event)
        );

        this.update();

        if (this.interval) {

            clearInterval(this.interval);

        }

        this.interval = setInterval(() => {

            this.update();

        }, 60000);

    },

    async update() {

        try {

            const form = document.querySelector("form");

            if (!form) {
                return;
            }

            const params = new URLSearchParams(
                new FormData(form)
            );

            const response = await fetch(
                `/events/data?${params.toString()}`
            );

            if (!response.ok) {

                throw new Error(`HTTP ${response.status}`);

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

            const tbody = document.getElementById(
                "events-table-body"
            );

            if (!tbody) {
                return;
            }

            let html = "";

            for (const event of data.events) {

                let badge = "";

                switch (event.level) {

                    case "INFO":

                        badge =
                            '<span class="badge badge-info">INFO</span>';

                        break;

                    case "WARNING":

                        badge =
                            '<span class="badge badge-warning">WARNING</span>';

                        break;

                    case "ERROR":

                        badge =
                            '<span class="badge badge-error">ERROR</span>';

                        break;

                }

                html += `
                    <tr>

                        <td>${event.timestamp}</td>

                        <td>${badge}</td>

                        <td>${event.source}</td>

                        <td>${event.message}</td>

                    </tr>
                `;

            }

            tbody.innerHTML = html;

        } catch (error) {

            console.error(
                "Falha ao atualizar Eventos.",
                error
            );

        }

    },

    async submit(event) {

        event.preventDefault();

        const form = event.target;

        const period =
            form.elements.period.value;

        const level =
            form.elements.level.value;

        const source =
            form.elements.source.value;

        const search =
            form.elements.search.value.trim();

        const limit =
            form.elements.limit.value;

        const isDefaultFilters =

            period === "" &&
            level === "" &&
            source === "" &&
            search === "" &&
            limit === "20";

        if (isDefaultFilters) {

            showModal({

                title: "Nada a Aplicar",

                message:
                    "Não há filtros a serem aplicados.",

                icon: "check",

                iconClass: "info",

                confirmClass: "btn-outline",

                confirmText: "Cancelar",

                showCancel: false

            });

            return;

        }

        const params = new URLSearchParams(
            new FormData(form)
        );

        const link = document.querySelector(
            '.menu a[data-route="/events"]'
        );

        await loadPage(

            `/events?${params.toString()}`,

            link

        );

    },

    async clearFilters() {

        const form = document.querySelector("form");

        if (!form) {

            return;

        }

        const period = form.elements.period.value;

        const level = form.elements.level.value;

        const source = form.elements.source.value;

        const search = form.elements.search.value.trim();

        const limit = form.elements.limit.value;

        const isDefaultFilters =

            period === "" &&
            level === "" &&
            source === "" &&
            search === "" &&
            limit === "20";

        if (isDefaultFilters) {

            showModal({

                title: "Nada a Limpar",

                message:
                    "Não há filtros a serem limpos.",

                icon: "refresh",

                iconClass: "info",

                confirmText: "Cancelar",

                confirmClass: "btn-outline",

                showCancel: false

            });

            return;

        }

        const link = document.querySelector(
            '.menu a[data-route="/events"]'
        );

        await loadPage(
            "/events",
            link
        );

    },

    async clear() {

        const tbody = document.getElementById(
            "events-table-body"
        );

        if (!tbody || tbody.rows.length === 0) {

            showModal({

                title: "Nada a Apagar",

                message:
                    "Não há eventos a serem apagados.",

                icon: "trash",

                iconClass: "info",

                confirmText: "Cancelar",

                confirmClass: "btn-outline",

                showCancel: false

            });

            return;

        }

        showModal({

            title: "Apagar Eventos",

            message:
                "Você deseja apagar todo o registro de eventos?\nEsta ação não poderá ser desfeita!",

            icon: "trash",

            iconClass: "danger",

            confirmText: "Apagar",

            confirmClass: "btn-danger",

            onConfirm: async () => {

                await fetch(

                    "/events/clear",

                    {

                        method: "POST"

                    }

                );

                const link = document.querySelector(
                    '.menu a[data-route="/events"]'
                );

                await loadPage(
                    "/events",
                    link
                );

            }

        });

    },

    destroy() {

        if (this.interval) {

            clearInterval(this.interval);

            this.interval = null;

        }

    }

};
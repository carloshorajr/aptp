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

    submit(event) {

        event.preventDefault();

        const form = event.target;

        const params = new URLSearchParams(
            new FormData(form)
        );

        window.location.href =
            `/events?${params.toString()}`;

    },

    destroy() {

        if (this.interval) {

            clearInterval(this.interval);

            this.interval = null;

        }

    }

};
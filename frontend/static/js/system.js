const System = {

    interval: null,

    async update() {

        const response = await fetch("/system/data");

        const data = await response.json();

        document.getElementById("system-cpu").textContent =
            `${data.cpu}%`;

        document.getElementById("system-memory").textContent =
            `${data.memory}%`;

        document.getElementById("system-uptime").textContent =
            data.uptime;

    },

    init() {

        this.update();

        if (this.interval) {

            clearInterval(this.interval);

        }

        this.interval = setInterval(() => {

            this.update();

        }, 60000);

    }

};
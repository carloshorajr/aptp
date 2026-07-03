const System = {

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

    }

};
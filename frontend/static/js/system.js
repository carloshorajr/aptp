const System = {

    lastData: {
        cpu: null,
        memory: null,
        uptime: null
    },

    interval: null,

    async update() {

        try {

            const response = await fetch("/system/data");

            if (!response.ok) {

                throw new Error(
                    `HTTP ${response.status}`
                );

            }

            const data = await response.json();

            if (data.cpu !== this.lastData.cpu) {

                document.getElementById("system-cpu").textContent =
                    `${data.cpu}%`;

                this.lastData.cpu = data.cpu;

            }

            if (data.memory !== this.lastData.memory) {

                document.getElementById("system-memory").textContent =
                    `${data.memory}%`;

                this.lastData.memory = data.memory;

            }

            if (data.uptime !== this.lastData.uptime) {

                document.getElementById("system-uptime").textContent =
                    data.uptime;

                this.lastData.uptime = data.uptime;

            }

        } catch (error) {

            console.error(
                "Falha ao atualizar dados do sistema.",
                error
            );

        }

    },

/*     destroy() {

        if (this.interval) {

            clearInterval(this.interval);

            this.interval = null;

        }

    }, */

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
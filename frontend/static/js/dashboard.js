const Dashboard = {

    chart: null,

    interval: null,

    connectedTime: null,

    connectedSSID: null,

    connectedTimeInterval: null,

    init() {

        const canvas = document.getElementById("wifi-connectivity-chart");

        if (!canvas) {

            return;

        }

        this.chart = new Chart(

            canvas,

            {

                type: "bar",

                data: {

                    labels: [],

                    datasets: [

                        {

                            label: "Associações",

                            data: [],

                            backgroundColor: "#2563eb"

                        },

                        {

                            label: "Desassociações",

                            data: [],

                            backgroundColor: "#dc2626"

                        }

                    ]

                },

                options: {

                    responsive: true,

                    maintainAspectRatio: false,

                    plugins: {

                        legend: {

                            position: "bottom"

                        }

                    },

                    scales: {

                        y: {

                            beginAtZero: true,

                            ticks: {

                                precision: 0

                            }

                        }

                    }

                }

            }

        );

        this.update();

        this.startConnectedTimeCounter();

        this.interval = setInterval(

            () => this.update(),

            60000

        );

    },

    async update() {

        try {

            const response = await fetch(

                "/dashboard/wifi-connectivity"

            );

            if (!response.ok) {

                throw new Error(

                    `HTTP ${response.status}`

                );

            }

            const data = await response.json();

            const chart = data.chart;

            this.connectedSSID = data.connected_time.ssid;

            this.connectedTime = data.connected_time.seconds;

            const indicator = document.getElementById(

                "wifi-status-indicator"

            );

            const statusText = document.getElementById(

                "wifi-status-text"

            );

            if (

                this.connectedTime !== null

            ) {

                indicator.classList.remove(

                    "dashboard-status-disconnected"

                );

                indicator.classList.add(

                    "dashboard-status-connected"

                );

                statusText.textContent =

                    "Conectado";

            }

            else {

                indicator.classList.remove(

                    "dashboard-status-connected"

                );

                indicator.classList.add(

                    "dashboard-status-disconnected"

                );

                statusText.textContent =

                    "Desconectado";

            }

            this.renderConnectedTime();

            this.chart.data.labels =

                chart.map(

                    item => item.day

                );

            this.chart.data.datasets[0].data =

                chart.map(

                    item => item.associations

                );

            this.chart.data.datasets[1].data =

                chart.map(

                    item => item.disassociations

                );

            this.chart.update();

        }

        catch (error) {

            console.error(

                "Failed to update dashboard.",

                error

            );

        }

    },

    renderConnectedTime() {

        const element = document.getElementById(

            "wifi-connected-time"

        );

        const ssid = document.getElementById(

            "wifi-connected-ssid"

        );

        if (!element) {

            return;

        }

        ssid.textContent = this.connectedSSID || "—";

        if (

            this.connectedTime === null

        ) {

            element.textContent =

                "--:--:--";

            return;

        }

        const hours = Math.floor(

            this.connectedTime / 3600

        );

        const minutes = Math.floor(

            (this.connectedTime % 3600) / 60

        );

        const seconds = this.connectedTime % 60;

        element.textContent =

            String(hours).padStart(2, "0")

            + ":"

            + String(minutes).padStart(2, "0")

            + ":"

            + String(seconds).padStart(2, "0");

    },

    startConnectedTimeCounter() {

        this.connectedTimeInterval = setInterval(

            () => {

                if (

                    this.connectedTime !== null

                ) {

                    this.connectedTime++;

                    this.renderConnectedTime();

                }

            },

            1000

        );

    },

    destroy() {

        if (

            this.interval

        ) {

            clearInterval(

                this.interval

            );

            this.interval = null;

        }

        if (

            this.connectedTimeInterval

        ) {

            clearInterval(

                this.connectedTimeInterval

            );

            this.connectedTimeInterval = null;

        }

        if (

            this.chart

        ) {

            this.chart.destroy();

            this.chart = null;

        }

    }

};
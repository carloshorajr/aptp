const Dashboard = {

    chart: null,

    interval: null,

    connectedTime: null,

    connectedSSID: null,

    signalDbm: null,

    connectedTimeInterval: null,

    init() {

        const canvas = document.getElementById("wifi-connectivity-chart");

        if (canvas) {

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

        }

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

            const signalResponse = await fetch(

                "/dashboard/wifi-signal"

            );

            if (!signalResponse.ok) {

                throw new Error(

                    `HTTP ${signalResponse.status}`

                );

            }

            const signal = await signalResponse.json();

            this.signalDbm = signal.signal_dbm;

            const chart = data.chart;

            if (data.connected_time) {

                this.connectedSSID = data.connected_time.ssid;

                this.connectedTime = data.connected_time.seconds;

            }
            else {

                this.connectedSSID = null;

                this.connectedTime = null;

            }

            const indicator = document.getElementById(

                "wifi-status-indicator"

            );

            const statusText = document.getElementById(

                "wifi-status-text"

            );

            if (

                indicator &&

                statusText

            ) {

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
        
        }

            this.renderConnectedTime();

            this.renderSignal();

            if (this.chart) {

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

    renderSignal() {

        const value = document.getElementById(

            "wifi-signal-value"

        );

        const quality = document.getElementById(

            "wifi-signal-quality"

        );

        const bars = document.querySelectorAll(

            "#wifi-signal-icon .signal-bar"

        );

        if (

            !value ||

            !quality ||

            bars.length === 0

        ) {

            return;

        }

        bars.forEach(

            bar => bar.classList.remove("active")

        );

        if (

            this.signalDbm === null

        ) {

            value.textContent = "--";

            quality.textContent = "--";

            return;

        }

        value.textContent =

            `${this.signalDbm} dBm`;

        quality.textContent = "RSSI";

        const level = Math.max(

            1,

            Math.min(

                4,

                Math.round(

                    (this.signalDbm + 100) / 15

                )

            )

        );

        for (

            let i = 0;

            i < level;

            i++

        ) {

            bars[i].classList.add(

                "active"

            );

        }

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
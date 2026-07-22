const Dashboard = {

    chart: null,
    
    signalHistory: [],

    interval: null,

    connectedTime: null,

    connectedSSID: null,

    signalDbm: null,

    latency: null,

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

                                backgroundColor: "#2563eb",

                                barPercentage: 0.55,

                                categoryPercentage: 0.70,

                                borderRadius: 4,

                            },

                            {

                                label: "Desassociações",

                                data: [],

                                backgroundColor: "#dc2626",

                                barPercentage: 0.55,

                                categoryPercentage: 0.70,

                                borderRadius: 4,

                            }

                        ]

                    },

                    options: {

                        responsive: true,

                        maintainAspectRatio: false,

                        plugins: {

                            legend: {

                                position: "bottom",

                                align: "center",

                                labels: {

                                    boxWidth: 42,

                                    padding: 16

                                }

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

        const signalCanvas = document.getElementById(

            "wifi-signal-chart"

        );

        if (signalCanvas) {

            const dangerZonePlugin = {

                id: "dangerZone",

                beforeDraw(chart) {

                    const {

                        ctx,

                        chartArea,

                        scales

                    } = chart;

                    const y = scales.y.getPixelForValue(-71);

                    ctx.save();

                    ctx.fillStyle = "rgba(220,38,38,0.12)";

                    ctx.fillRect(

                        chartArea.left,

                        y,

                        chartArea.right - chartArea.left,

                        chartArea.bottom - y

                    );

                    ctx.restore();

                }

            };

            this.signalChart = new Chart(

                signalCanvas,

                {

                    type: "line",

                    data: {

                        labels: [],

                        datasets: [

                            {

                                data: [],

                                borderColor: "#2563eb",

                                backgroundColor: "rgba(37,99,235,0.15)",

                                fill: true,

                                tension: 0.35,

                                pointRadius: 4,

                                pointHoverRadius: 6

                            }

                        ]

                    },

                    options: {

                        responsive: true,

                        maintainAspectRatio: false,

                        plugins: {

                            legend: {

                                display: false

                            }

                        },

                        scales: {

                            x: {

                                grid: {

                                    display: false

                                }

                            },

                            y: {

                                reverse: true,

                                min: -90,

                                max: -30

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

            this.signalHistory = signal.history || [];

            const latencyResponse = await fetch(

                "/dashboard/wifi-latency"

            );

            if (!latencyResponse.ok) {

                throw new Error(

                    `HTTP ${latencyResponse.status}`

                );

            }

            this.latency = await latencyResponse.json();
                        const chart = data.chart.slice(-30);
                        
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

            const statusIcon = document.getElementById(
            
                "wifi-status-icon"
            
            );

            if (

                indicator &&

                statusText &&

                statusIcon

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

                statusIcon.src =
                    
                    "/static/icons/wifi_connect_green.svg";

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

                statusIcon.src =
                    
                    "/static/icons/wifi_connect_red.svg";

            }
        
        }

            this.renderConnectedTime();

            if (this.signalChart) {

                const history =

                    this.signalHistory.slice(-5);

                this.signalChart.data.labels =

                    history.map(

                        item => item.time

                    );

                this.signalChart.data.datasets[0].data =

                    history.map(

                        item => item.signal_dbm

                    );

                this.signalChart.update();

            }

            this.renderLatency();

            if (this.chart) {

                this.chart.data.labels =

                    chart.map(

                        item => item.day.substring(0, 5)

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

    renderLatency() {

        const rtt = document.getElementById(

            "wifi-latency-rtt"

        );

        const loss = document.getElementById(

            "wifi-latency-loss"

        );

        const gateway = document.getElementById(

            "wifi-latency-gateway"

        );

        if (

            !rtt ||

            !loss ||

            !gateway

        ) {

            return;

        }

        if (

            !this.latency

        ) {

            rtt.textContent = "--";

            loss.textContent = "--";

            gateway.textContent = "--";

            return;

        }

        gateway.textContent =

            this.latency.gateway || "--";

        if (

            this.latency.rtt_avg_ms === null

        ) {

            rtt.textContent = "--";

        }

        else {

            rtt.textContent =

                `${this.latency.rtt_avg_ms} ms`;

        }

        if (

            this.latency.loss_percent === null

        ) {

            loss.textContent = "--";

        }

        else {

            loss.textContent =

                `${this.latency.loss_percent}%`;

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

        if (

            this.signalChart

        ) {

            this.signalChart.destroy();

            this.signalChart = null;

        }

    }

};
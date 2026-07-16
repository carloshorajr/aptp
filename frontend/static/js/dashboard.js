const Dashboard = {

    chart: null,

    interval: null,

    init() {

        const canvas = document.getElementById(

            "wifi-connectivity-chart"

        );

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

                        title: {

                            display: true,

                            text: "Conectividade"

                        },

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

            this.chart.data.labels =

                data.map(

                    item => item.day

                );

            this.chart.data.datasets[0].data =

                data.map(

                    item => item.associations

                );

            this.chart.data.datasets[1].data =

                data.map(

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

            this.chart

        ) {

            this.chart.destroy();

            this.chart = null;

        }

    }

};
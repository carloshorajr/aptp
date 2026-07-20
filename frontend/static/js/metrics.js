const Metrics = {

    DEFAULT_INTERVAL: 30,

    DEFAULT_ENABLED: false,

    metrics: {},

// Inicialização

    init() {

        this.metrics = {

            connectivity: {

                button: document.getElementById(
                    "connectivity-enabled"
                ),

                interval: document.getElementById(
                    "connectivity-interval"
                ),

                initialEnabled:
                    document.getElementById(
                        "connectivity-enabled"
                    ).checked

            },

            signal: {

                button: document.getElementById(
                    "signal-enabled"
                ),

                interval: document.getElementById(
                    "signal-interval"
                ),

                initialEnabled:
                    document.getElementById(
                        "signal-enabled"
                    ).checked

            },

        };

        const saveButton = document.getElementById(
            "save-button"
        );

        const clearButton = document.getElementById(
            "clear-button"
        );

        const globalToggle = document.getElementById(
            "metrics-enabled-all-input"
        );

        if (globalToggle) {

            globalToggle.checked =

                Object.values(this.metrics).every(

                    metric => metric.button.checked

                );

        }

        Object.values(this.metrics).forEach(metric => {

            if (metric.button) {

                metric.button.onchange = () => {};

            }

        });

        if (saveButton) {

            saveButton.onclick = () => this.save();

        }

        if (clearButton) {

            clearButton.onclick = () => this.clear();

        }

        if (globalToggle) {

            globalToggle.onchange = () => {

                Object.values(this.metrics).forEach(metric => {

                    metric.button.checked =
                        globalToggle.checked;

                });

            };

        }

    },

// Construção do Payload

    buildPayload() {

        const payload = {};

        Object.entries(this.metrics).forEach(

            ([name, metric]) => {

                payload[name] = {

                    enabled: metric.button.checked,

                    interval_seconds: Number(
                        metric.interval.value
                    )

                };

            }

        );

        return payload;

    },

// Verificação de Alterações

    isDirty() {

        const payload = this.buildPayload();

        return Object.entries(this.metrics).some(

            ([name, metric]) =>

                payload[name].enabled !==
                    metric.initialEnabled

                ||

                payload[name].interval_seconds !==
                Number(metric.interval.dataset.value)

        );

    },

// Verificação do Estado Padrão

    isDefault() {

        const payload = this.buildPayload();

        return Object.keys(this.metrics).every(

            name =>

                payload[name].enabled ===
                this.DEFAULT_ENABLED

                &&

                payload[name].interval_seconds ===
                this.DEFAULT_INTERVAL

        );

    },

// Salvamento das Configurações

    async save(force = false) {

        if (!force && !this.isDirty()) {

            showModal({

                title: "Nada a Salvar",

                message:
                    "Não há alterações para salvar.",

                icon: "save",

                iconClass: "info",

                confirmText: "Sair",

                confirmClass: "btn-outline",

                showCancel: false

            });

            return;

        }

        await fetch(

            "/metrics/save",

            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify(

                    this.buildPayload()

                )
            }
        );

        const link = document.querySelector(
            '.menu a[data-route="/metrics"]'
        );

        await loadPage(
            "/metrics",
            link
        );

    },

// Restauração dos Valores Padrão

        async clear() {

            if (this.isDefault()) {

                showModal({

                    title: "Nada a Limpar",

                    message:
                        "Todas as métricas já estão no padrão.",

                    icon: "cached",

                    iconClass: "info",

                    confirmText: "Sair",

                    confirmClass: "btn-outline",

                    showCancel: false

                });

                return;

            }

            Object.values(this.metrics).forEach(metric => {

                metric.button.checked = this.DEFAULT_ENABLED;

                metric.interval.value =
                    this.DEFAULT_INTERVAL;

            });

            const globalToggle = document.getElementById(
                "metrics-enabled-all-input"
            );

            if (globalToggle) {

                globalToggle.checked = false;

            }

            await this.save(true);

        },

// Liberação de Recursos

    destroy() {

        Object.values(this.metrics).forEach(metric => {

            if (metric.button) {

                metric.button.onchange = null;

            }

        });

        const saveButton = document.getElementById(
            "save-button"
        );

        if (saveButton) {

            saveButton.onclick = null;

        }

        const clearButton = document.getElementById(
            "clear-button"
        );

        if (clearButton) {

            clearButton.onclick = null;

        }

        this.metrics = {};

    }

};
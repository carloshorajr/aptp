const Metrics = {

    DEFAULT_INTERVAL: 30,

    DEFAULT_ENABLED: false,

    button: null,

    interval: null,

    init() {

        this.button = document.getElementById(
            "connectivity-enabled"
        );

        this.interval = document.getElementById(
            "connectivity-interval"
        );

        const saveButton = document.getElementById(
            "save-button"
        );

        const clearButton = document.getElementById(
            "clear-button"
        );

        if (this.button) {

            this.button.onclick = () => this.toggle();

        }

        if (saveButton) {

            saveButton.onclick = () => this.save();

        }

        if (clearButton) {

            clearButton.onclick = () => this.clear();

        }

    },

    toggle() {

        this.button.classList.toggle(
            "metric-enabled"
        );

        this.button.classList.toggle(
            "metric-disabled"
        );

    },

    buildPayload() {

        return {

            enabled: this.button.classList.contains(
                "metric-enabled"
            ),

            interval_seconds: Number(
                this.interval.value
            )

        };

    },

    isDirty() {

        return (

            this.buildPayload().enabled !==
            (this.button.dataset.enabled === "true")

            ||

            this.buildPayload().interval_seconds !==
            Number(this.interval.dataset.value)

        );

    },

    isDefault() {

        return (

            this.buildPayload().enabled ===
            this.DEFAULT_ENABLED

            &&

            this.buildPayload().interval_seconds ===
            this.DEFAULT_INTERVAL

        );

    },

    async save() {

        if (!this.isDirty()) {

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

        async clear() {

            if (this.isDefault()) {

                showModal({

                    title: "Nada a Limpar",

                    message:
                        "Todas as métricas já estão no padrão.",

                    icon: "refresh",

                    iconClass: "info",

                    confirmText: "Sair",

                    confirmClass: "btn-outline",

                    showCancel: false

                });

                return;

            }

            if (this.DEFAULT_ENABLED) {

                this.button.classList.add(
                    "metric-enabled"
                );

                this.button.classList.remove(
                    "metric-disabled"
                );

            } else {

                this.button.classList.add(
                    "metric-disabled"
                );

                this.button.classList.remove(
                    "metric-enabled"
                );

            }

            this.interval.value =
                this.DEFAULT_INTERVAL;

            await this.save();

        },

    destroy() {

        if (this.button) {

            this.button.onclick = null;

        }

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

        this.button = null;

        this.interval = null;

    }

};
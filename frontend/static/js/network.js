const Network = {

    init() {

    },

    destroy() {

    },

    async scanWifi() {

        this.setScanningState(true);

        try {

            await fetch(

                "/network/scan",

                {

                    method: "POST"

                }

            );

            const link = document.querySelector(

                '.menu a[data-route="/network"]'

            );

            await loadPage(

                "/network",

                link

            );

        }

        finally {

            this.setScanningState(false);

        }

    },

    async clear() {

        const rows =
            document.querySelectorAll(".wifi-item");

        if (rows.length === 0) {

            showModal({

                title: "Nada a Limpar",

                message:
                    "Não há redes para limpar.",

                icon: "refresh",

                iconClass: "info",

                confirmText: "Sair",

                confirmClass: "btn-outline",

                showCancel: false

            });

            return;

        }

        await fetch(

            "/network/clear",

            {

                method: "POST"

            }

        );

        const link = document.querySelector(

            '.menu a[data-route="/network"]'

        );

        await loadPage(

            "/network",

            link

        );

    },

    renderWifiList(networks) {

        const list =
            document.getElementById("wifi-list");
        
        list.innerHTML = "";

        if (networks.length === 0) {

            list.innerHTML = `

            <div class="wifi-empty">

                Clique em "Escanear" para mostrar as redes WiFi disponíveis.

            </div>

            `;

            return;

        }

        for (const [index, network] of networks.entries()) {

            list.insertAdjacentHTML(

                "beforeend",

                `

                <div class="wifi-item">

                    <span class="wifi-ssid">

                        ${network.ssid}

                    </span>

                    <div class="wifi-actions">

                        <button
                            type="button"
                            class="btn btn-outline wifi-icon-btn"
                            title="Detalhes"
                            onclick="Network.showWifiDetails(${index})"
                        >

                            <i class="fa fa-info-circle"></i>

                        </button>

                        <button
                            type="button"
                            class="btn ${network.connected ? "btn-danger" : "btn-primary"} wifi-icon-btn"
                            title="${network.connected ? "Desconectar" : "Conectar"}"
                            onclick="Network.toggleWifi(${index})"
                        >

                            <i class="fa fa-${network.connected ? "chain-broken" : "plug"}"></i>

                        </button>

                    </div>

                </div>

                `

            );

        }

    },

    showWifiDetails(button) {

        const network = {

            ssid:
                button.dataset.ssid,

            security:
                button.dataset.security,

            signal:
                button.dataset.signal,

            connected:
                button.dataset.connected === "true"

        };

        if (!network) {

            return;

        }

        showModal({

            title: network.ssid,

            message:
                "Os detalhes desta rede serão implementados no próximo sprint.",

            icon: "info-circle",

            iconClass: "info",

            confirmText: "Sair",

            confirmClass: "btn-outline",

            showCancel: false

        });

    },

    toggleWifi(button) {

        const network = {

            ssid:
                button.dataset.ssid,

            connected:
                button.dataset.connected === "true"

        };

        showModal({

            title: network.ssid,

            message:
                "A conexão com redes Wi-Fi será implementada no próximo sprint.",

            icon: "wifi",

            iconClass: "info",

            confirmText: "Sair",

            confirmClass: "btn-outline",

            showCancel: false

        });

    },

    destroy() {

    },

    setScanningState(scanning) {

        const button =
            document.getElementById("scan-wifi-button");

        if (!button) {

            return;

        }

        const icon =
            button.querySelector("i");

        const label =
            button.querySelector("span");

        button.classList.toggle(
            "wifi-scanning",
            scanning
        );

        icon.className = scanning
            ? "fa fa-spinner fa-spin"
            : "fa fa-wifi";

        label.style.display = "";

        button.disabled = scanning;

    },

};
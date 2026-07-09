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
                    "Não há redes escaneadas para limpar.",

                icon: "refresh",

                iconClass: "info",

                messageClass: "wifi-modal-message",

                confirmText: "Sair",

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

                Clique em "Escanear" para mostrar as redes WiFi disponíveis para associação.

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

            ssid: button.dataset.ssid,

            frequency: button.dataset.frequency,

            channel: button.dataset.channel,

            signal: button.dataset.signal,

            security: button.dataset.security,

            saved: button.dataset.saved === "true",

            connected: button.dataset.connected === "true"

        };

        if (!network) {

            return;

        }

        showModal({

            title: network.ssid,

            message: `

            <div class="wifi-details">

                <div class="wifi-detail">

                    <span>Frequência</span>

                    <strong>${network.frequency}</strong>

                </div>

                <div class="wifi-detail">

                    <span>Canal</span>

                    <strong>${network.channel}</strong>

                </div>

                <div class="wifi-detail">

                    <span>Sinal</span>

                    <strong>${network.signal}%</strong>

                </div>

                <div class="wifi-detail">

                    <span>Criptografia</span>

                    <strong>${network.security || "-"}</strong>

                </div>

                <div class="wifi-detail">

                    <span>Perfil salvo</span>

                    <strong>${network.saved ? "Sim" : "Não"}</strong>

                </div>

                <div class="wifi-detail">

                    <span>Conectada</span>

                    <strong>${network.connected ? "Sim" : "Não"}</strong>

                </div>

            </div>

            `,

            allowHtml: true,

            icon: "info-circle",

            iconClass: "info",

            messageClass: "wifi-modal-message",

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
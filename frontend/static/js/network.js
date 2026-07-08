const Network = {

    networks: [],

    init() {

    },

    destroy() {

    },

    async scanWifi() {

        const response = await fetch(

            "/settings/wifi/scan",

            {

                method: "POST"

            }

        );

        const networks = await response.json();

        this.renderWifiList(networks);

    },

    renderWifiList(networks) {

        const list =
            document.getElementById("wifi-list");
        
        this.networks = networks;

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

    showWifiDetails(index) {

        const network = this.networks[index];

        if (!network) {

            return;

        }

        showModal({

            title: network.ssid,

            message:
                "Os detalhes desta rede serão implementados no próximo sprint.",

            icon: "info-circle",

            iconClass: "info",

            confirmText: "Entendi",

            confirmClass: "btn-outline",

            showCancel: false

        });

    },

    toggleWifi(index) {

        const network = this.networks[index];

        if (!network) {

            return;

        }

        showModal({

            title: network.ssid,

            message:
                "A conexão com redes Wi-Fi será implementada no próximo sprint.",

            icon: "wifi",

            iconClass: "info",

            confirmText: "Entendi",

            confirmClass: "btn-outline",

            showCancel: false

        });

    },

};
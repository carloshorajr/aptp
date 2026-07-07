const Settings = {

    networks: [],

    init() {

        this.initTextarea();

    },

    initTextarea() {

        const textarea =
            document.getElementById("descricao");

        if (!textarea) {

            return;

        }

        textarea.style.height = "auto";

        textarea.style.height =
            textarea.scrollHeight + "px";

        textarea.addEventListener(

            "input",

            () => {

                textarea.style.height = "auto";

                textarea.style.height =
                    textarea.scrollHeight + "px";

            }

        );

    },

    async save() {

        const cliente =
            document.querySelector('[name="cliente"]').value.trim();

        const local =
            document.querySelector('[name="local"]').value.trim();

        const descricao =
            document.querySelector('[name="descricao"]').value.trim();

        if (
            cliente === "" &&
            local === "" &&
            descricao === ""
        ) {

            showModal({

                title: "Nada a Salvar",

                message:
                    "Não há dados a serem salvos.",

                icon: "save",

                iconClass: "info",

                confirmText: "Cancelar",

                confirmClass: "btn-outline",

                showCancel: false

            });

            return;

        }

        const form =
            document.getElementById("settings-form");

        const formData =
            new FormData(form);

        await fetch(

            "/settings",

            {

                method: "POST",

                body: formData

            }

        );

        const link = document.querySelector(
            '.menu a[data-route="/settings"]'
        );

        await loadPage(

            "/settings",

            link

        );

    },

    async clear() {

        const cliente =
            document.querySelector('[name="cliente"]').value.trim();

        const local =
            document.querySelector('[name="local"]').value.trim();

        const descricao =
            document.querySelector('[name="descricao"]').value.trim();

        if (
            cliente === "" &&
            local === "" &&
            descricao === ""
        ) {

            showModal({

                title: "Nada a Apagar",

                message:
                    "Não há dados a serem apagados.",

                icon: "trash",

                iconClass: "info",

                confirmText: "Cancelar",

                confirmClass: "btn-outline",

                showCancel: false

            });

            return;

        }

        showModal({

            title: "Apagar Informações",

            message:
                "Você deseja apagar todas as informações do cliente?\nEsta ação não poderá ser desfeita!",

            icon: "trash",

            iconClass: "danger",

            confirmText: "Apagar",

            confirmClass: "btn-danger",

            onConfirm: async () => {

                await fetch(

                    "/settings/clear",

                    {

                        method: "POST"

                    }

                );

                const link = document.querySelector(
                    '.menu a[data-route="/settings"]'
                );

                await loadPage(

                    "/settings",

                    link

                );

            }

        });

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

                Nenhuma rede encontrada.

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
                            onclick="Settings.showWifiDetails(${index})"
                        >

                            <i class="fa fa-info-circle"></i>

                        </button>

                        <button
                            type="button"
                            class="btn ${network.connected ? "btn-danger" : "btn-primary"} wifi-icon-btn"
                            title="${network.connected ? "Desconectar" : "Conectar"}"
                            onclick="Settings.toggleWifi(${index})"
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

    destroy() {

    }

};
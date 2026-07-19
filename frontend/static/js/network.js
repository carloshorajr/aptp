const Network = {

    init() {

    },

    destroy() {

    },

// Escaneia as redes Wi-Fi disponíveis e atualiza a listagem.

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

// Limpa a lista de redes atualmente exibida na interface.

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

// Renderiza dinamicamente a lista de redes Wi-Fi (legado).

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

                            data-ssid="${network.ssid}"
                            data-connected="${network.connected}"

                            onclick="Network.toggleWifi(this)"
                        >

                            <i class="fa fa-${network.connected ? "unlink" : "plug"}"></i>

                        </button>

                    </div>

                </div>

                `

            );

        }

    },

// Exibe as informações detalhadas da rede selecionada.

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

// Conecta ou desconecta a rede Wi-Fi selecionada.

    async toggleWifi(button) {

        const network = {

            ssid:
                button.dataset.ssid,

            connected:
                button.dataset.connected === "true"

        };

        if (network.connected) {

            this.setDisconnectingState(

                button,

                true

            );

            try {

                const response = await fetch(

                    "/network/disconnect",

                    {

                        method: "POST"

                    }

                );

                const result = await response.json();

                if (!result.success) {

                    showModal({

                        title: "Erro",

                        message: result.message,

                        icon: "times-circle",

                        iconClass: "danger",

                        confirmText: "Sair",

                        confirmClass: "btn-outline",

                        showCancel: false

                    });

                    return;

                }

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

                this.setDisconnectingState(

                    button,

                    false

                );

            }

            return;

        }

        showModal({

            title: network.ssid,

            allowHtml: true,

            messageClass: "wifi-modal-message",

            message: `

                <div class="wifi-connect">

                    <div class="wifi-password">

                        <input
                            id="wifi-password"
                            type="password"
                            placeholder="Digite a senha">

                        <button
                            id="toggle-password"
                            type="button"
                            class="wifi-password-toggle">

                            <i class="fa fa-eye-slash"></i>

                        </button>

                    </div>

                </div>

            `,

            icon: "wifi",

            iconClass: "info",

            cancelText: "Conectar",
            
            cancelClass: "btn-primary",

            confirmText: "Sair",
            
            confirmClass: "btn-outline",

            showCancel: true,

            onShow: () => {

                const input =
                    document.getElementById("wifi-password");

                const toggle =
                    document.getElementById("toggle-password");

                const connectButton =
                    document.getElementById("modal-cancel");

                connectButton.disabled = true;

                input.addEventListener("input", () => {

                    connectButton.disabled =
                        input.value.trim() === "";

                });

                if (!input || !toggle) {

                    return;

                }

                toggle.onclick = () => {

                    const showing =
                        input.type === "text";

                    input.type =
                        showing
                            ? "password"
                            : "text";

                    toggle.innerHTML =
                        showing
                            ? '<i class="fa fa-eye-slash"></i>'
                            : '<i class="fa fa-eye"></i>';

                };

            },

            onCancel: async () => {

                const connectButton =
                    document.getElementById("modal-cancel");

                const exitButton =
                    document.getElementById("modal-confirm");
                
                const input =
                    document.getElementById("wifi-password");

                const toggle =
                    document.getElementById("toggle-password");
                
                const connectIcon =
                    connectButton.querySelector(".wifi-icon");

                const password =
                    document
                        .getElementById("wifi-password")
                        .value;
                
                connectButton.disabled = true;

                exitButton.disabled = true;

                input.disabled = true;

                toggle.disabled = true;

                connectButton.classList.add(
                    "wifi-scanning"
                );

                if (connectIcon) {

                    connectIcon.src =
                        "/static/icons/progress_activity.svg";

                    connectIcon.classList.add(
                        "wifi-rotating"
                    );

                }

                const response =
                    await fetch(

                        "/network/connect",

                        {

                            method: "POST",

                            headers: {

                                "Content-Type":
                                    "application/json"

                            },

                            body: JSON.stringify({

                                ssid: network.ssid,

                                password

                            })

                        }

                    );

                const result =
                    await response.json();

                connectButton.disabled = false;

                exitButton.disabled = false;

                input.disabled = false;

                toggle.disabled = false;

                connectButton.classList.remove(
                    "wifi-scanning"
                );

                if (connectIcon) {

                    connectIcon.src =
                        "/static/icons/wifi_connect.svg";

                    connectIcon.classList.remove(
                        "wifi-rotating"
                    );

                }

                hideModal();

                showModal({

                    title:
                        result.success
                            ? "Conectado"

                            : "Erro",

                    message:
                        result.message,

                    icon:
                        result.success
                            ? "check-circle"

                            : "times-circle",

                    iconClass:
                        result.success
                            ? "success"

                            : "danger",

                    confirmText:"Sair",

                    confirmClass:"btn-outline",

                    showCancel:false

                });

                if (result.success) {

                    await fetch(

                        "/network/scan",

                        {

                            method:"POST"

                        }

                    );

                    const link =
                        document.querySelector(

                            '.menu a[data-route="/network"]'

                        );

                    await loadPage(

                        "/network",

                        link

                    );

                }

            }

        });

    },

    destroy() {

    },

// Atualiza o estado visual do botão de escaneamento.

    setScanningState(scanning) {

        const button =
            document.getElementById("scan-wifi-button");

        if (!button) {

            return;

        }

        const icon =
            button.querySelector(".wifi-icon");

        const label =
            button.querySelector("span");

        button.classList.toggle(

            "wifi-scanning",

            scanning

        );

        if (icon) {

            icon.src = scanning

                ? "/static/icons/progress_activity.svg"

                : "/static/icons/wifi_find.svg";

            icon.classList.toggle(

                "wifi-rotating",

                scanning

            );

        }

        label.style.display = "";

        button.disabled = scanning;

    },

// Atualiza o estado visual do botão de desconexão.

    setDisconnectingState(button, disconnecting) {

        if (!button) {

            return;

        }

        const icon =
            button.querySelector(".wifi-icon");

        button.disabled =
            disconnecting;

        if (disconnecting) {

            button.classList.add("wifi-scanning");

        } else {

            button.classList.remove("wifi-scanning");

        }

        if (icon) {

            icon.src = disconnecting

                ? "/static/icons/progress_activity.svg"

                : "/static/icons/wifi_disconnect.svg";

            icon.classList.toggle(

                "wifi-rotating",

                disconnecting

            );

        }

    },

};
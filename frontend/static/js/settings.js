const Settings = {

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
                    "Não há dados a serem salvos no formulário.",

                icon: "save",

                iconClass: "info",

                confirmText: "Entendi",

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
                    "O formulário já está vazio.",

                icon: "trash",

                iconClass: "info",

                confirmText: "Entendi",

                confirmClass: "btn-outline",

                showCancel: false

            });

            return;

        }

        showModal({

            title: "Apagar Configurações",

            message:
                "Deseja realmente apagar todas as informações do cliente?",

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

    destroy() {

    }

};
async function loadPage(url) {

    console.log("Solicitando:", url);

    const response = await fetch(url);

    if (!response.ok) {

        console.error("Erro HTTP:", response.status);

        return;

    }

    const html = await response.text();

    const parser = new DOMParser();

    const documentHtml = parser.parseFromString(
        html,
        "text/html"
    );

    const newContent = documentHtml.getElementById("app-content");

    if (!newContent) {

        console.error("app-content não encontrado.");

        return;

    }

    const currentContent = document.getElementById("app-content");

    currentContent.innerHTML = newContent.innerHTML;

}

function updateActiveMenu(url) {

    document
        .querySelectorAll(".menu a")
        .forEach(link => {

            link.classList.remove("active");

            if (link.dataset.route === url) {

                link.classList.add("active");

            }

        });

}

async function navigate(url) {

    updateActiveMenu(url);

    await loadPage(url);

}

function start() {

    console.log("APTP iniciado");

    document
        .querySelectorAll(".menu a")
        .forEach(link => {

            link.addEventListener("click", async event => {

                event.preventDefault();

                await navigate(link.dataset.route);

            });

        });

}

start();
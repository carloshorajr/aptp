async function loadPage(route, link) {

    document
        .querySelectorAll(".menu a")
        .forEach(item => item.classList.remove("active"));

    link.classList.add("active");

    const response = await fetch(route);

    const html = await response.text();

    const parser = new DOMParser();

    const documentHtml = parser.parseFromString(html, "text/html");

    const newContent = documentHtml.getElementById("app-content");

    if (!newContent) {
        return;
    }

    document.getElementById("app-content").innerHTML =
        newContent.innerHTML;
}

async function start() {

    document.querySelectorAll(".menu a").forEach(link => {

        link.addEventListener("click", async event => {

            event.preventDefault();

            await loadPage(link.dataset.route, link);

        });

    });

}

start();
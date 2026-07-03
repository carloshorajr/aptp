async function loadPage(route, link) {

    document
        .querySelectorAll(".menu a")
        .forEach(item => item.classList.remove("active"));

    link.classList.add("active");

    const currentContent = document.getElementById("app-content");

    currentContent.classList.add("is-loading");

    await new Promise(resolve => setTimeout(resolve, 180));

    const response = await fetch(route);

    const html = await response.text();

    const parser = new DOMParser();

    const documentHtml = parser.parseFromString(html, "text/html");

    const newContent = documentHtml.getElementById("app-content");

    if (!newContent) {
        return;
    }

    currentContent.innerHTML = newContent.innerHTML;

    requestAnimationFrame(() => {

        currentContent.classList.remove("is-loading");

    });
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
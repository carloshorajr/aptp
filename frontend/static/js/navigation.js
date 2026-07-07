async function loadPage(route, link, callback = null) {

    document
        .querySelectorAll(".menu a")
        .forEach(item => item.classList.remove("active"));

    link.classList.add("active");

    const currentContent = document.getElementById("app-content");

    currentContent.classList.add("is-loading");

    showLoader();

    await new Promise(resolve => setTimeout(resolve, 180));

    const response = await fetch(route);

    const html = await response.text();

    const parser = new DOMParser();

    const documentHtml = parser.parseFromString(
        html,
        "text/html"
    );

    const newContent = documentHtml.getElementById("app-content");

    if (!newContent) {
        return;
    }

    currentContent.innerHTML = newContent.innerHTML;

    history.pushState({}, "", route);

    const page = route === "/"

        ? "dashboard"

        : route
            .split("?")[0]
            .substring(1);

    PageManager.init(page);

    requestAnimationFrame(() => {

        currentContent.classList.remove("is-loading");

        hideLoader();

        if (typeof callback === "function") {

            callback();

        }

    });

}

function initializeNavigation() {

    document
        .querySelectorAll(".menu a")
        .forEach(link => {

            link.addEventListener("click", async event => {

                event.preventDefault();

                await loadPage(
                    link.dataset.route,
                    link
                );

            });

        });

}
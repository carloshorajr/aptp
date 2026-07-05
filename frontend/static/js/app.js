function start() {

    initializeNavigation();

    const page =
        window.location.pathname === "/"
            ? "dashboard"
            : window.location.pathname.substring(1);

    PageManager.init(page);

}

start();
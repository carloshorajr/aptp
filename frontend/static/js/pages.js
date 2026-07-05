const PageManager = {

    currentPage: null,

    pages: {

        dashboard: Dashboard,

        system: System,

        events: Events

    },

    init(page) {

        const currentModule =
            this.pages[this.currentPage];

        if (
            currentModule &&
            typeof currentModule.destroy === "function"
        ) {

            currentModule.destroy();

        }

        const nextModule =
            this.pages[page];

        if (
            nextModule &&
            typeof nextModule.init === "function"
        ) {

            nextModule.init();

        }

        this.currentPage = page;

    }

};
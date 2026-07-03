const PageManager = {

    init(page) {

        switch (page) {

            case "dashboard":

                Dashboard.init();

                break;

            case "system":

                System.init();

                break;

            default:

                break;

        }

    }

};
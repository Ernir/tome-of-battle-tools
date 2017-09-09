/*
 * Vue.js based filter for maneuvers. Based on:
 * https://jsfiddle.net/chrisvfritz/aomd3y9n/
 */

let app = new Vue({
    // -------------
    // APP CONTAINER
    // -------------
    el: '#app',

    // --------
    // RAW DATA
    // --------

    data: {
        tableColumns: [
            {
                title: 'Maneuver name',
                field: 'name'
            }, {
                title: 'Level',
                field: 'level'
            }, {
                title: 'Discipline',
                field: 'discipline'
            }, {
                title: "Requirements",
                field: "requirements"
            }, {
                title: "Type",
                field: "type"
            }
        ],

        maneuvers: [],


        maneuverName: '',
        requirements: [],
        levels: [],
        disciplines: [],
        types: [],

        fetchError: false
    },

    // ------------
    // DERIVED DATA
    // ------------
    computed: {
        filteredManeuvers: function () {
            const vm = this;
            return vm.maneuvers.filter(function (maneuver) {
                const regex = new RegExp(vm.maneuverName, 'i');
                return regex.test(maneuver.name)
                    && (vm.requirements.length === 0 || vm.requirements.includes(maneuver.requirements.toString()))
                    && (vm.levels.length === 0 || vm.levels.includes(maneuver.level.toString()))
                    && (vm.disciplines.length === 0 || vm.disciplines.includes(maneuver.discipline))
                    && (vm.types.length === 0 || vm.types.includes(maneuver.type));
            });
        }
        ,
        statusMessage: function () {
            if (this.fetchError) {
                return "There was a problem fetching the maneuvers. Please try again later.";
            }
            if (this.maneuvers.length) {
                if (!this.filteredManeuvers.length) {
                    return "No matching maneuvers were found.";
                }
            } else {
                return 'Loading...'
            }
        }
    },

    // ---------------
    // LIFECYCLE HOOKS
    // ---------------
    created: function () {

        // Extract URL params if they exist.
        // Known to not work on Edge. ¯\_(ツ)_/¯
        let searchParams = new URLSearchParams(window.location.search);
        const name = searchParams.get("n");
        if (name) {
            this.maneuverName = name;
        }
        const levels = searchParams.getAll("l");
        if (levels) {
            this.levels = levels;
        }
        const requirements = searchParams.getAll("r");
        if (requirements) {
            this.requirements = requirements;
        }
        const disciplines = searchParams.getAll("d");
        if (disciplines) {
            this.disciplines = disciplines;
        }
        const types = searchParams.getAll("t");
        if (types) {
            this.types = types;
        }

        this.fetchManeuvers()
    },

    updated: function () {
        let searchParams = new URLSearchParams();

        if (this.maneuverName) {
            searchParams.set("n", this.maneuverName);
        } else {
            searchParams.delete("n");
        }

        if (this.levels) {
            for (let level of this.levels) {
                searchParams.append("l", level);
            }
        } else {
            searchParams.delete("l");
        }

        if (this.requirements) {
            for (let req of this.requirements) {
                searchParams.append("r", req);
            }
        } else {
            searchParams.delete("r");
        }

        if (this.disciplines) {
            for (let dis of this.disciplines) {
                searchParams.append("d", dis);
            }
        } else {
            searchParams.delete("d");
        }

        if (this.types) {
            for (let t of this.types) {
                searchParams.append("t", t);
            }
        } else {
            searchParams.delete("t");
        }

        history.replaceState(
            null, null, searchParams.toString() ? "?" + searchParams.toString() : window.location.pathname
        )
    },

    // --------------
    // SCOPED METHODS
    // --------------
    methods: {
        fetchManeuvers: function () {
            let vm = this;
            vm.maneuvers = [];
            vm.fetchError = false;
            fetch('/api/get-all-maneuvers/')
                .then(function (response) {
                    return response.json()
                })
                .then(function (maneuvers) {
                    vm.maneuvers = maneuvers
                })
                .catch(function () {
                    vm.fetchError = true
                })
        }
    }
});

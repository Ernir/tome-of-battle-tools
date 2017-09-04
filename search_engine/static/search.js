/*
 * Vue.js based filter for maneuvers. Based on:
 * https://jsfiddle.net/chrisvfritz/aomd3y9n/
 */

var app = new Vue({
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
            var vm = this;
            return vm.maneuvers.filter(function (maneuver) {
                var regex = new RegExp(vm.maneuverName, 'i');
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
        this.fetchManeuvers()
    },

    // --------------
    // SCOPED METHODS
    // --------------
    methods: {
        fetchManeuvers: function () {
            var vm = this;
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

/*
 * Vue.js based filter for maneuvers. Based on:
 * https://jsfiddle.net/chrisvfritz/aomd3y9n/
 */

new Vue({
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
        filterQuery: '',
        fetchError: false
    },

    // ------------
    // DERIVED DATA
    // ------------
    computed: {
        filteredManeuvers: function () {
            var vm = this;
            return vm.maneuvers.filter(function (user) {
                var regex = new RegExp(vm.filterQuery, 'i');
                return regex.test(user.name);
            });
        },
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
        },
        getField: function (object, field) {
            return object[field];
        }
    }
});

/*
 Generates three more or less hard-coded http://www.chartjs.org/ charts.
 */

function initializeCharts() {

    Chart.defaults.global.animation = false;

    $.get("/api/statistics/errata/", function (data) {
        makeErrataChart(data);
    });
    $.get("/api/statistics/types/", function(data) {
        makeTypeChart(data);
    });
    $.get("/api/statistics/disciplines/", function(data) {
        makeDisciplineChart(data);
    })
}

function makeErrataChart(rawData) {
    var ctx = $("#errata-chart").get(0).getContext("2d");
    var baseColors = ["#F04124","#5AD3D1"];
    var lightenedColors = ["#FF5B3E","#74EDEB"];

    // Only two items, creating them manually.
    var chartData = [
        {
            value: rawData["errata_num"],
            color: baseColors[0],
            highlight: lightenedColors[0],
            label: "Modified"
        },
        {
            value: rawData["errata_free_num"],
            color: baseColors[1],
            highlight: lightenedColors[1],
            label: "Not modified"
        }
    ];

    new Chart(ctx).Pie(chartData, {
        showScale: true,
        animateScale: true
    });
}

function makeTypeChart(rawData) {
    var ctx = $("#type-number-chart").get(0).getContext("2d");
    var baseColors =      ["#F04124", "#EBDB32", "#74E740", "#4EE291", "#5AD3D1"];
    var lightenedColors = ["#FF5B3E", "#FFF54C", "#8EFF5A", "#68FCAB", "#74EDEB"];

    var chartData = [];

    // Extracting the relevant JSON data.
    var types = Object.keys(rawData);
    for (var i = 0; i < types.length; i++) {
        var label = capitalizeFirstLetter(types[i]) + "s";
        var currentObject = {
            value: rawData[types[i]]["num"],
            color: baseColors[i],
            highlight: lightenedColors[i],
            label: label
        };
        chartData.push(currentObject);
    }

    new Chart(ctx).Pie(chartData, {
        showScale: true,
        animateScale: true
    });
}

// Stolen from: http://stackoverflow.com/a/1026087/1675015
function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function makeDisciplineChart(rawData) {
    var ctx = $("#discipline-size-chart").get(0).getContext("2d");
    var baseColors =      ["#F04124", "#ED922B", "#EBDB32", "#BE4939", "#74E740", "#47E452", "#4EE291", "#53E0CA", "#5AD3D1"];
    var lightenedColors = ["#FF5B3E", "#FFAC45", "#FFF54C", "#D86353", "#8EFF5A", "#61FE6C", "#68FCAB", "#6DFAE4", "#74EDEB"];

    var chartData = [];

    // Parsing the JSON
    for (var i = 0; i < rawData.length; i++) {
        var currentObject = {
            value: rawData[i]["count"],
            color: baseColors[i],
            highlight: lightenedColors[i],
            label: rawData[i]["name"]
        };
        chartData.push(currentObject);
    }
    console.log(chartData);

    new Chart(ctx).Pie(chartData, {
        showScale: true,
        animateScale: true
    });
}

$(initializeCharts());
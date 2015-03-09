/*
 Generates three more or less hard-coded http://www.chartjs.org/ charts.
 */

function initializeCharts() {

    Chart.defaults.global.animation = false;

    // AJAX calls. Each chart is created on the callback.
    $.get("/api/statistics/errata/", function (data) {
        makeErrataChart(data);
    });
    $.get("/api/statistics/types/", function (data) {
        makeTypeChart(data);
    });
    $.get("/api/statistics/disciplines/", function (data) {
        makeDisciplineChart(data);
    })
}

function makeErrataChart(rawData) {
    var ctx = $("#errata-chart").get(0).getContext("2d");
    var baseColors = ["#F04124", "#5AD3D1"];
    var lightenedColors = ["#FF5B3E", "#74EDEB"];

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
    var baseColors = ["#F04124", "#EBDB32", "#74E740", "#4EE291", "#5AD3D1"];
    var lightenedColors = ["#FF5B3E", "#FFF54C", "#8EFF5A", "#68FCAB", "#74EDEB"];

    var chartData = [];

    // Extracting the relevant JSON data.
    var types = Object.keys(rawData);
    for (var i = 0; i < types.length; i++) {
        // Creating capitalized labels from the raw titles, see below
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
    var baseColors = ["#F04124", "#ED922B", "#EBDB32", "#BE4939", "#74E740", "#47E452", "#4EE291", "#53E0CA", "#5AD3D1"];
    var lightenedColors = ["#FF5B3E", "#FFAC45", "#FFF54C", "#D86353", "#8EFF5A", "#61FE6C", "#68FCAB", "#6DFAE4", "#74EDEB"];

    var chartLabels = [];
    var chartValues = [];

    // Parsing the JSON
    for (var i = 0; i < rawData.length; i++) {
        chartValues.push(rawData[i]["count"]);
        chartLabels.push(rawData[i]["name"]);
    }

    var chartData = {
        labels: chartLabels,
        datasets: [
            {
                fillColor: baseColors[0], // Default color
                strokeColor: "#ffffff", // Surrounded by white
                highlightFill: lightenedColors[0],
                highlightStroke: "#ffffff",
                data: chartValues
            }
        ]
    };

    var bar = new Chart(ctx).Bar(chartData, {
        showScale: true
    });

    // Setting the colors
    var n = bar.datasets[0].bars.length;
    for (var j = 0; j < n; j++) {
        var currentBar = bar.datasets[0].bars[j];
        currentBar.fillColor = baseColors[j];
        currentBar.highlightFill = lightenedColors[j];
    }
    bar.update();
}

$(initializeCharts());
$(document).ready(function () {
    function build_chart(chart_data) {
        var chart = AmCharts.makeChart("chartdiv", {
            "type": "serial",
            "theme": "light",
            "columnWidth": 1,
            "dataProvider": chart_data,
            "graphs": [{
                "fillColors": "#c55",
                "fillAlphas": 0.9,
                "lineColor": "#fff",
                "lineAlpha": 0.7,
                "type": "column",
                "valueField": "value"
            }],
            "categoryField": "country__title",
            "categoryAxis": {
                "startOnAxis": true,
                "title": "Страны"
            },
            "valueAxes": [{
                "title": "Значения"
            }]
        });
    }

    var json_data = $("#select_group option:selected").data("val");
    build_chart(json_data);

    $("#select_group").on("change", function () {
        var json_data = $("#select_group option:selected").data("val");
        build_chart(json_data);
    });
});
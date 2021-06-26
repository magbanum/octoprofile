$(document).ready(function () {

    var endpoint1 = '/api/top-languages/'
    var endpoint2 = '/api/most-starred/'
    var endpoint3 = '/api/stars-per-languages/'
    var labels = []
    var defaultData = []

    // For Top languages chart
    $.ajax({
        method: "GET",
        url: endpoint1,
        success: function (data) {
            labels = data.labels
            defaultData = data.values
            backgroundColors = data.colors
            var ctx1 = document.getElementById('myChart1').getContext('2d');
            var myChart = new Chart(ctx1, {
                type: 'pie',
                data: {
                    labels: labels,
                    datasets: [{
                        label: '# of Votes',
                        data: defaultData,
                        backgroundColor: backgroundColors,
                        borderWidth: 1

                    }]
                },
                options: {
                    scales: {
                        y: {
                            display: false
                        },
                        x: {
                            display: false
                        }
                    },
                    responsive: true
                }
            });
        },
        error: function (error_data) {
            console.log("error")
        }
    })

    // For Most starred Chart
    $.ajax({
        method: "GET",
        url: endpoint2,
        success: function (data) {
            labels = data.labels
            defaultData = data.values
            var ctx2 = document.getElementById('myChart2').getContext('2d');

            var myChart = new Chart(ctx2, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Most starred repository',
                        data: defaultData,
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.8)',
                            'rgba(54, 162, 235, 0.8)',
                            'rgba(255, 206, 86, 0.8)',
                            'rgba(75, 192, 192, 0.8)',
                            'rgba(153, 102, 255, 0.8)',

                        ],
                        borderColor: [
                            'rgba(255, 99, 132, 1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)',

                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true,
                        },
                        x: {
                            ticks: {
                                display: false
                            },
                        }
                    },
                    responsive: true


                }
            });
        },
        error: function (error_data) {
            console.log("error")
        }
    })

    // For stars per language chart
    $.ajax({
        method: "GET",
        url: endpoint3,
        success: function (data) {
            labels = data.labels
            defaultData = data.values
            backgroundColors = data.colors
            var ctx3 = document.getElementById('myChart3').getContext('2d');
            var myChart = new Chart(ctx3, {
                type: 'doughnut',
                data: {
                    labels: labels,
                    datasets: [{
                        label: '# of Votes',
                        data: defaultData,
                        backgroundColor: backgroundColors,
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            display: false
                        },
                        x: {
                            display: false
                        }
                    },
                    responsive: true
                }
            });
        },
        error: function (error_data) {
            console.log("error")
        }
    })

    // For sort button
    var options = {
        valueNames: [ 'stars', 'forks' , 'repo-size' ]
      };
      
    var userList = new List('top-repos', options);

    var monkeyList = new List('top-repos', {
        valueNames: ['stars', 'forks', 'repo-size'],
        page: 8,
        pagination: true
    });

    $(".sort").click(function() {
        var attr = $(this).attr("id");

        $(".sort").removeClass("active");
        $(this).addClass("active");
    });
})
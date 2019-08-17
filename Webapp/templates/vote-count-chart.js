(function($) {
  'use strict';
  $(function() {
      Chart.defaults.global.legend.labels.usePointStyle = true;

      if ($("#visit-sale-chart").length) {
          Chart.defaults.global.legend.labels.usePointStyle = true;
          var ctx = document.getElementById('visit-sale-chart').getContext("2d");

          var gradientStrokeViolet = ctx.createLinearGradient(0, 0, 0, 181);
          gradientStrokeViolet.addColorStop(0, 'rgba(218, 140, 255, 1)');
          gradientStrokeViolet.addColorStop(1, 'rgba(154, 85, 255, 1)');
          var gradientLegendViolet = 'linear-gradient(to right, rgba(218, 140, 255, 1), rgba(154, 85, 255, 1))';

          var gradientStrokeBlue = ctx.createLinearGradient(0, 0, 0, 360);
          gradientStrokeBlue.addColorStop(0, 'rgba(54, 215, 232, 1)');
          gradientStrokeBlue.addColorStop(1, 'rgba(177, 148, 250, 1)');
          var gradientLegendBlue = 'linear-gradient(to right, rgba(54, 215, 232, 1), rgba(177, 148, 250, 1))';

          var gradientStrokeRed = ctx.createLinearGradient(0, 0, 0, 300);
          gradientStrokeRed.addColorStop(0, 'rgba(255, 191, 150, 1)');
          gradientStrokeRed.addColorStop(1, 'rgba(254, 112, 150, 1)');
          var gradientLegendRed = 'linear-gradient(to right, rgba(255, 191, 150, 1), rgba(254, 112, 150, 1))';

          var myChart = new Chart(ctx, {
              type: 'bar',
              data: {
                  labels: ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG'],
                  datasets: [
                      {
                          label: "CHN",
                          borderColor: gradientStrokeViolet,
                          backgroundColor: gradientStrokeViolet,
                          hoverBackgroundColor: gradientStrokeViolet,
                          legendColor: gradientLegendViolet,
                          pointRadius: 0,
                          fill: false,
                          borderWidth: 1,
                          fill: 'origin',
                          data: [20, 40, 15, 35, 25, 50, 30, 20]
                      },
                      {
                          label: "USA",
                          borderColor: gradientStrokeRed,
                          backgroundColor: gradientStrokeRed,
                          hoverBackgroundColor: gradientStrokeRed,
                          legendColor: gradientLegendRed,
                          pointRadius: 0,
                          fill: false,
                          borderWidth: 1,
                          fill: 'origin',
                          data: [40, 30, 20, 10, 50, 15, 35, 40]
                      },
                      {
                          label: "UK",
                          borderColor: gradientStrokeBlue,
                          backgroundColor: gradientStrokeBlue,
                          hoverBackgroundColor: gradientStrokeBlue,
                          legendColor: gradientLegendBlue,
                          pointRadius: 0,
                          fill: false,
                          borderWidth: 1,
                          fill: 'origin',
                          data: [70, 10, 30, 40, 25, 50, 15, 30]
                      }
                  ]
              },
              options: {
                  responsive: true,
                  legend: false,
                  legendCallback: function (chart) {
                      var text = [];
                      text.push('<ul>');
                      for (var i = 0; i < chart.data.datasets.length; i++) {
                          text.push('<li><span class="legend-dots" style="background:' +
                              chart.data.datasets[i].legendColor +
                              '"></span>');
                          if (chart.data.datasets[i].label) {
                              text.push(chart.data.datasets[i].label);
                          }
                          text.push('</li>');
                      }
                      text.push('</ul>');
                      return text.join('');
                  },
                  scales: {
                      yAxes: [{
                          ticks: {
                              display: false,
                              min: 0,
                              stepSize: 20,
                              max: 80
                          },
                          gridLines: {
                              drawBorder: false,
                              color: 'rgba(235,237,242,1)',
                              zeroLineColor: 'rgba(235,237,242,1)'
                          }
                      }],
                      xAxes: [{
                          gridLines: {
                              display: false,
                              drawBorder: false,
                              color: 'rgba(0,0,0,1)',
                              zeroLineColor: 'rgba(235,237,242,1)'
                          },
                          ticks: {
                              padding: 20,
                              fontColor: "#9c9fa6",
                              autoSkip: true,
                          },
                          categoryPercentage: 0.5,
                          barPercentage: 0.5
                      }]
                  }
              },
              elements: {
                  point: {
                      radius: 0
                  }
              }
          })
          $("#visit-sale-chart-legend").html(myChart.generateLegend());

      }
  }
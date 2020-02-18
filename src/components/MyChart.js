import React, { Component } from 'react'
import {Chart} from 'chart.js';

export class MyChart extends Component {
    componentDidMount(){
        var ctx = document.getElementById('myChart').getContext('2d');
        new Chart(ctx, {
            type: 'radar',
            data: {
                labels: ['Sports','Technology','Politics','Cooking','Pets'],
                datasets: [{
                    // label: 'trending rate',
                    data: [12, 19, 13, 9, 11],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                title: {
                    display: true,
                    text: 'Trending Rate',
                    fontSize: '25'
                },
                legend: {
                    display: false,
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
    }
    render() {
        return (
            <div className="myChartContainer" >
            <canvas id="myChart"></canvas>
          </div>
        )
    }
}

export default MyChart

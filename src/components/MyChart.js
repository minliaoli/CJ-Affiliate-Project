import React, { Component } from 'react'
import {Chart} from 'chart.js';
import axios from 'axios';

export class MyChart extends Component {
    constructor(props){
        super();
        this.state={
            done:false,
            dataList: [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
        }
        this.getTrend  = this.getTrend.bind(this); 
    }
    getTrend(){
        var link=`http://localhost:5000/trendrate`;
        console.log(`opening ${link}`)
        axios.get(link)
        .then(response => 
                {
                    this.setState( {dataList : [5*response.data["Home"], 5*response.data["Business"], 5*response.data["Computers"],
                    5*response.data["Fashion"], 5* response.data["Games"], 5*response.data["Health"], 5*response.data["Recreation"],
                    5*response.data["Society"], 5*response.data["Sports"], 5*response.data["Technology"] ] })
                    this.setState({done:true})
                }
            )
        .catch(err => console.log(err));
    }
    componentDidUpdate(){
        var ctx = document.getElementById('myChart').getContext('2d');
        if(this.state.done===true){
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ["Business","Computers","Fashion","Games","Health","Home","Recreation","Society", "Sports","Technology"],
                    datasets: [{
                        // label: 'trending rate',
                        data: this.state.dataList,
                        backgroundColor: [
                            'rgba(255, 0, 0, 0.5)',
                            'rgba(255, 0, 0, 0.5)',
                            'rgba(255, 0, 0, 0.5)',
                            'rgba(255, 0, 0, 0.5)',
                            'rgba(255, 0, 0, 0.5)',
                            'rgba(255, 0, 0, 0.5)',
                            'rgba(255, 0, 0, 0.5)',
                            'rgba(255, 0, 0, 0.5)',
                            'rgba(255, 0, 0, 0.5)',
                            'rgba(255, 0, 0, 0.5)'
                        ],
                        barThickness: 20,
                    }]
                },
                options: {
                    title: {
                        display: true,
                        text: 'Trending Rate',
                        fontSize: '25'
                    },
                    // layout: {
                    //     padding: {
                    //         left: 200,
                    //         right: 0,
                    //         top: 0,
                    //         bottom: 0
                    //     }
                    // },
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
        return true;
    }
    componentDidMount(){this.getTrend();}
    render() {
        return (
            <div className="myChartContainer" >
                <canvas id="myChart"></canvas>
            </div>
        )
    }
}

export default MyChart

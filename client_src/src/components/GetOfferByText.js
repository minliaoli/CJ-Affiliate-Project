import React, { Component } from 'react';
import axios from 'axios';
import {Link} from 'react-router-dom';
import {Chart} from 'chart.js';

class GetOfferByText extends Component {
    constructor(props){
        super();
        this.state={
            details:[]
        }
    }
    componentDidMount(){
        this.getOffers();
    }
    myFunction(idN) {
        let me=document.getElementById(idN)
        console.log(me)
        // let copyText = this.textArea;
        me.select();
        me.setSelectionRange(0, 99999); 
        document.execCommand("copy");
        alert(`AD Link Copied!`);
      }
    getOffers(){
// get chart part
    var ctx = document.getElementById('myChart').getContext('2d');
    new Chart(ctx, {
        type: 'horizontalBar',
        data: {
            labels: ['Sports','Technology','Politics','Cooking','Pets'],
            datasets: [{
                label: 'trending rate',
                data: [12, 19, 3, 5, 3, 3],
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
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });




      ///get offer part
        let theText=this.props.match.params.blogtext;

        //var link=`http://localhost:5000/alg/${theText}`;
        var link=`http://localhost:3000/api/CJOffers?filter={"where":{"or":[{"id":"5e386a4199a3e94b4c3657cf"},{"id":"5e386a4199a3e94b4c3657e3"},{"id":"5e386a4199a3e94b4c366451"},{"id":"5e386a4199a3e94b4c366d3e"},{"id":"5e386a4199a3e94b4c3676e3"}]}}`;

        console.log(`opening ${link}`)
       
        axios.get(link)
        .then(response => 
                {
                    let TheArray=[];
                    for (var i=0;i<response.data.length;i++)
                        {TheArray.push(response.data[i]); }
                    this.setState({details : TheArray })
                }
            )
        .catch(err => console.log(err));
    }
    render() {
        var maxStyle = {
            maxHeight : 200
          };
        const MyOffers = this.state.details.map((detail) => {
            var href1="#a"+(detail.id);
            var href2="a"+(detail.id);
            var idHtml="b"+(detail.id);
            return (
                <div key={detail.id}>
                    <li className="table-success">
                        Name: <strong>{detail.title}</strong> 
                        <br></br>
                        advertiser Name: {detail.advertiserName} 
                        <br></br>
                        Detail: {detail.description}
                        <br></br>
                        <a href={detail.link} target="blank" className="btn btn-success">See More Detail</a>  
                        <br></br>
                        <br></br>
                        <p>
                            <a className="btn btn-success" data-toggle="collapse" href={href1} role="button" aria-expanded="false" aria-controls="collapseExample">
                            Copy the Link
                            </a>
                        </p>

                        <div className="collapse" id={href2}>
                            <textarea readOnly
                            ref={(textarea) => this.textArea = textarea}
                            value={detail.link}
                            id={idHtml}
                            style={{width: '100%'}}

                            />
                            <button className="btn btn-outline-success" onClick={() => this.myFunction(idHtml)}>Copy Link</button>
                        </div>
                        <br></br>
                        <br></br>
                        <img src={detail.imageLink} alt={detail.link} className="rounded mx-auto d-block" style={maxStyle}></img>
                    </li>
                    <br></br>
                </div>
            )
        })

        var divStyle = {
            textalign:"center",
            width:"1000px" ,
            height:"400px"
          };
        return (
            <div>
                <br></br>
                <Link className="btn-lg btn-success" to="/"> Back</Link>
                <div className="text-center">
                    {/* <Link className="btn-lg btn-success" to="/"> Back</Link> */}
                    <h2>{this.props.match.params.class} Offers:</h2>
                </div>
                
                <br></br>
                <ul className="collection">
                    {MyOffers}
                </ul>

                <div className="myChartContainer" style={divStyle}>
                <canvas id="myChart" width="1000" height="400"></canvas>
                </div>
            </div>
        )
    }
}

export default GetOfferByText
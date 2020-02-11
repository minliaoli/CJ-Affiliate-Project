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

        var link=`http://localhost:5000/alg/${theText}`;
        //var link=`http://localhost:3000/api/CJOffers?filter={"where":{"or":[{"id":"5e3a7d30f125753e48b6c16b"},{"id":"5e3a7cc8f125753e48b6b51b"},{"id":"5e3a7d1bf125753e48b6bdf2"},{"id":"5e3a7d30f125753e48b6c306"},{"id":"5e3b96f86d73459893a3c807"}]}}`;

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
                    <div className="card"> 
                    <tr className="table-success"> 
                    <div class="row">
                    <div className="col">
                    <br></br>
                    <strong>Name: </strong> {detail.title} 
                        <br></br>
                    <strong>advertiser Name: </strong>{detail.advertiserName} 
                        <br></br>
                    <strong>Detail: </strong>{detail.description}
                        <br></br>
                        <div className="btn-group">
                        <a href={detail.link} target="blank" className="btn btn-success">See More Detail</a>  
                            
                        <a className="btn btn-outline-success" data-toggle="collapse" href={href1} role="button" aria-expanded="false" aria-controls="collapseExample">
                        Copy the Link
                        </a>
                        </div>
                        <br></br>

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
                    </div>
                        
                    <div className="col">
                    <br></br>
                    <img src={detail.imageLink} alt={detail.link} className="rounded mx-auto d-block" style={maxStyle}></img>
                    <br></br>
                    </div>
                    </div>
                    </tr> 
                    </div>
                    
                </div>
            )
        })

        var divStyle = {
            textalign:"center",
            width:"80%" ,
            height:"600px"
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
                <canvas id="myChart"></canvas>
                </div>
            </div>
        )
    }
}

export default GetOfferByText
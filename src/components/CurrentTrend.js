import React, { Component } from 'react'
import MyChart from  '../components/MyChart';
import axios from 'axios';

export class CurrentTrend extends Component {
    constructor(props){
        super();
        this.state={
            AxDone:false,
            trendList: []
        }
        this.getTrend  = this.getTrend.bind(this); 
    }
    getTrend(){
        var link=`http://localhost:5000/trendwords`;
        console.log(`opening ${link}`)
        axios.get(link)
        .then(response => 
                {
                    this.setState({trendList:response.data})
                }
            )
        .catch(err => console.log(err));
        this.setState({AxDone:true})
    }
    componentDidMount(){
        this.getTrend()
    }
    render() {
        const wordList=this.state.trendList.map((word) => {
            return (
            <li key={word} className="list-group-item py-1">
                {word}
            </li>
                );
            }
        )
        return (
            <div className="modal-body row pl-5 pr-5">
                <div className="col-md-3">
                    <p> <strong>Current Trending: </strong>
                    </p>
                    <ul className="list-group list-group-flush">
                    {wordList}
                    </ul>
                </div>

                <div className="col-md-9">
                    <MyChart/>
                </div>
            </div>

        )
    }
}

export default CurrentTrend

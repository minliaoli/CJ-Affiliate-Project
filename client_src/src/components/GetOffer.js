import React, { Component } from 'react';
import axios from 'axios';
import {Link} from 'react-router-dom';

class GetOffer extends Component {
    constructor(props){
        super();
        this.state={
            details:[]
        }
    }
    componentDidMount(){
        this.getMeetup();
    }
    getMeetup(){
        let theTypes=this.props.match.params.class.split("+");
        //let className=this.props.match.params.class;
        var link=`http://localhost:3000/api/OneOffers?filter={"where":{"or":[`;
        link+=`{"class":"${theTypes[1]}"}`;
        for(var i=2;i<theTypes.length;i++){
            link+=",";
            link+=`{"class":"${theTypes[i]}"}`;
        }
        link+=`]}}`
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
        const MyOffers = this.state.details.map((detail) => {
            return (
                <div key={detail.id}>
                    <li className="table-success">
                        Name: <strong>{detail.name}</strong> Brand: {detail.brand} 
                        <br></br>
                        Detail: {detail.detail}
                    </li>
                    <br></br>
                </div>
            )
        })
        return (
            <div>
                <br/>
                <Link className="btn btn-success" to="/"> Back</Link>
                <h2>{this.props.match.params.class} Offers:</h2>
                <ul className="collection">
                    {MyOffers}
                </ul>
            </div>
        )
    }
}

export default GetOffer
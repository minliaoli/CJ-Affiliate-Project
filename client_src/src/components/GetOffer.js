import React, { Component } from 'react';
import axios from 'axios';
import {Link} from 'react-router-dom';

class GetOffer extends Component {
    constructor(props){
        super();
        this.state={
            details:''
        }
    }
    componentDidMount(){
        this.getMeetup();
    }
    getMeetup(){
        let classId=this.props.match.params.id;
        axios.get(`http://localhost:3000/api/offers/${classId}`)
        .then(response => {
            this.setState({details: response.data}, () => {
                console.log(this.state);
            })
        })
        .catch(err => console.log(err));
    }
    render() {
        return (
            <div>
                <br/>
                <Link className="btn grey" to="/"> Back</Link>
                <h2>{this.state.details.class}</h2>
                <h3>Offers:{this.state.details.detail}</h3>
            </div>
        )
    }
}

export default GetOffer
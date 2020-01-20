import React, { Component } from 'react'
const axios = require('axios');

const options = {
    url: 'http://localhost:5000/test/data',
    method: 'GET'//,
    // headers: {
    //   'Accept': 'application/json',
    //   'Content-Type': 'application/json;charset=UTF-8'
    // },
    // data: {
    //   a: 10,
    //   b: 20
    // }
  };

export class BlogText extends Component {
    constructor(props) {
        super(props);
        this.state = {
          value: ''
        };
    
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
      }
    
    handleChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        alert('Blog Text: ' + this.state.value);
        event.preventDefault();
        axios(options)
            .then(response => {
                console.log(response);
  });
    }
    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <div className="form-group">
                    <label htmlFor="exampleFormControlTextarea4">Enter blog text:</label>
                    <textarea value={this.state.value} onChange={this.handleChange} 
                    className="form-control" id="exampleFormControlTextarea4" rows="5" placeholder="Enter blog here"></textarea>
                    <br></br>
                    <button type="submit" className="btn btn-success mb-2">submit</button>
                </div>    
            </form>
               
        )
    }
}

export default BlogText

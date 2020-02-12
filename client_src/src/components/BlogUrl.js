import React, { Component } from 'react'

export class BlogUrl extends Component {
    constructor(props) {
        super(props);
        this.state = {value: ''};
    
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    
    handleChange(event) {
        this.setState({value: event.target.value});
    }
    
    handleSubmit(event) {
        event.preventDefault();
        var theUrl=this.state.value;
        theUrl=encodeURIComponent(theUrl)
        window.alert(theUrl)
        var theLink = "http://localhost:3001/urloffers/";
        theLink += theUrl;
        console.log(theLink);
        window.location.href =theLink;
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <div className="form-group">
                <label htmlFor="urlInput">Enter URL</label>
                <input type="url" className="form-control" id="urlInput" aria-describedby="urlHelp" 
                value={this.state.value} onChange={this.handleChange} placeholder="Enter URL here"/>
                <small id="urlHelp" className="form-text text-muted">The blog might have access protection, if so please use text</small>
                </div>
                
                <button type="submit" className="btn btn-success">Submit</button>
            </form>
        )
    }
}

export default BlogUrl

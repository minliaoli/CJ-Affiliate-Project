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
        // window.alert(theUrl)
        var theLink = "http://localhost:3000/urloffers/";
        theLink += theUrl;
        console.log(theLink);
        window.location.href =theLink;
    }

    render() {
        return (
            <div>
                <br></br>
                <br></br>
                <br></br>
                <h3 className="text-center">Enter Blog URL</h3>
                <form onSubmit={this.handleSubmit} className="text-center">
                    <div className="form-group">
                        <p id="urlHelp" className="form-text text-muted">The blog might have access protection, if so please use text</p>
                        {/* <label htmlFor="urlInput">Enter URL</label> */}
                        <input type="url" className="form-control form-control-lg" id="urlInput" 
                        value={this.state.value} onChange={this.handleChange} placeholder="Enter URL here"/>
                    </div>
                    
                    <button type="submit" className="btn btn-success btn-lg">Submit</button>
                </form>          
            </div>
        )
    }
}

export default BlogUrl

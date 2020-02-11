import React, { Component } from 'react'

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
    };

    handleSubmit(event) {
        event.preventDefault();
        var blogText=this.state.value;

        if(0===blogText.length){
            window.alert("Please enter something!");
        }
        else{
            var theLink = "http://localhost:3001/textoffers/";
            theLink += this.state.value;
            console.log(theLink);
            window.location.href =theLink;
          }

        // alert('Blog Text: ' + this.state.value);
    };


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

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
            //blogText=toString(blogText)
            console.log(typeof(blogText))
            // blogText=blogText.replace(/\\["']/g, ' ')
            blogText=blogText.replace(/[^A-Za-z0-9 ]/g, ' ');
            // blogText=blogText.replace(/[/]+/g, ' ');
            // blogText=blogText.replace(/\\|\//g,' ');
            // blogText=blogText.replace(/\\"/g, ' ');
            window.alert(blogText)
            blogText = encodeURIComponent(blogText)
            //console.log(blogText);
            var theLink = "http://localhost:3001/textoffers/";
            theLink += blogText;
            //window.alert(theLink);
            //theLink = encodeURI(theLink)
            window.location.href = theLink;
            window.alert(theLink)
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

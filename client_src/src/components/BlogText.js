import React, { Component } from 'react'

export class BlogText extends Component {
    render() {
        return (
            <div class="form-group">
                <label for="exampleFormControlTextarea4">Enter blog text:</label>
                <textarea class="form-control" id="exampleFormControlTextarea4" rows="5"></textarea>
                <br></br>
                <button type="submit" class="btn btn-success mb-2">submit</button>
            </div>                   
        )
    }
}

export default BlogText

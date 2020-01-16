import React, { Component } from 'react'

export class BlogUrl extends Component {
    render() {
        return (
            <form>
                <div className="form-group">
                <label htmlFor="urlInput">Enter URL</label>
                <input type="email" className="form-control" id="urlInput" aria-describedby="urlHelp" placeholder="Enter URL" />
                <small id="urlHelp" className="form-text text-muted">The blog might have access protection, if so please use text</small>
                </div>
                
                <button type="submit" className="btn btn-success">Submit</button>
            </form>
        )
    }
}

export default BlogUrl

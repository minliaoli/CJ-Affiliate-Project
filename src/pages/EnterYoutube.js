import React, { Component } from 'react'
import '../css/App.css';
import BlogYoutube from '../components/BlogYoutube';

export class EnterYoutube extends Component {
    render() {
        return (
            <div className="App">
                <div className="card-body">
                  <BlogYoutube />
                </div>
            </div>
        )
    }
}

export default EnterYoutube

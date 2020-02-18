import React, { Component } from 'react'
import '../css/App.css';
import BlogUrl from '../components/BlogUrl';

export class EnterYoutube extends Component {
    render() {
        return (
            <div className="App">
                <div className="card-body">
                  <BlogUrl />
                </div>
            </div>
        )
    }
}

export default EnterYoutube

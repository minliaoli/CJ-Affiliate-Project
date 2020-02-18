import React, { Component } from 'react'
import '../css/App.css';
import BlogText from '../components/BlogText';

export class EnterText extends Component {
    render() {
        return (
            <div className="App">
                <div className="card-body">
                  <BlogText />
                </div>
            </div>
        )
    }
}

export default EnterText

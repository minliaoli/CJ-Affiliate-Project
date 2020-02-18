import React, { Component } from 'react'
import '../css/App.css';
import BlogTypes from '../components/BlogTypes';

export class EnterType extends Component {
    render() {
        return (
            <div className="App">
                <div className="card-body">
                  <BlogTypes />
                </div>
            </div>
        )
    }
}

export default EnterType

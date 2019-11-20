import React, { Component } from 'react'

export class Header extends Component {
    render() {
        return (
            <header className="App-header">
                <div className="App-container">
                    <div id="branding">
                    <h1>CJ-Affiliate Bloggers' Tool</h1>
                    </div>
                    <nav>
                    <ul>
                        <li><a href="../">Home</a></li>
                        <li><a href="../about">About</a></li>
                        <li><a href="../contact">Contact</a></li>
                    </ul>
                    </nav>
                </div>
            </header>
        )
    }
}

export default Header


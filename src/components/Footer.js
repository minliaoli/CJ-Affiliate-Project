import React, { Component } from 'react'
import CurrentTrend from './CurrentTrend';

export class Footer extends Component {
    render() {
        return (
            <footer className="text-center">
            <br></br>
            <br></br>
            <br></br>
            <br></br>
            <br></br>
            <br></br>
            <br></br>
            <hr/>
            <a className="btn btn-outline-success btn-block" data-toggle="collapse" href="#trending" role="button" aria-expanded="false" aria-controls="collapseExample">
                Current Trend
            </a>
            <div className="collapse" id="trending">
                <CurrentTrend/>
            </div>

            <hr/>
            <br></br>
                <div>
                    <p>
                        Version 1.1.5<br></br>
                        <a href="../contact" className="text-success">Contact</a> | <a href="../about" className="text-success">About</a> | <a href="../about" className="text-success">How to use</a>
                    </p>
                </div>
                <p>CJ Affiliate & The Great Fantastic Team, Copyright &copy; , 2019 </p>
            </footer>
        )
    }
}

export default Footer

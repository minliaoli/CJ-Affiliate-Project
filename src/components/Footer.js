import React, { Component } from 'react'
// import MyChart from "./MyChart"

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
            {/* <div className="text-center w-50 p-3 mx-auto">
                <MyChart/>
            </div> */}
            <hr/>
            <br></br>
                <div>
                    <p>
                        Version 1.0.0<br></br>
                        <a href="../contact" className="text-success">Contact</a> | <a href="../about" className="text-success">About</a> | <a href="../about" className="text-success">How to use</a>
                    </p>
                </div>
                <p>CJ Affiliate & The Great Fantastic Team, Copyright &copy; , 2019 </p>
            </footer>
        )
    }
}

export default Footer

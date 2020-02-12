import React from 'react';
import '../css/App.css';

class Loading extends React.Component {
    render() {
        return (
            <div className="App text-center">
                <br></br>
                <br></br>
                <br></br>
                <br></br>
                <br></br>
                <div className="spinner-grow text-success justify-content-center" role="status">
                <span className="sr-only">Loading...</span>
                <br></br>
                </div>
                <h2>Loading...</h2>
                <br></br>
                <br></br>
                <br></br>
                <br></br>
                <br></br>
            </div>
        );
    }
}

export default Loading

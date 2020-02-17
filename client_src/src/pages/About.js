import React from 'react';
import '../css/App.css';
import Loading from  '../components/Loading';

class About extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      done: false
    };
  }

  componentDidMount() {
    this.setState({done: true})
  }


  render() {

    // console.log(this.state.todos)
    return (
      <div className="App text-center">

      <div>
        {!this.state.done ? (
           <Loading/>
        ) : (
          <h1>hello world</h1>
        )}
      </div>


      </div>
    );
  }
}


export default About;
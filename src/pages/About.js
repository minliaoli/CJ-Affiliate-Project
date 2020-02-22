import React from 'react';
import '../css/App.css';
import Loading from  '../components/Loading';

class About extends React.Component {
  constructor(props) {
    super(props);
    this.state={done: false};
    this.myClick  = this.myClick.bind(this); 
  }


  componentDidMount() {
    this.setState({done: false})
  }

  myAlert(){
    if(this.state.alertOn){
      return (<div className="alert alert-success" role="alert">
      This is a success alert—check it out!
    </div>)
    }
  }
  myClick(){
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
          <div>

          <div className="alert alert-success" role="alert">
            This is a success alert—check it out!
          </div>

          <h1>hello world</h1>
          

          </div>
        )}
      </div>
      <button className="btn-success" onClick={this.myClick}>push</button>


      </div>
    );
  }
}


export default About;
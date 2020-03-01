import React from 'react';
import '../css/App.css';
import Loading from  '../components/Loading';
import Fade from 'react-reveal/Fade';

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
    this.setState({done: !this.state.done})
  }
  render() {
    return (
      <div className="App text-center">
        <Fade>
          <img  src="../youTube.png" href="../" alt="Youtube" width={120} height={120} />
        </Fade>


        
      <div>
        {!this.state.done ? (
           <Loading/>
        ) : (
          <div>

          <div className="alert alert-success fade show" role="alert">
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
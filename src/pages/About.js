import React from 'react';
import '../css/App.css';
import Loading from  '../components/Loading';
import { CSSTransition } from 'react-transition-group';
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


        <CSSTransition
        in={this.state.done}
        appear={true}
        timeout={600}
        classNames="fade"
        >
          <img src="https://cdn2.jianshu.io/assets/default_avatar/4-3397163ecdb3855a0a4139c34a695885.jpg" alt="nane"/>
        
        </CSSTransition>
        
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
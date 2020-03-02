import React from 'react';
import '../css/App.css';
import { FaRegQuestionCircle } from "react-icons/fa";
import CurrentTrend from '../components/CurrentTrend';

class Contact extends React.Component {
  constructor(props){
    super();
    this.myFunction = this.myFunction.bind(this);
    this.hoverHandler = this.hoverHandler.bind(this);
  }

  myFunction(idN) {
    let me=document.getElementById(idN)
    console.log(me)
    // let copyText = this.textArea;
    me.select();
    me.setSelectionRange(0, 99999); 
    document.execCommand("copy");
    alert(`AD Link Copied! ${me}`);
  }
  hoverHandler(){

  }

  render() {
    // var divStyle = {
    //   textalign:"center",
    //   width:"80%" ,
    //   height:"600px"
    // };    
    return (
      <div className="App">
        <h3 className="text-center">
    Enter Blog Text <FaRegQuestionCircle size={20} onMouseEnter={this.hoverHandler()} />
        </h3>

        <section id = "App-selection">
          <div className="App-container">
            <h2>This is contact!</h2>
          </div>
        </section>

        <CurrentTrend/>

          


      </div>



    );
  }
}


export default Contact;
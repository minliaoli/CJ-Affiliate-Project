import React from 'react';
import '../css/App.css';
import MyChart from  '../components/MyChart';

class Contact extends React.Component {
  constructor(props){
    super();
    this.myFunction = this.myFunction.bind(this);
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

  render() {
    // var divStyle = {
    //   textalign:"center",
    //   width:"80%" ,
    //   height:"600px"
    // };    
    return (
      <div className="App">

        <section id = "App-selection">
          <div className="App-container">
            <h2>This is contact!</h2>
          </div>
        </section>

        <div className="modal-body row">
          <div className="col-md-6">
            <img className="mySlides" src="https://media.expedia.com/hotels/3000000/2230000/2228000/2227922/d1f35bf5_b.jpg" alt="custom_html_banner1" style={{width: '90%'}} />
          </div>
          <div className="col-md-6">
            <MyChart/>
          </div>
        </div>

          


      </div>



    );
  }
}


export default Contact;
import React from 'react';
import '../css/App.css';

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
    // console.log(this.state.todos)
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
            <h2>TextTextTextText</h2>
          </div>
        </div>

          <p>
            <a className="btn btn-success btn-block" data-toggle="collapse" href="#a5e386a4199a3e94b4c3657cf" role="button" aria-expanded="false">
              Link with href
            </a>
          </p>

          <div className="collapse" id="a5e386a4199a3e94b4c3657cf">
            <textarea readOnly
              ref={(textarea) => this.textArea = textarea}
              value="Example copy for the textarea."
              id="1111"
              style={{width: '100%'}}
            />
            <button className="btn btn-success" onClick={() => this.myFunction("1111")}>Copy text</button>
          </div>

          <p>
            <a className="btn btn-success btn-block" data-toggle="collapse" href="#collapseExample2" role="button" aria-expanded="false" aria-controls="collapseExample">
              Link with href
            </a>
          </p>

          <div className="collapse" id="collapseExample2">
            <textarea readOnly
              ref={(textarea) => this.textArea = textarea}
              value="Example 2"
              id="12223"
              style={{width: '100%'}}

            />
            <button className="btn btn-success" onClick={() => this.myFunction("12223")}>Copy text</button>
          </div>
        


      </div>



    );
  }
}


export default Contact;
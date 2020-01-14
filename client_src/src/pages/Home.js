import React from 'react';
import '../css/App.css';
import BlogTypes from '../components/BlogTypes';

class Home extends React.Component {


    render() {
      // console.log(this.state.todos)
      return (

        <div className="App">
          <br></br>
          
          <section id = "App-selection">
            <div className="App-container">
              <h2 style={{textAlign: 'center'}}><strong>Select Your Blog Types:</strong></h2>

              <p>
                <button class="btn btn-success btn-block text-left" type="button" data-toggle="collapse" data-target="#collapseExample1" aria-expanded="false" aria-controls="collapseExample">
                  Enter by selecting from keywords
                </button>
              </p>
              <div class="collapse" id="collapseExample1">
                <BlogTypes />
              </div>


              <p>
                <button class="btn btn-success btn-block text-left" type="button" data-toggle="collapse" data-target="#collapseExample2" aria-expanded="false" aria-controls="collapseExample">
                  Enter by entering blog text
                </button>
              </p>
              <div class="collapse" id="collapseExample2">
                <p>Text Area</p>
              </div>



              <p>
                <button class="btn btn-success btn-block text-left" type="button" data-toggle="collapse" data-target="#collapseExample3" aria-expanded="false" aria-controls="collapseExample">
                  Enter by entering URL
                </button>
              </p>
              <div class="collapse" id="collapseExample3">
                <p>URL Area</p>
              </div>




  
            </div>
          </section>
  
  
  
        </div>
      );
    }
  }
  
  
  export default Home;
  
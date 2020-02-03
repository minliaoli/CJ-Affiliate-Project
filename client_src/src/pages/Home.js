import React from 'react';
import '../css/App.css';
import BlogTypes from '../components/BlogTypes';
import BlogText from '../components/BlogText';
import BlogUrl from '../components/BlogUrl';

class Home extends React.Component {


    render() {
      // console.log(this.state.todos)
      return (

        <div className="App">
          <br></br>


                  
          <section id = "App-selection">
            <div className="App-container">
              <h2 style={{textAlign: 'center'}}><strong>Select Your Blog Types:</strong></h2>

            <div className="accordion" id="accordionExample">
            <div className="card">
              <div className="card-header" id="headingOne">
                <h2 className="mb-0">
                  <button className="btn btn-success btn-block text-left" type="button" data-toggle="collapse" data-target="#collapseOne" aria-expanded="false" aria-controls="collapseOne">
                  Enter by entering URL
                  </button>
                </h2>
              </div>
              <div id="collapseOne" className="collapse show" aria-labelledby="headingOne" data-parent="#accordionExample">
                <div className="card-body">
                  <BlogUrl />
                </div>
              </div>
            </div>

            <div className="card">
              <div className="card-header" id="headingTwo">
                <h2 className="mb-0">
                  <button className="btn btn-success btn-block text-left" type="button" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="true" aria-controls="collapseTwo">
                    Enter by entering blog text
                  </button>
                </h2>
              </div>
              <div id="collapseTwo" className="collapse" aria-labelledby="headingTwo" data-parent="#accordionExample">
                <div className="card-body">
                  <BlogText />
                </div>
              </div>
            </div>

            <div className="card">
              <div className="card-header" id="headingThree">
                <h2 className="mb-0">
                  <button className="btn btn-success btn-block text-left" type="button" data-toggle="collapse" data-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                  Enter by selecting from keywords 
                  </button>
                </h2>
              </div>
              <div id="collapseThree" className="collapse" aria-labelledby="headingThree" data-parent="#accordionExample">
                <div className="card-body">
                <BlogTypes />
                </div>
              </div>
            </div>
          </div>

  
            </div>
          </section>
  
  
  
        </div>
      );
    }
  }
  
  
  export default Home;
  
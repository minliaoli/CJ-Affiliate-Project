import React from 'react';
import '../css/App.css';

class About extends React.Component {


  render() {
    // console.log(this.state.todos)
    return (
      <div className="App">
        
        <section id = "App-selection">
          <div className="App-container">
            <h2>This is About!</h2>
          </div>


          <p>
            <a class="btn btn-success btn-block" data-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
              Link with href
            </a>
          </p>

          <div class="collapse" id="collapseExample">
              Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident.
          </div>

          <div className="tab">
            <p>
              <button class="btn btn-success btn-block text-left" type="button" data-toggle="collapse" data-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
                  Button with data-target
              </button>
            </p>
          </div>



        </section>



      </div>
    );
  }
}


export default About;
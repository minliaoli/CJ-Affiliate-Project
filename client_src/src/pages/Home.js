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

              <BlogTypes />
  
            </div>
          </section>
  
  
  
        </div>
      );
    }
  }
  
  
  export default Home;
  
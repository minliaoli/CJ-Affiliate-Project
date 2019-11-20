import React from 'react';
import '../css/App.css';
import BlogTypes from '../components/BlogTypes';

class Home extends React.Component {


    render() {
      // console.log(this.state.todos)
      return (
        <div className="App">
          
          <section id = "App-selection">
            <div className="App-container">
              <h2>Select Your Blog Types:</h2>
  
              <BlogTypes />
  
            </div>
          </section>
  
  
  
        </div>
      );
    }
  }
  
  
  export default Home;
  
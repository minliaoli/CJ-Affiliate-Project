import React from 'react';
import './css/App.css';
import Header from './components/Header';
import Footer from './components/Footer';
import Main from './pages/Main.js';



class App extends React.Component {


  render() {
    // console.log(this.state.todos)
    return (
      <div className="App">
        <Header/>
        
        <section id = "App-selection">
          <div className="App-container">
            <Main/>

          </div>
        </section>

        <Footer/>


      </div>
    );
  }
}


export default App;

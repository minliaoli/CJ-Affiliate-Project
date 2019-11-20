import React  from 'react'
import {Switch, Route} from 'react-router-dom';
import Home from './Home.js';
import About from './About.js';
import Contact from './Contact.js';
import GetOffer from '../components/GetOffer.js';


const Main = () => (
    <main>
        <Switch>
            <Route exact path ="/" component ={Home} />
            <Route exact path ="/about" component ={About} />
            <Route exact path ="/contact" component ={Contact} />
            <Route exact path = '/offers/:id' component= {GetOffer}/>
        </Switch>

    </main>
)


export default Main
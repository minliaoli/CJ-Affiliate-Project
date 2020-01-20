import React  from 'react'
import {Switch, Route} from 'react-router-dom';
import Home from './Home.js';
import About from './About.js';
import Contact from './Contact.js';
import GetOffer from '../components/GetOffer.js';
import GetOfferByText from '../components/GetOfferByText.js';


const Main = () => (
    <main>
        <Switch>
            <Route exact path ="/" component ={Home} />
            <Route exact path ="/about" component ={About} />
            <Route exact path ="/contact" component ={Contact} />
            <Route exact path = '/offers/:class' component= {GetOffer}/>
            <Route exact path = '/textoffers/:blogtext' component= {GetOfferByText}/>
        </Switch>

    </main>
)


export default Main
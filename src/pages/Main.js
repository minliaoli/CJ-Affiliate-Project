import React  from 'react'
import {Switch, Route} from 'react-router-dom';
import EnterURL from './EnterURL.js';
import EnterText from './EnterText.js';
import EnterType from './EnterType.js';
import EnterYoutube from './EnterYoutube.js';
import About from './About.js';
import Contact from './Contact.js';
import GetOffer from '../components/GetOffer.js';
import GetOfferByText from '../components/GetOfferByText.js';
import GetOfferByUrl from '../components/GetOfferByUrl.js';


const Main = () => (
    <main>
        <Switch>
            <Route exact path ="/" component ={EnterURL} />
            <Route exact path ="/enterurl" component ={EnterURL} />
            <Route exact path ="/entertext" component ={EnterText} />
            <Route exact path ="/entertype" component ={EnterType} />
            <Route exact path ="/enteryoutube" component ={EnterYoutube} />
            <Route exact path ="/about" component ={About} />
            <Route exact path ="/contact" component ={Contact} />
            <Route exact path = '/offers/:class' component= {GetOffer}/>
            <Route exact path = '/textoffers/:blogtext' component= {GetOfferByText}/>
            <Route path = '/urloffers/:blogurl' component= {GetOfferByUrl}/>
        </Switch>

    </main>
)


export default Main
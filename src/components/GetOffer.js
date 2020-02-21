import React, { Component } from 'react';
import axios from 'axios';
import {Link} from 'react-router-dom';

class GetOffer extends Component {constructor(props){
    super();
    this.state={
        details:[]
    }
}
componentDidMount(){
    this.getOffers();
}
myFunction(idN) {
    let me=document.getElementById(idN)
    console.log(me)
    // let copyText = this.textArea;
    me.select();
    me.setSelectionRange(0, 99999); 
    document.execCommand("copy");
    alert(`AD Link Copied!`);
  }
getOffers(){
  ///get offer part
    let theTypes=this.props.match.params.class;
    // window.alert(theUrl)

    var link=`http://localhost:5000/alg/${theTypes}`;
    //var link=`http://localhost:3000/api/CJOffers?filter={"where":{"or":[{"id":"5e3a7d30f125753e48b6c16b"},{"id":"5e3a7cc8f125753e48b6b51b"},{"id":"5e3a7d1bf125753e48b6bdf2"},{"id":"5e3a7d30f125753e48b6c306"},{"id":"5e3b96f86d73459893a3c807"}]}}`;

    console.log(`opening ${link}`)
   
    axios.get(link)
    .then(response => 
            {
                let TheArray=[];
                for (var i=0;i<response.data.length;i++)
                    {TheArray.push(response.data[i]); }
                this.setState({details : TheArray })
            }
        )
    .catch(err => console.log(err));
}
render() {
    var maxStyle = {
        maxHeight : 200
      };
    const MyOffers = this.state.details.map((detail) => {
        var href1="#a"+(detail.id);
        var href2="a"+(detail.id);
        var href3="#aa"+(detail.id);
        var href4="aa"+(detail.id);
        var idHtml="b"+(detail.id);
        return (
            <div className="card-body" key={detail.id}>
                <div className="card"> 
                {/* <tr className="table-success">  */}
                <div className="table-success">
                <div className="row ml-md-auto">
                <div className="col ml-md-auto">
                <br></br>
                <strong>Name: </strong> {detail.title} 
                    <br></br>
                <strong>Advertiser Name: </strong>{detail.advertiserName} 
                    <br></br>
                    <br></br>
                    <div className="btn-group">
                    <a className="btn btn-outline-success" data-toggle="collapse" href={href3} role="button" aria-expanded="false" aria-controls="collapseExample">
                    View Detail
                    </a>

                    <a href={detail.link} target="blank" className="btn btn-success">Open Product Page</a>  
                        
                    <a className="btn btn-outline-success" data-toggle="collapse" href={href1} role="button" aria-expanded="false" aria-controls="collapseExample">
                    Copy the Link
                    </a>
                    </div>
                    <br></br>
                    <br></br>

                    <div className="collapse" id={href4}>
                        <strong>Detail: </strong>{detail.description}
                        <br></br>
                    </div>

                    <div className="collapse" id={href2}>
                        <textarea readOnly
                        ref={(textarea) => this.textArea = textarea}
                        value={`<a href="${detail.link}" target="blank"><img src="${detail.imageLink}" title="AD from Offer Matcher" alt="AD Pic"></a><br><br/><small>Advertisement provided by the Offer Matcher and CJ Affiliate.</small>`}
                        id={idHtml}
                        rows="6"
                        style={{width: '100%' , height: '100%'}}
                        />
                        <button className="btn btn-outline-success" onClick={() => this.myFunction(idHtml)}>Copy Link</button>
                    </div>
                    <br></br>
                </div>
                    
                <div className="col">
                <br></br>
                <img src={detail.imageLink} alt={detail.link} className="rounded mx-auto d-block" style={maxStyle}></img>
                <br></br>
                </div>
                </div>
                </div>
                </div>
                
            </div>
        )
    })

    return (
        <div>
            <br></br>
                <div className="sticky-top text-right pr-4" >
                    <Link className="btn-lg btn-success" to="/"> Back</Link>
                </div>
            <div className="text-center">
                {/* <Link className="btn-lg btn-success" to="/"> Back</Link> */}
                <h2> Offers:</h2>
            </div>
            
            <br></br>
            <ul className="collection">
                {MyOffers}
            </ul>

        </div>
    )
}
}

export default GetOffer
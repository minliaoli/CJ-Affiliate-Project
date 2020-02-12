import React, { Component } from "react";
import axios from 'axios';
import Checkbox from "./Checkbox";

const BTypes = [
    'Sports','Technology','Politics','Cooking','Pets', 'Education', 'Travelling',
     'Parenting', 'Gaming', 'Business','Music', 'Movie', 'Cars', 'Beaut','Design',
      'Photography', 'Health', 'History'
  ];


export class BlogTypes extends Component {
  state = {
    offers: [],
    checkboxes: BTypes.reduce(
      (options, option) => ({
        ...options,
        [option]: false
      }),
      {}
    )
  };
  componentDidMount(){
    this.getOffers();
  }
  getOffers(){
    axios.get('http://localhost:3000/api/offers')
    .then(response => {
        this.setState({offers: response.data}, () => {
            // console.log(this.state);
        })
    })
    .catch(err => console.log(err));
}

  selectAllCheckboxes = isSelected => {
    Object.keys(this.state.checkboxes).forEach(checkbox => {
      this.setState(prevState => ({
        checkboxes: {
          ...prevState.checkboxes,
          [checkbox]: isSelected
        }
      }));
    });
  };

  selectAll = () => this.selectAllCheckboxes(true);

  deselectAll = () => this.selectAllCheckboxes(false);

  handleCheckboxChange = changeEvent => {
    const { name } = changeEvent.target;

    this.setState(prevState => ({
      checkboxes: {
        ...prevState.checkboxes,
        [name]: !prevState.checkboxes[name]
      }
    }));
  };

  handleFormSubmit = formSubmitEvent => {
    formSubmitEvent.preventDefault();
    var selected=Object.keys(this.state.checkboxes).filter(checkbox => this.state.checkboxes[checkbox]);
    //console.log(this.state.offers[1].class);

    if(0===selected.length){
      window.alert("Please select at least one type!");
    }
    else{
      var theLink = "http://localhost:3001/offers/";
      selected.forEach(checkbox => {
        //console.log(checkbox);
        for (var i=0;i<this.state.offers.length;i++)
          {
              if(this.state.offers[i].class===checkbox){
                theLink+="+";
                theLink+=this.state.offers[i].class;
                //window.open(`http://localhost:3001/offers/${this.state.offers[i].class}`);
                //window.location.href = "https://www.runoob.com";
              }
          }
      })
      console.log(theLink);
      window.location.href =theLink;
    }
  };

  createCheckbox = option => (
    <Checkbox
      label={option}
      isSelected={this.state.checkboxes[option]}
      onCheckboxChange={this.handleCheckboxChange}
      key={option}
    />
  );

  createCheckboxes = () => BTypes.map(this.createCheckbox);

  render() {
    return (
      <div className="container">
        <div className="row mt-5">
          <div className="col-sm-12">
            <form onSubmit={this.handleFormSubmit} >
              {this.createCheckboxes()}
              <br></br>

              <div className="bs-component" style={{marginBottom: '15px'}}>
                <div className="btn-group" role="group" aria-label="Basic example">
                  <button type="button" onClick={this.selectAll} className="btn btn-success">Select All</button>
                  <button type="button" onClick={this.deselectAll} className="btn btn-success">Deselect All</button>
                  <button type="submit" className="btn btn-success  active">Submit</button>
                </div>
              </div>

            </form>
          </div>
        </div>
      </div>
    );
  }
}

export default BlogTypes
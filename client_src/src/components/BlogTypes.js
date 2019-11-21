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
    console.log(this.state.offers[1].class);

    if(0===selected.length){
      console.log("Nothing is selected!");
    }
    else{
      selected.forEach(checkbox => {
        console.log(checkbox)
        for (var i=0;i<this.state.offers.length;i++)
          {
              if(this.state.offers[i].class===checkbox){
                window.open(`http://localhost:3001/offers/${this.state.offers[i].class}`)
              }
          }
      })
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
            <form onSubmit={this.handleFormSubmit}>
              {this.createCheckboxes()}

              <div className="form-group mt-2">
                <button
                  type="button"
                  className="btn btn-outline-primary mr-2"
                  onClick={this.selectAll}
                >
                  Select All
                </button>
                <button
                  type="button"
                  className="btn btn-outline-primary mr-2"
                  onClick={this.deselectAll}
                >
                  Deselect All
                </button>
                <button type="submit" className="btn btn-primary">
                  Save
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    );
  }
}

export default BlogTypes

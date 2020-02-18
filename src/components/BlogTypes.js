import React, { Component } from "react";
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
        this.setState({offers: ['Sports','Technology','Politics','Cooking','Pets', 'Education', 'Travelling',
     'Parenting', 'Gaming', 'Business','Music', 'Movie', 'Cars', 'Beaut','Design',
      'Photography', 'Health', 'History']})
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
      var theLink = "http://localhost:3000/offers/";
      selected.forEach(checkbox => {
        //console.log(checkbox);
        for (var i=0;i<this.state.offers.length;i++)
          {
              if(this.state.offers[i]===checkbox){
                theLink+="+";
                theLink+=this.state.offers[i];
                //window.open(`http://localhost:3000/offers/${this.state.offers[i].class}`);
                //window.location.href = "https://www.runoob.com";
              }
          }
      })
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
        <br></br>
        <br></br>
        <h2 className="text-center">Select keywords: </h2>
        <div className="row mt-5">
          <div className="col-sm-12">
            <form onSubmit={this.handleFormSubmit} >
              {this.createCheckboxes()}
              <br></br>

              <div className="bs-component text-center" style={{marginBottom: '15px'}}>
                <div className="btn-group" role="group" aria-label="Basic example">
                  <button type="button" onClick={this.selectAll} className="btn btn-success btn-lg">Select All</button>
                  <button type="button" onClick={this.deselectAll} className="btn btn-success btn-lg">Deselect All</button>
                  <button type="submit" className="btn btn-success btn-lg active">Submit</button>
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

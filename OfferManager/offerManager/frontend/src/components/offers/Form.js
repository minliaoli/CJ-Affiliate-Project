import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addOffers } from '../../actions/offers';

export class Form extends Component {
    state = {
        name: "",
        price: "",
        description: ""
    }

    static propTypes = {
        addOffer: PropTypes.func.isRequired
    };

    onChange = e => this.setState({ [e.target.name] : e.target.value });

    onSubmit = e => {
        e.preventDefault();
        const{ name, price, description } = this.state;
        const offer = { name, price, description };
        this.props.addOffers(offer)
        this.setState({
                name: "",
                price: "",
                description: ""
            });
        console.log("submit");
    }

    render() {
        const { name, price, description } = this.state;
        return (
          <div className="card card-body mt-4 mb-4">
            <h2>Add Offer</h2>
            <form onSubmit={this.onSubmit}>
              <div className="form-group">
                <label>Name</label>
                <input
                  className="form-control"
                  type="text"
                  name="name"
                  onChange={this.onChange}
                  value={name}
                />
              </div>
              <div className="form-group">
                <label>Price</label>
                <input
                  className="form-control"
                  type="text"
                  name="price"
                  onChange={this.onChange}
                  value={price}
                />
              </div>
              <div className="form-group">
                <label>Description</label>
                <textarea
                  className="form-control"
                  type="text"
                  name="description"
                  onChange={this.onChange}
                  value={description}
                />
              </div>
              <div className="form-group">
                <button type="submit" className="btn btn-primary">
                  Submit
                </button>
              </div>
            </form>
          </div>
        );
      }
    }

export default connect(null, {addOffers})(Form);

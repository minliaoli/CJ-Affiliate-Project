import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getOffers, deleteOffers } from '../../actions/offers';

export class Offers extends Component {
  static propTypes = {
      offers: PropTypes.array.isRequired
  };

  componentDidMount() {
      this.props.getOffers();
  }

  render() {
      return (
        <Fragment>
          <h2>Leads</h2>
          <table className="table table-striped">
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Message</th>
                <th />
              </tr>
            </thead>
            <tbody>
              {this.props.offers.map(offer => (
                <tr key={offer.id}>
                  <td>{offer.id}</td>
                  <td>{offer.name}</td>
                  <td>{offer.price}</td>
                  <td>{offer.description}</td>
                  <td>
                    <button
                      onClick={this.props.deleteOffers.bind(this, offer.id)}
                      className="btn btn-danger btn-sm"
                    >
                      {" "}
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </Fragment>
      );
    }
  }
  
const mapStateToProps = state => ({
    offers: state.offers.offers
});

export default connect(mapStateToProps, 
                    { getOffers, deleteOffers })
                    (Offers);

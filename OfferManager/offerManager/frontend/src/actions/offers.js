import axios from 'axios';

import { GET_OFFERS, DELETE_OFFERS } from './types';

//GET OFFERS
export const getOffers = () => dispatch => {
    axios.get("/api/offers/")
        .then(res => {
            dispatch({
                type: GET_OFFERS,
                payload: res.data
            });
        }).catch(err => console.log(err));
};

//DELETE OFFERs
export const deleteOffers = (id) => dispatch => {
    axios.get(`/api/offers/${id}/`)
        .then(res => {
            dispatch({
                type: DELETE_OFFERS,
                payload: id
            });
        }).catch(err => console.log(err));
};
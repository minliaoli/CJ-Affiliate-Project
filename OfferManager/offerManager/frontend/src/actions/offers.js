import axios from 'axios';

import { GET_OFFERS, DELETE_OFFERS, ADD_OFFERS, IMPORT } from './types';

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

export const getProducts = () => dispatch => {
    axios.get("/api/offers/")
        .then(res => {
            dispatch({
                type: IMPORT,
                payload: res.data
            });
        }).catch(err => console.log(err));
};

//DELETE OFFER
export const deleteOffers = id => dispatch => {
    axios.delete(`/api/offers/${id}/`)
        .then(res => {
            dispatch({
                type: DELETE_OFFERS,
                payload: id
            });
        }).catch(err => console.log(err));
};

//ADD OFFER
export const addOffers = offer => dispatch => {
    axios.post("/api/offers/", offer)
        .then(res => {
            dispatch({
                type: ADD_OFFERS,
                payload: res.data
            });
        }).catch(err => console.log(err));
};
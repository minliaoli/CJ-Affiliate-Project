import { GET_OFFERS, DELETE_OFFERS, ADD_OFFERS, IMPORT } from "../actions/types.js";

const initialState = {
    offers: []
}

export default function(state = initialState, action){
    switch(action.type){
        case GET_OFFERS:
            return { 
                ...state,
                offers: action.payload
            };
        case DELETE_OFFERS:
            return {  
                ...state,
                offers: state.offers.filter(offer => offer.id !== action.payload)
            };
        case ADD_OFFERS:
            return {
                ...state,
                offers: [...state.offers, action.payload]
            };
        case IMPORT:
            return {
                ...state,
                offers: action.payload
            };
    default:
        return state;
    }
}
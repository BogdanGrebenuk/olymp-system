import { combineReducers } from "redux";

import {
    SET_CONTESTS
} from "../actions";


function contestReducer(state=[], action) {
    switch (action.type) {
        case SET_CONTESTS:
            return action.payload.contests;
        default:
            return state;
    }
}


const mainReducer = combineReducers({
    contests: contestReducer
});

export default mainReducer;

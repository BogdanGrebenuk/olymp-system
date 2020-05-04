import { combineReducers } from "redux";

import {
    SET_CONTESTS,
    SET_CONTEST,
    SET_TASKS,
    ADD_TASK_IO,
    RESET_TASK_IOS
} from "../actions";


function contestReducer(state={}, action) {
    let temp;
    switch (action.type) {
        case SET_CONTESTS:
            const contests = action.payload.contests;
            temp = {};
            for (let contest of contests) {
                temp[contest.id] = contest;
            }
            return temp;
        case SET_CONTEST:
            const contestId = action.payload.contest.id;
            temp = {...state};
            temp[contestId] = action.payload.contest;
            return temp;
        default:
            return state;
    }
}


function taskReducer(state={}, action) {
    switch (action.type) {
        case SET_TASKS:
            const tasks = action.payload.tasks;
            const temp = {};
            for (let task of tasks) {
                temp[task.id] = task;
            }
            return temp;
        default:
            return state;
    }
}


function taskIOReducer(state=[], action) {
    switch (action.type) {
        case ADD_TASK_IO:
            return [...state, action.payload];
        case RESET_TASK_IOS:
            return [];
        default:
            return state;
    }
}


const mainReducer = combineReducers({
    contests: contestReducer,
    tasks: taskReducer,
    taskIOs: taskIOReducer
});

export default mainReducer;

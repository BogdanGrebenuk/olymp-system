import { combineReducers } from "redux";

import {
    SET_CONTESTS,
    SET_CONTEST,
    SET_TASKS,
    SET_TASK,
    ADD_TASK_IO,
    RESET_TASK_IOS,
    SET_CURRENT_USER,
    SET_TEAMS,
    SET_TEAM_MEMBERS,
    SET_USERS, SET_INVITES_FOR_TEAM, SET_INVITES_FOR_CONTEST
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
    let temp;
    switch (action.type) {
        case SET_TASKS:
            const tasks = action.payload.tasks;
            temp = {};
            for (let task of tasks) {
                temp[task.id] = task;
            }
            return temp;
        case SET_TASK:
            const task = action.payload.task;
            temp = {...state};
            temp[task.id] = task;
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


function currentUserReducer(state=null, action) {
    switch (action.type) {
        case SET_CURRENT_USER:
            return action.payload.user;
        default:
            return state;
    }
}


function teamsReducer(state={}, action) {
    let temp;
    switch (action.type) {
        case SET_TEAMS:
            const teams = action.payload.teams;
            temp = {};
            for (let team of teams) {
                temp[team.id] = team;
            }
            return temp;
        default:
            return state
    }
}


function teamMembersReducer(state={}, action) {
    let temp;
    switch (action.type) {
        case SET_TEAM_MEMBERS:
            const teamMembers = action.payload.teamMembers;
            temp = {};
            for (let tm of teamMembers) {
                temp[tm.id] = tm;
            }
            return temp;
        default:
            return state
    }
}


function usersReducer(state={}, action) {
    let temp;
    switch (action.type) {
        case SET_USERS:
            const users = action.payload.users;
            temp = {};
            for (let u of users) {
                temp[u.id] = u;
            }
            return temp;
        default:
            return state
    }
}


function invitesForTeamReducer(state={}, action) {
    let temp;
    switch (action.type) {
        case SET_INVITES_FOR_TEAM:
            const invitesForTeam = action.payload.invitesForTeam;
            temp = {};
            for (let i of invitesForTeam) {
                temp[i.id] = i;
            }
            return temp;
        default:
            return state
    }
}


function invitesForContestReducer(state={}, action) {
    let temp;
    switch (action.type) {
        case SET_INVITES_FOR_CONTEST:
            const invitesForContest = action.payload.invitesForContest;
            temp = {};
            for (let i of invitesForContest) {
                temp[i.id] = i;
            }
            return temp;
        default:
            return state
    }
}


const mainReducer = combineReducers({
    contests: contestReducer,
    tasks: taskReducer,
    taskIOs: taskIOReducer,
    currentUser: currentUserReducer,
    teams: teamsReducer,
    teamMembers: teamMembersReducer,
    users: usersReducer,
    invitesForTeam: invitesForTeamReducer, // for trainer
    invitesForContest: invitesForContestReducer // for participant
});

export default mainReducer;

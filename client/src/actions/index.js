export const GET_CONTEST = 'GET_CONTEST';
export const SET_CONTEST = 'SET_CONTEST';
export const GET_CONTESTS = 'GET_CONTESTS';
export const SET_CONTESTS = 'SET_CONTESTS';
export const CREATE_CONTEST = 'CREATE_CONTEST';

export const GET_TASK = 'GET_TASK';
export const SET_TASK = 'SET_TASK';
export const GET_TASKS = 'GET_TASKS';
export const SET_TASKS = 'SET_TASKS';
export const CREATE_TASK = 'CREATE_TASK';

export const ADD_TASK_IO = 'ADD_TASK_IO';
export const RESET_TASK_IOS = 'RESET_TASK_IOS';

export const SUBMIT_SOLUTION = 'SUBMIT_SOLUTION';
export const GET_SOLUTIONS_FOR_CONTEST = 'GET_SOLUTIONS_FOR_CONTEST';
export const SET_SOLUTIONS = 'SET_SOLUTIONS';

export const REGISTER_USER = 'REGISTER_USER';
export const AUTHENTICATE_USER = 'AUTHENTICATE_USER';
export const GET_CURRENT_USER = 'GET_CURRENT_USER';
export const SET_CURRENT_USER = 'SET_CURRENT_USER';
export const GET_USERS = 'GET_USERS';
export const SET_USERS = 'SET_USERS';

export const CREATE_TEAM = 'CREATE_TEAM';
export const GET_TEAMS = 'GET_TEAMS';
export const SET_TEAMS = 'SET_TEAMS';

export const GET_TEAM_MEMBERS = 'GET_TEAM_MEMBERS';
export const SET_TEAM_MEMBERS = 'SET_TEAM_MEMBERS';
export const DELETE_MEMBER = 'DELETE_MEMBER';

export const INVITE_USER = 'INVITE USER';
export const GET_INVITES_FOR_TEAM = 'GET_INVITES_FOR_TEAM';
export const SET_INVITES_FOR_TEAM = 'SET_INVITES_FOR_TEAM';
export const GET_INVITES_FOR_CONTEST = 'GET_INVITES_FOR_CONTEST';
export const SET_INVITES_FOR_CONTEST = 'SET_INVITES_FOR_CONTEST';
export const ACCEPT_INVITE = 'ACCEPT_INVITE';
export const DECLINE_INVITE = 'DECLINE_INVITE';

export const ADD_TOAST = 'ADD_TOAST';
export const REMOVE_FIRST_TOAST = 'REMOVE_FIRST_TOAST';


export function getContest(contestId) {
    return {
        type: GET_CONTEST,
        payload: { contestId }
    }
}


export function setContest(contest) {
    return {
        type: SET_CONTEST,
        payload: { contest }
    }
}


export function getContests() {
    return {
        type: GET_CONTESTS,
        payload: {}
    }
}

export function setContests(contests) {
    return {
        type: SET_CONTESTS,
        payload: { contests }
    }
}

export function createContest(contestData) {
    return {
        type: CREATE_CONTEST,
        payload: { contestData }
    }
}


export function getTask(contestId, taskId) {
    return {
        type: GET_TASK,
        payload: { taskId, contestId }
    }
}


export function setTask(task) {
    return {
        type: SET_TASK,
        payload: { task }
    }
}


export function getTasks(contestId) {
    return {
        type: GET_TASKS,
        payload: { contestId }
    }
}

export function setTasks(tasks) {
    return {
        type: SET_TASKS,
        payload: { tasks }
    }
}

export function createTask(contestId, taskName, description, maxCPU, maxMemory, taskIOs) {
    return {
        type: CREATE_TASK,
        payload: { contestId, taskName, description, maxCPU, maxMemory, taskIOs }
    }
}

export function addTaskIO(taskIO, inputRef, outputRef) {
    return {
        type: ADD_TASK_IO,
        payload: { taskIO, inputRef, outputRef }
    }
}

export function resetTaskIOs() {
    return {
        type: RESET_TASK_IOS,
        payload: {}
    }
}

export function submitSolution(taskId, code, language) {
    return {
        type: SUBMIT_SOLUTION,
        payload: {
            taskId, code, language
        }
    }
}

export function registerUser(userData) {
    return {
        type: REGISTER_USER,
        payload: { userData }
    }
}

export function authenticateUser(userData) {
    return {
        type: AUTHENTICATE_USER,
        payload: { userData }
    }
}


export function getCurrentUser() {
    return {
        type: GET_CURRENT_USER,
        payload: {}
    }
}


export function setCurrentUser(user) {
    return {
        type: SET_CURRENT_USER,
        payload: { user }
    }
}


export function createTeam(teamData) {
    return {
        type: CREATE_TEAM,
        payload: { teamData }
    }
}


export function getTeams(contestId) {
    return {
        type: GET_TEAMS,
        payload: { contestId }
    }
}


export function setTeams(teams) {
    return {
        type: SET_TEAMS,
        payload: { teams }
    }
}


export function getTeamMembers(contestId, teamId) {
    return {
        type: GET_TEAM_MEMBERS,
        payload: { contestId, teamId }
    }
}


export function setTeamMembers(teamMembers) {
    return {
        type: SET_TEAM_MEMBERS,
        payload: { teamMembers }
    }
}


export function deleteMember(memberId) {
    return {
        type: DELETE_MEMBER,
        payload: { memberId }
    }
}


export function inviteUser(inviteData) {
    return {
        type: INVITE_USER,
        payload: { inviteData }
    }
}


export function getUsers() {
    return {
        type: GET_USERS,
        payload: {}
    }
}


export function setUsers(users) {
    return {
        type: SET_USERS,
        payload: { users }
    }
}


export function getInvitesForTeam(contestId, teamId) {
    return {
        type: GET_INVITES_FOR_TEAM,
        payload: {
            contestId, teamId
        }
    }
}


export function setInvitesForTeam(invitesForTeam) {
    return {
        type: SET_INVITES_FOR_TEAM,
        payload: { invitesForTeam }
    }
}


export function getInvitesForContest(contestId) {
    return {
        type: GET_INVITES_FOR_CONTEST,
        payload: { contestId }
    }
}


export function setInvitesForContest(invitesForContest) {
    return {
        type: SET_INVITES_FOR_CONTEST,
        payload: { invitesForContest }
    }
}


export function acceptInvite(inviteId) {
    return {
        type: ACCEPT_INVITE,
        payload: { inviteId }
    }
}


export function declineInvite(inviteId) {
    return {
        type: DECLINE_INVITE,
        payload: { inviteId }
    }
}


export function addToast(toastType, message) {
    return {
        type: ADD_TOAST,
        payload: { type: toastType, message }
    }
}


export function removeFirstToast() {
    return {
        type: REMOVE_FIRST_TOAST,
        payload: {}
    }
}


export function getSolutionsForContest(contestId) {
    return {
        type: GET_SOLUTIONS_FOR_CONTEST,
        payload: { contestId }
    }
}


export function setSolutions(solutions) {
    return {
        type: SET_SOLUTIONS,
        payload: { solutions }
    }
}

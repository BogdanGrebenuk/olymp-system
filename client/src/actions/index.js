export const GET_CONTEST = 'GET_CONTEST';
export const SET_CONTEST = 'SET_CONTEST';
export const GET_CONTESTS = 'GET_CONTESTS';
export const SET_CONTESTS = 'SET_CONTESTS';
export const CREATE_CONTEST = 'CREATE_CONTEST';

export const GET_TASKS = 'GET_TASKS';
export const SET_TASKS = 'SET_TASKS';
export const CREATE_TASK = 'CREATE_TASK';

export const ADD_TASK_IO = 'ADD_TASK_IO';
export const RESET_TASK_IOS = 'RESET_TASK_IOS';

export const SUBMIT_SOLUTION = 'SUBMIT_SOLUTION';


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

export function createContest(contestName, contestDescription, imageData) {
    return {
        type: CREATE_CONTEST,
        payload: { contestName, contestDescription, imageData }
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

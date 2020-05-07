import { all, put, call, takeEvery } from 'redux-saga/effects';

import {
    setContests,
    setTasks,
    setContest
} from '../actions';

import {
    GET_CONTEST,
    GET_CONTESTS,
    CREATE_CONTEST,
    GET_TASKS,
    CREATE_TASK,
    SUBMIT_SOLUTION,
    REGISTER_USER,
    AUTHENTICATE_USER
} from "../actions";

import {
    fetchContestService,
    fetchContestsService,
    createContestService,
    fetchTasksService,
    createTaskService,
    submitSolutionService,
    registerUserService,
    authenticateUserService
} from '../services';


function* createContest(action) {
    yield call(
        createContestService,
        action.payload.contestName,
        action.payload.contestDescription,
        action.payload.imageData
    );
}


function* fetchContest(action) {
    const { data } = yield call(
        fetchContestService,
        action.payload.contestId
    );
    const { contest } = data;
    yield put(setContest(contest));
}


function* fetchContests(action) {
    const { data } = yield call(fetchContestsService);
    const { contests } = data;
    yield put(setContests(contests));
}


function* fetchTasks(action) {
    const { data } = yield call(fetchTasksService, action.payload.contestId);
    const { tasks } = data;
    yield put(setTasks(tasks));
}


function* createTask(action) {
    yield call(
        createTaskService,
        action.payload.contestId,
        action.payload.taskName,
        action.payload.description,
        action.payload.maxCPU,
        action.payload.maxMemory,
        action.payload.taskIOs
    );
}


function* submitSolution(action) {
    yield call(
        submitSolutionService,
        action.payload.taskId,
        action.payload.code,
        action.payload.language
    );
}


function* registerUser(action) {
    const response = yield call(
        registerUserService,
        action.payload.userData
    );
    if (response.status === 200) {
        window.location.href = '/authenticate'; // TODO: investigate how to do it correct
    }
}


function* authenticateUser(action) {
   const response = yield call(
        authenticateUserService,

        action.payload.userData
    );

   if (response.status === 200) {
       const { data } = response;
       const { token } = data;
       localStorage.setItem('token', token);
       window.location.href = '/contests';
   }
}


function* watchFetchContest() {
    yield takeEvery(GET_CONTEST, fetchContest);
}


function* watchFetchContests() {
    yield takeEvery(GET_CONTESTS, fetchContests);
}


function* watchCreateContest() {
    yield takeEvery(CREATE_CONTEST, createContest);
}


function* watchFetchTasks() {
    yield takeEvery(GET_TASKS, fetchTasks);
}


function* watchCreateTask() {
    yield takeEvery(CREATE_TASK, createTask)
}


function* watchSubmitSolution() {
    yield takeEvery(SUBMIT_SOLUTION, submitSolution);
}


function* watchRegisterUser(){
    yield takeEvery(REGISTER_USER, registerUser);
}


function* watchAuthenticateUser() {
    yield takeEvery(AUTHENTICATE_USER, authenticateUser);
}


export default function* rootSaga() {
    yield all([
        watchFetchContest(),
        watchFetchContests(),
        watchCreateContest(),
        watchFetchTasks(),
        watchCreateTask(),
        watchSubmitSolution(),
        watchRegisterUser(),
        watchAuthenticateUser()
    ]);
}

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
    SUBMIT_SOLUTION
} from "../actions";

import {
    fetchContestService,
    fetchContestsService,
    createContestService,
    fetchTasksService,
    createTaskService,
    submitSolutionService
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


export default function* rootSaga() {
    yield all([
        watchFetchContest(),
        watchFetchContests(),
        watchCreateContest(),
        watchFetchTasks(),
        watchCreateTask(),
        watchSubmitSolution()
    ]);
}

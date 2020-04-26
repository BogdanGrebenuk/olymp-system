import {all, put, call} from 'redux-saga/effects';

import { setContests } from '../actions';
import { fetchContestsService } from '../services';


function* fetchContests(action) {
    const { data } = yield call(fetchContestsService);
    const { contests } = data;
    yield put(setContests(contests));
}


export default function* rootSaga() {
    yield all([
        fetchContests()
    ]);
}

import { all, put, call, takeEvery } from 'redux-saga/effects';

import {
    setContests,
    setTasks,
    setContest,
    setTask,
    setCurrentUser,
    setTeams,
    setTeamMembers,
    setUsers,
    setInvitesForTeam,
    setInvitesForContest, DECLINE_INVITE
} from '../actions';

import {
    GET_CONTEST,
    GET_CONTESTS,
    CREATE_CONTEST,
    GET_TASKS,
    GET_TASK,
    CREATE_TASK,
    SUBMIT_SOLUTION,
    REGISTER_USER,
    AUTHENTICATE_USER,
    GET_CURRENT_USER,
    CREATE_TEAM,
    GET_TEAMS,
    GET_TEAM_MEMBERS,
    DELETE_MEMBER,
    INVITE_USER,
    GET_USERS,
    GET_INVITES_FOR_TEAM,
    GET_INVITES_FOR_CONTEST,
    ACCEPT_INVITE
} from "../actions";

import {
    fetchContestService,
    fetchContestsService,
    fetchTaskService,
    createContestService,
    fetchTasksService,
    createTaskService,
    submitSolutionService,
    registerUserService,
    authenticateUserService,
    fetchCurrentUserService,
    createTeamService,
    fetchTeamsService,
    fetchTeamMembersService,
    deleteMemberService,
    inviteUserService,
    getUsersService,
    getInvitesForTeamService,
    getInvitesForContestService,
    acceptInviteService,
    declineInviteService
} from '../services';


function* createContest(action) {
    yield call(
        createContestService,
        action.payload.contestData
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


function* fetchTask(action) {
    const { data } = yield call(
        fetchTaskService,
        action.payload.contestId,
        action.payload.taskId
    );
    const { task } = data;
    yield put(setTask(task));
}


function* fetchTasks(action) {
    try{
        const { data } = yield call(fetchTasksService, action.payload.contestId);
        const { tasks } = data;
        yield put(setTasks(tasks));
    } catch (e) {
        // TODO: toastr!
    }

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


function* fetchCurrentUser(action) {
    // try {
        const { data } = yield call(fetchCurrentUserService);
        const { user } = data;
        yield put(setCurrentUser(user));
    // } catch (e) {
    //     window.location.href = '/authenticate';
    // }
}


function* fetchTeams(action) {
    const { data } = yield call(fetchTeamsService, action.payload.contestId)
    const { teams } = data;
    yield put(setTeams(teams));
}


function* createTeam(action) {
    yield call(createTeamService, action.payload.teamData);
}


function* fetchTeamMembers(action) {
    const { data } = yield call(
        fetchTeamMembersService,
        action.payload.contestId,
        action.payload.teamId
    );
    const { members } = data;
    yield put(setTeamMembers(members));
}


function* deleteMember(action) {
    yield call(deleteMemberService, action.payload.memberId);
}


function* inviteUser(action) {
    yield call(inviteUserService, action.payload.inviteData);
}


function* fetchUsers(action) {
    const { data } = yield call(getUsersService);
    const { users } = data;
    yield put(setUsers(users));
}


function* fetchInvitesForTeam(action) {
    const { data } = yield call(
        getInvitesForTeamService,
        action.payload.contestId,
        action.payload.teamId
        );
    const { invites } = data;
    yield put(setInvitesForTeam(invites));
}


function* fetchInvitesForContest(action) {
    const { data } = yield call(
        getInvitesForContestService,
        action.payload.contestId
    );
    const { invites } = data;
    yield put(setInvitesForContest(invites));
}


function* acceptInvite(action) {
    yield call(
        acceptInviteService,
        action.payload.inviteId
    )
}


function* declineInvite(action) {
    yield call(
        declineInviteService,
        action.payload.inviteId
    )
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


function* watchFetchTask() {
    yield takeEvery(GET_TASK, fetchTask);
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


function* watchFetchCurrentUser() {
    yield takeEvery(GET_CURRENT_USER, fetchCurrentUser);
}


function* watchCreateTeam() {
    yield takeEvery(CREATE_TEAM, createTeam)
}


function* watchFetchTeams() {
    yield takeEvery(GET_TEAMS, fetchTeams);
}


function* watchFetchTeamMembers() {
    yield takeEvery(GET_TEAM_MEMBERS, fetchTeamMembers)
}


function* watchDeleteMember() {
    yield takeEvery(DELETE_MEMBER, deleteMember)
}


function* watchInviteUser() {
    yield takeEvery(INVITE_USER, inviteUser)
}


function* watchFetchUsers() {
    yield takeEvery(GET_USERS, fetchUsers);
}


function* watchFetchInvitesForTeam() {
    yield takeEvery(GET_INVITES_FOR_TEAM, fetchInvitesForTeam)
}


function* watchFetchInvitesForContest() {
    yield takeEvery(GET_INVITES_FOR_CONTEST, fetchInvitesForContest);
}


function* watchAcceptInvite() {
    yield takeEvery(ACCEPT_INVITE, acceptInvite);
}


function* watchDeclineInvite() {
    yield takeEvery(DECLINE_INVITE, declineInvite);
}



export default function* rootSaga() {
    yield all([
        watchFetchContest(),
        watchFetchContests(),
        watchCreateContest(),
        watchFetchTask(),
        watchFetchTasks(),
        watchCreateTask(),
        watchSubmitSolution(),
        watchRegisterUser(),
        watchAuthenticateUser(),
        watchFetchCurrentUser(),
        watchCreateTeam(),
        watchFetchTeams(),
        watchFetchTeamMembers(),
        watchDeleteMember(),
        watchInviteUser(),
        watchFetchUsers(),
        watchFetchInvitesForTeam(),
        watchFetchInvitesForContest(),
        watchAcceptInvite(),
        watchDeclineInvite()
    ]);
}

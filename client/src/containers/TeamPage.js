import { connect } from 'react-redux';

import TeamPageComponent from "../components/TeamPage";

import {getContest, getTeams} from '../actions';


const onRefreshTeams = (dispatch, contestId) => () => {
    dispatch(getTeams(contestId));
}

const onRefreshContest = (dispatch, contestId) => () => {
    dispatch(getContest(contestId));
}


const mapStateToProps = (state, ownProps) => {
    return {
        contest: state.contests[ownProps.match.params.contestId],
        team: state.teams[ownProps.match.params.teamId],
        user: state.currentUser
    }
}


const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onRefreshTeams: onRefreshTeams(dispatch, ownProps.match.params.contestId),
        onRefreshContest: onRefreshContest(dispatch, ownProps.match.params.contestId)
    }
}


const TeamPageContainer = connect(mapStateToProps, mapDispatchToProps)(TeamPageComponent);


export default TeamPageContainer;

import { connect } from 'react-redux';

import TeamPageComponent from "../components/TeamPage";

import {getTeams} from '../actions';


const onRefreshTeams = (dispatch, contestId) => () => {
    dispatch(getTeams(contestId));
}


const mapStateToProps = (state, ownProps) => {
    return {
        team: state.teams[ownProps.match.params.teamId],
        user: state.currentUser
    }
}


const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onRefreshTeams: onRefreshTeams(dispatch, ownProps.match.params.contestId)
    }
}


const TeamPageContainer = connect(mapStateToProps, mapDispatchToProps)(TeamPageComponent);


export default TeamPageContainer;

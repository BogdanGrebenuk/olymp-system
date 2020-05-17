import { connect } from 'react-redux';

import MemberListComponent from "../components/MemberList";

import {getTeamMembers} from '../actions';


const onFetchTeamMembers = dispatch => (contestId, teamId) => {
    dispatch(getTeamMembers(contestId, teamId));
}


const mapStateToProps = (state, ownProps) => {
    return {
        team: ownProps.team,
        members: Object.values(state.teamMembers)
    }
}


const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onFetchTeamMembers: onFetchTeamMembers(dispatch)
    }
}


const MemberListContainer = connect(mapStateToProps, mapDispatchToProps)(MemberListComponent);


export default MemberListContainer;

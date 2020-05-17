import { connect } from 'react-redux';

import InviteListComponent from "../components/InviteList";

import {getInvitesForTeam} from '../actions';


const onFetchInvites = dispatch => (contestId, teamId) => {
    dispatch(getInvitesForTeam(contestId, teamId));
}


const mapStateToProps = (state, ownProps) => {
    return {
        team: ownProps.team,
        invites: Object.values(state.invitesForTeam)
    }
}


const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onFetchInvites: onFetchInvites(dispatch)
    }
}


const InviteListContainer = connect(mapStateToProps, mapDispatchToProps)(InviteListComponent);


export default InviteListContainer;

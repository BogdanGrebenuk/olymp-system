import { connect } from 'react-redux';

import TeamItemComponent from "../components/TeamItem";

import {acceptInvite, declineInvite} from '../actions';


const onAcceptInvite = dispatch => inviteId => {
    dispatch(acceptInvite(inviteId));
}


const onDeclineInvite = dispatch => inviteId => {
    dispatch(declineInvite(inviteId));
}


const mapDispatchToProps = dispatch => {
    return {
        onAcceptInvite: onAcceptInvite(dispatch),
        onDeclineInvite: onDeclineInvite(dispatch)
    }
}


const TeamItemContainer = connect(null, mapDispatchToProps)(TeamItemComponent);


export default TeamItemContainer;

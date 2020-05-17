import { connect } from 'react-redux';

import InviteBlockComponent from "../components/InviteBlock";

import { inviteUser } from '../actions';


const onInviteUser = dispatch => inviteData => {
    dispatch(inviteUser(inviteData));
}


const mapDispatchToProps = dispatch => {
    return {
        onInviteUser: onInviteUser(dispatch)
    }
}


const mapStateToProps = (state, ownProps) => {
    return {
        user: state.currentUser,
        team: ownProps.team
    }
}


const InviteBlockContainer = connect(mapStateToProps, mapDispatchToProps)(InviteBlockComponent);


export default InviteBlockContainer;

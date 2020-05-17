import { connect } from 'react-redux';

import InviteItemComponent from "../components/InviteItem";

import {deleteMember} from '../actions';


const getMember = (state, member) => {
    let temp;
    temp = {...member};
    console.log(member)
    console.log(state)
    const user = state.users[member.userId];
    temp['email'] = user.email;
    temp['firstName'] = user.firstName;
    temp['lastName'] = user.lastName;
    return temp;
}


const onDeleteMember = dispatch => (memberId) => {
    dispatch(deleteMember(memberId));
}


const mapStateToProps = (state, ownProps) => {
    return {
        invite: getMember(state, ownProps.invite)
    }
}


const mapDispatchToProps = dispatch => {
    return {
        onDeleteMember: onDeleteMember(dispatch)
    }
}


const InviteItemContainer = connect(mapStateToProps, mapDispatchToProps)(InviteItemComponent);


export default InviteItemContainer;

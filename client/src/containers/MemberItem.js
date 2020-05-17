import { connect } from 'react-redux';

import MemberItemComponent from "../components/MemberItem";

import {deleteMember, getTeamMembers} from '../actions';


const getMember = (state, member) => {
    let temp;
    temp = {...member};
    const user = state.users[member.userId];
    temp['email'] = user.email;
    temp['firstName'] = user.firstName;
    temp['lastName'] = user.lastName;
    return temp;
}


const onDeleteMember = dispatch => (memberId) => {
    dispatch(deleteMember(memberId));
}


const onFetchTeamMembers = dispatch => (contestId, teamId) => {
    dispatch(getTeamMembers(contestId, teamId));
}


const mapStateToProps = (state, ownProps) => {
    return {
        user: state.currentUser,
        team: ownProps.team,
        member: getMember(state, ownProps.member)
    }
}


const mapDispatchToProps = dispatch => {
    return {
        onDeleteMember: onDeleteMember(dispatch),
        onFetchTeamMembers: onFetchTeamMembers(dispatch)
    }
}


const MemberItemContainer = connect(mapStateToProps, mapDispatchToProps)(MemberItemComponent);


export default MemberItemContainer;

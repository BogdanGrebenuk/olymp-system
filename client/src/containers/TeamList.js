import { connect } from 'react-redux';

import TeamListComponent from "../components/TeamList";
import {getTeams, getInvitesForContest} from "../actions";


const onFetchTeams = dispatch => contestId => {
    dispatch(getTeams(contestId));
}


const onFetchInvitesForContest = dispatch => contestId => {
    dispatch(getInvitesForContest(contestId));
}


const mapStateToProps = (state, ownProps) => {
    return {
        teams: Object.values(state.teams),
        contest: ownProps.contest,
        invites: Object.values(state.invitesForContest),
        user: state.currentUser
    }
}


const mapDispatchToProps = dispatch => {
    return {
        onFetchTeams: onFetchTeams(dispatch),
        onFetchInvitesForContest: onFetchInvitesForContest(dispatch)
    }
}


const TeamListContainer = connect(mapStateToProps, mapDispatchToProps)(TeamListComponent);


export default TeamListContainer;

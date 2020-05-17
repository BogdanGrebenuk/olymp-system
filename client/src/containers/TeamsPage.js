import { connect } from 'react-redux';

import TeamsPageComponent from "../components/TeamsPage";
import {getContest, getTeams} from "../actions";


const onRefreshContest = (dispatch, contestId) => () => {
    dispatch(getContest(contestId));
}


const mapStateToProps = (state, ownProps) => {
    return {
        user: state.currentUser,
        contest: state.contests[ownProps.match.params.contestId]
    }
}


const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onRefreshContest: onRefreshContest(dispatch, ownProps.match.params.contestId)
    }
}


const TeamsPageContainer = connect(mapStateToProps, mapDispatchToProps)(TeamsPageComponent);


export default TeamsPageContainer;

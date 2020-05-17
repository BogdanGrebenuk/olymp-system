import { connect } from 'react-redux';

import CreateTeamComponent from "../components/CreateTeam";
import {getContest, createTeam} from "../actions";


const onCreateTeam = dispatch => teamData => {
    dispatch(createTeam(teamData));
}


const onRefreshContest = (dispatch, contestId) => () => {
    dispatch(getContest(contestId));
}


const mapStateToProps = (state, ownProps) => {
    return {
        contest: state.contests[ownProps.match.params.contestId]
    }
}


const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onCreateTeam: onCreateTeam(dispatch),
        onRefreshContest: onRefreshContest(dispatch, ownProps.match.params.contestId)
    }
}


const CreateTeamContainer = connect(mapStateToProps, mapDispatchToProps)(CreateTeamComponent);

export default CreateTeamContainer;

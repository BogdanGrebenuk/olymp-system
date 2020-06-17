import { connect } from 'react-redux';

import LeaderBoardComponent from "../components/LeaderBoard";
import {getContest} from "../actions";


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
        onRefreshContest: onRefreshContest(dispatch, ownProps.match.params.contestId)
    }
}


const LeaderBoardContainer = connect(mapStateToProps, mapDispatchToProps)(LeaderBoardComponent);


export default LeaderBoardContainer;

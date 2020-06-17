import { connect } from 'react-redux';

import LeaderBoardTableComponent from "../components/LeaderBoardTable";
import {getLeaderBoard} from "../actions";


const onFetchLeaderBoard = dispatch => contestId => {
    dispatch(getLeaderBoard(contestId));
}


const mapStateToProps = (state, ownProps) => {
    return {
        leaderBoard: state.leaderBoard
    }
}


const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onFetchLeaderBoard: onFetchLeaderBoard(dispatch)
    }
}


const LeaderBoardTableContainer = connect(mapStateToProps, mapDispatchToProps)(LeaderBoardTableComponent);


export default LeaderBoardTableContainer;

import { connect } from 'react-redux';

import SolutionsTableRowComponent from "../components/SolutionsTableRow";
import {getTask, getTeams} from "../actions";


const onRefreshTeams = (dispatch, contestId) => () => {
    dispatch(getTeams(contestId));
}


const onRefreshTask = (dispatch, contestId, taskId) => () => {
    dispatch(getTask(contestId, taskId));
}


const mapStateToProps = (state, ownProps) => {
    return {
        solution: ownProps.solution,
        task: state.tasks[ownProps.solution.taskId],
        team: state.teams[ownProps.solution.teamId]
    }
}


const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onRefreshTeams: onRefreshTeams(dispatch, ownProps.contest.id),
        onRefreshTask: onRefreshTask(dispatch, ownProps.contest.id, ownProps.solution.taskId)
    }
}


const SolutionsTableRowContainer = connect(mapStateToProps, mapDispatchToProps)(SolutionsTableRowComponent);


export default SolutionsTableRowContainer;

import { connect } from 'react-redux';

import TaskPageComponent from "../components/TaskPage";
import {getContest, getTask, submitSolution} from "../actions";


const onRefreshTask = (dispatch, contestId, taskId) => () => {
    dispatch(getTask(contestId, taskId));
}


const onRefreshContest = (dispatch, contestId) => () => {
    dispatch(getContest(contestId));
}


const onSubmitSolution = dispatch => (taskId, code, language) => {
    dispatch(submitSolution(taskId, code, language));
}


const mapStateToProps = (state, ownProps) => {
    return {
        contest: state.contests[ownProps.match.params.contestId],
        task: state.tasks[ownProps.match.params.taskId],
        user: state.currentUser
    };
}


const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onSubmitSolution: onSubmitSolution(dispatch),
        onRefreshTask: onRefreshTask(
            dispatch,
            ownProps.match.params.contestId,
            ownProps.match.params.taskId
            ),
        onRefreshContest: onRefreshContest(dispatch, ownProps.match.params.contestId)
    }
}


const TaskPageContainer = connect(mapStateToProps, mapDispatchToProps)(TaskPageComponent);

export default TaskPageContainer;
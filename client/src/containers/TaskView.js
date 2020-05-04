import { connect } from 'react-redux';

import TaskPageComponent from "../components/TaskPage";
import { submitSolution } from "../actions";


const onSubmitSolution = dispatch => (taskId, code, language) => {
    dispatch(submitSolution(taskId, code, language));
}


const mapStateToProps = (state, ownProps) => {
    return {
        contest: ownProps.contest, //state.contests[ownProps.match.params.contestId],
        task: ownProps.task //state.tasks[ownProps.match.params.taskId]
    };
}


const mapDispatchToProps = dispatch => {
    return {
        onSubmitSolution: onSubmitSolution(dispatch)
    }
}


const TaskPageContainer = connect(mapStateToProps, mapDispatchToProps)(TaskPageComponent);

export default TaskPageContainer;
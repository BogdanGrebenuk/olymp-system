import { connect } from 'react-redux';

import TaskListComponent from "../components/TaskList";

import { getTasks } from '../actions';


const onFetchContestTasks = dispatch => (contestId) => {
    dispatch(getTasks(contestId));
}


const mapStateToProps = (state, ownProps) => {
    return {
        tasks: Object.values(state.tasks),
        contest: ownProps.contest
    }
}


const mapDispatchToProps = dispatch => {
    return {
        onFetchContestTasks: onFetchContestTasks(dispatch)
    }
}


const TaskListContainer = connect(mapStateToProps, mapDispatchToProps)(TaskListComponent);


export default TaskListContainer;

import { connect } from "react-redux";

import CreateTaskComponent from "../components/CreateTask";
import {createTask, getContest} from '../actions';


const onCreateTask = dispatch => (contestId, taskName, description, maxCPU, maxMemory, taskIOs) => {
    dispatch(createTask(contestId, taskName, description, maxCPU, maxMemory, taskIOs));
}


const onRefreshContest = (dispatch, contestId) => () => {
    dispatch(getContest(contestId));
}


const mapStateToProps = (state, ownProps) => {
    return {
        taskIOs: state.taskIOs,
        contest: state.contests[ownProps.match.params.contestId]
    }
}


const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onCreateTask: onCreateTask(dispatch),
        onRefreshContest: onRefreshContest(dispatch, ownProps.match.params.contestId)
    }
}


const CreateTaskContainer = connect(mapStateToProps, mapDispatchToProps)(CreateTaskComponent);


export default CreateTaskContainer;
import React from 'react';
import { connect } from 'react-redux';

import TaskIOListComponent from "../components/TaskIOList";
import { addTaskIO, resetTaskIOs } from '../actions';


const onAddTaskIO = dispatch => () => {
    const inputRef = React.createRef();
    const outputRef = React.createRef();
    const taskIO = (
        <div>
            <textarea ref={inputRef}/>
            <textarea ref={outputRef}/>
        </div>
    )
    dispatch(addTaskIO(taskIO, inputRef, outputRef));
}


const onResetTaskIOs = dispatch => () => {
    dispatch(resetTaskIOs())
}


const mapStateToProps = state => {
    return {
        taskIOs: state.taskIOs
    }
};


const mapDispatchToProps = dispatch => {
    return {
        onAddTaskIO: onAddTaskIO(dispatch),
        onResetTaskIOs: onResetTaskIOs(dispatch)
    }
}


const TaskIOListContainer = connect(mapStateToProps, mapDispatchToProps)(TaskIOListComponent);


export default TaskIOListContainer;

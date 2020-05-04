import React, { Component } from 'react';
import { withRouter } from "react-router";

class TaskItem extends Component {

    onTaskSelected() {
        const contestId = this.props.contest.id;
        const taskId = this.props.task.id;
        this.props.history.push(
            `/contests/${contestId}/tasks/${taskId}/view`
        );
    }

    render() {
        const { task } = this.props;
        return (
            <div onClick={this.onTaskSelected.bind(this)}>
                <div> Task name (implement) </div>
                <div> {task.description} </div>
            </div>
        )
    }
}


export default withRouter(TaskItem);

import React, { Component } from 'react';
import { withRouter } from "react-router";

import icon from "../assets/images/task.png"

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
            <div className="task-block" onClick={this.onTaskSelected.bind(this)}>
                <img src={icon} />
                <div>
                    <h3> {task.name} </h3>
                    <p> {task.description} </p>
                </div>
            </div>
        )
    }
}


export default withRouter(TaskItem);

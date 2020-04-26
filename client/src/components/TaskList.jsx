import React, { Component } from 'react';

import TaskItem from "./TaskItem";


class TaskList extends Component {

    componentDidMount() {
        this.props.onFetchContestTasks()
    }

    render() {
        const { tasks } = this.props;
        return (
            <div>
                {
                    tasks.map(task => <TaskItem key={task.id} task={task}/>)
                }
            </div>
        )
    }
}


export default TaskList;
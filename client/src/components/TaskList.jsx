import React, { Component } from 'react';

import TaskItem from "./TaskItem";
import '../App.css';


class TaskList extends Component {

    componentDidMount() {
        this.props.onFetchContestTasks(this.props.contest.id);
    }

    render() {
        const { tasks, contest } = this.props;
        return (
            <div className='task-list-block flex-container-column'>
                {
                    tasks.map(task => <TaskItem key={task.id} task={task} contest={contest}/>)
                }
            </div>
        )
    }
}


export default TaskList;
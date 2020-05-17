import React, { Component } from 'react';

import TaskItem from "./TaskItem";
import '../assets/styles/App.scss';


class TaskList extends Component {
    constructor(props) {
        super(props);
    }

    componentDidMount() {
        this.props.onFetchContestTasks(this.props.contest.id);
    }

    render() {
        const { tasks, contest } = this.props;

        return (
            <div className='flex-container-column'>
                {
                    tasks.map(task => <TaskItem key={task.id} task={task} contest={contest} />)
                }
            </div>
        )
    }
}


export default TaskList;
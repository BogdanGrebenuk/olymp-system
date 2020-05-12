import React, { Component } from 'react';

import TaskItem from "./TaskItem";
import '../assets/styles/App.scss';


class TaskList extends Component {

    componentDidMount() {
        //this.props.onFetchContestTasks(this.props.contest.id);
    }

    render() {
        const { tasks, contest } = this.props;
        // const tasks = [{ id: 1, description: "description" }];
        // const contest = { id: 1 };
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
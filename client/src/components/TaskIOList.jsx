import React, { Component } from 'react';


class TaskIOList extends Component {

    componentDidMount() {
        this.props.onResetTaskIOs();
    }

    componentWillUnmount() {
        this.props.onResetTaskIOs();
    }

    addTaskIOButtonClicked() {
        this.props.onAddTaskIO();
    }

    render() {
        const { taskIOs } = this.props;
        return (
            <div>
                {taskIOs.map((taskIO, i) => <div key={i}> {taskIO.taskIO} </div>)}
                <button onClick={this.addTaskIOButtonClicked.bind(this)}>
                    Add task IO
                </button>
            </div>
        );
    }

}


export default TaskIOList;
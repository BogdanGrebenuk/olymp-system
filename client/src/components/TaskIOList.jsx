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
            <>
                <div className="io-block">
                    {taskIOs.map((taskIO, i) => <div key={i}> {taskIO.taskIO} </div>)}
                </div>
                <button className="io-button" onClick={this.addTaskIOButtonClicked.bind(this)}>
                    Add task IO
                </button>
            </>
        );
    }

}


export default TaskIOList;
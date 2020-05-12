import React, { Component } from 'react';

import TaskIOListContainer from "../containers/TaskIOList.jsx"; // TODO: doesn't work without jsx ext

import "../assets/styles/CreateTask.scss"

class CreateTask extends Component {

    constructor(props) {
        super(props);
        this.taskNameInput = React.createRef();
        this.descriptionInput = React.createRef();
        this.maxCpuInput = React.createRef();
        this.maxMemoryInput = React.createRef();

        this.isRefreshed = false;
    }

    createTaskButtonClicked() {
        const taskName = this.taskNameInput.current.value.trim();
        const description = this.descriptionInput.current.value.trim();
        const maxCPU = this.maxCpuInput.current.value.trim();
        const maxMemory = this.maxMemoryInput.current.value.trim();
        if (
            [taskName, description, maxCPU, maxMemory].some(
                e => e.length === 0
            )
        ) {
            return alert('some of the fields isn\'t filled!')
        }

        const { taskIOs } = this.props;
        const taskIOValues = taskIOs.map(taskIO => [
            taskIO.inputRef.current.value.trim(),
            taskIO.outputRef.current.value.trim()
        ]);

        if (
            taskIOValues.length === 0
            || taskIOValues.some(
                taskIO => (
                    taskIO[0].length === 0
                    ||
                    taskIO[1].length === 0
                )
            )
        ) {
            return alert('fill all task ios fields!')
        }

        this.props.onCreateTask(
            this.props.contest.id,
            taskName,
            description,
            maxCPU,
            maxMemory,
            taskIOValues
        );
    }

    render() {

        // const { contest } = this.props;

        // if (typeof contest === 'undefined') {
        //     if (this.isRefreshed === true) {
        //         return <div> Contest not found! </div>
        //     }
        //     this.isRefreshed = true;
        //     this.props.onRefreshContest();
        //     return <div> Wait... </div>
        // }

        return (
            <div className='page'>
                <h1>Create task</h1>
                <ul className="create-form">
                    <li>
                        <label>Task name <span className="required">*</span></label>
                        <input ref={this.taskNameInput} type="text" className="field-long"/>
                    </li>
                    <li>
                        <label>Description <span className="required">*</span></label>
                        <textarea ref={this.descriptionInput} className="field-long field-textarea"/>
                    </li>
                    <li>
                        <label>Time <span className="required">*</span></label>
                        <input ref={this.maxCpuInput} type='number' className="field-long"/>
                    </li>
                    <li>
                        <label>Memory <span className="required">*</span></label>
                        <input ref={this.maxMemoryInput} type='number' className="field-long"/>
                    </li>
                    <li>
                        <TaskIOListContainer/>
                    </li>
                    <li>
                        <button className="submit-button" onClick={this.createTaskButtonClicked.bind(this)}>
                            Create
                        </button>
                    </li>
                </ul>
            </div>
        )
    }

}


export default CreateTask;

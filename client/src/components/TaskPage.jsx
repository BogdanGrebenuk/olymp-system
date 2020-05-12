import React, { Component } from 'react';

import "../assets/styles/TaskPage.scss"

class TaskPage extends Component {

    constructor(props) {
        super(props);

        this.codeRef = React.createRef();
        this.languageRef = React.createRef();

        this.isContestRefreshed = false;
        this.isTaskRefreshed = false;
    }


    onSubmitClicked() {
        const code = this.codeRef.current.value.trim();
        if (code.length === 0) {
            return alert('the code section is empty!');
        }
        const language = this.languageRef.current.value;
        if (language.length === 0) {
            return alert('you must specify language!');
        }
        this.props.onSubmitSolution(
            this.props.task.id,
            code,
            language
        );
    }

    render() {
        const { task } = this.props;

        const languages = ['','python']; // TODO: fetch from api

        return (
            <div className="page">
                <h1>Name</h1>
                <div className="task-wrap">
                    <p>Description</p>
                    <textarea ref={this.codeRef} rows={20} placeholder={"Your code..."} />
                    <select ref={this.languageRef} placeholder={"Select language..."}>
                        {languages.map((lang, i) => <option key={i} value={lang}> {lang} </option>)}
                    </select>
                    <button onClick={this.onSubmitClicked.bind(this)}> Submit </button>
                </div>
            </div>
        )
    }

}


export default TaskPage;
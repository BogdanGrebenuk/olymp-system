import React, { Component } from 'react';


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
            <div>
                <div> Task name </div>
                <div> {task.description} </div>
                <textarea ref={this.codeRef}/>
                <select ref={this.languageRef}>
                    {languages.map((lang, i) => <option key={i} value={lang}> {lang} </option>)}
                </select>
                <button onClick={this.onSubmitClicked.bind(this)}> Submit </button>
            </div>
        )
    }

}


export default TaskPage;
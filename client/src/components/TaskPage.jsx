import React, { Component } from 'react';

import "../assets/styles/TaskPage.scss"
import {ContestsElement, HomeElement, NavBarElement} from "../utils";
import Header from "./Header";
import {withRouter} from "react-router";


class TaskPage extends Component {

    constructor(props) {
        super(props);

        this.codeRef = React.createRef();
        this.languageRef = React.createRef();
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
        const { user, task } = this.props;

        if (typeof task === 'undefined') {
            this.props.onRefreshTask();
            return <div/>
        }

        let navBarElements = [
            HomeElement,
            ContestsElement,
            new NavBarElement('Contest', `/contests/view/${task.contestId}`),
            new NavBarElement('Task', this.props.match.url),
        ]

        const languages = ['','python']; // TODO: fetch from api

        return (
            <div>
                <Header navBarElements={navBarElements}/>
                <div className="page">
                    <h1>{task.name}</h1>
                    <div className="task-wrap">
                        <p> {task.description} </p>
                        {
                            user.role === 'participant'
                                ? (
                                <div>
                                    <textarea className="code-input" ref={this.codeRef} rows={20} placeholder={"Your code..."} />
                                    <select ref={this.languageRef} placeholder={"Select language..."}>
                                        {languages.map((lang, i) => <option key={i} value={lang}> {lang} </option>)}
                                    </select>
                                    <button onClick={this.onSubmitClicked.bind(this)}> Submit </button>
                                </div>)
                                : null
                        }
                    </div>
                </div>
            </div>
        )
    }

}


export default withRouter(TaskPage);
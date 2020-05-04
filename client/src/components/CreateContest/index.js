import React, { Component } from 'react';

import './styles.css';
import PageDescriptionHeader from "../PageDescriptionHeader";


class CreateContest extends Component {

    constructor(props) {
        super(props);
        this.contestNameInput = React.createRef();
        this.contestDescription = React.createRef()
    }

    createContestButtonClicked() {
        const contestName = this.contestNameInput.current.value.trim();
        if (contestName.length === 0) {
            return alert('Contest name can\'t be empty!');
        }
        const contestDescription = this.contestDescription.current.value.trim();
        if (contestDescription.length === 0) {
            return alert('Contest description can\'t be empty!');
        }
        this.props.onCreateContest(contestName, contestDescription);
    }

    render() {
        return (
            <div className='page'>
                <PageDescriptionHeader description='Create contest'/>
                <ul className="create-form">
                    <li>
                        <label>Contest name <span className="required">*</span></label>
                        <input ref={this.contestNameInput} type="text" className="field-long"/>
                    </li>
                    <li>
                        <label> Description <span className="required">*</span></label>
                        <textarea ref={this.contestDescription} className="field-long field-textarea"/>
                    </li>
                    <li>
                        <button className='submit-button' onClick={this.createContestButtonClicked.bind(this)}> Create</button>
                    </li>
                </ul>
            </div>
        )
    }

}


export default CreateContest;

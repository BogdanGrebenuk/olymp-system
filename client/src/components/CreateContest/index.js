import React, { Component } from 'react';
import ImageUploader from "react-images-upload";

import '../../assets/styles/CreateContest.scss';
import Header from "../Header";

import {HomeElement, ContestsElement, ContestsNewElement} from '../../utils';


class CreateContest extends Component {

    constructor(props) {
        super(props);
        this.contestNameInput = React.createRef();
        this.contestDescription = React.createRef();
        this.maxTeamsInput = React.createRef();
        this.maxParticipantsInTeamInput = React.createRef();
        this.dateOfBeginningInput = React.createRef();
        this.dateOfEndingInput = React.createRef();
        this.selectedImage = null;
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

        const maxTeams = this.maxTeamsInput.current.value.trim();
        if (maxTeams.length === 0) {
            return alert('Specify maximum amount of teams in contest!')
        }

        const maxParticipantsInTeam = this.maxParticipantsInTeamInput.current.value.trim();
        if (maxParticipantsInTeam.length === 0) {
            return alert('Specify maximum amount of participant in team!')
        }

        const beginningDate = this.dateOfBeginningInput.current.value.trim();
        if (beginningDate.length === 0) {
            return alert('Specify date of contest beginning!')
        }

        const endingDate = this.dateOfEndingInput.current.value.trim();
        if (endingDate.length === 0) {
            return alert('Specify date of contest ending!')
        }

        const contestData = {
            name: contestName,
            description: contestDescription,
            maxTeams,
            maxParticipantsInTeam,
            beginningDate: (new Date(beginningDate)).toJSON(),
            endingDate: (new Date(endingDate)).toJSON(),
            image: this.selectedImage
        }

        this.props.onCreateContest(contestData);
    }

    onDrop(pictureFile, pictureDataURL) {
        this.selectedImage = pictureFile[0];
    }

    render() {
        const navBarElements = [HomeElement, ContestsElement, ContestsNewElement];
        return (
            <div>
                <Header navBarElements={navBarElements}/>
                <div className='page'>
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
                            <label> Max teams  <span className="required">*</span></label>
                            <input ref={this.maxTeamsInput} type="number" className="field-long"/>
                        </li>
                        <li>
                            <label> Max participants in a team  <span className="required">*</span></label>
                            <input ref={this.maxParticipantsInTeamInput} type="number" className="field-long"/>
                        </li>
                        <li>
                            <label> Date of beginning  <span className="required">*</span></label>
                            <input ref={this.dateOfBeginningInput} type="datetime-local" className="field-long"/>
                        </li>
                        <li>
                            <label> Date of ending  <span className="required">*</span></label>
                            <input ref={this.dateOfEndingInput} type="datetime-local" className="field-long"/>
                        </li>

                        <ImageUploader
                            withIcon={true}
                            buttonText="Choose image"
                            onChange={this.onDrop.bind(this)}
                            imgExtension={[".jpg", ".gif", ".png", ".gif"]}
                            maxFileSize={5242880}
                            singleImage={true}
                          />
                        <li>
                            <button className='submit-button' onClick={this.createContestButtonClicked.bind(this)}> Create</button>
                        </li>
                    </ul>
                </div>
            </div>
        )
    }

}


export default CreateContest;

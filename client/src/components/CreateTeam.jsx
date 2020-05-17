import React, { Component } from 'react';
import ImageUploader from "react-images-upload";
import {ContestsElement, HomeElement, NavBarElement} from "../utils";

import {withRouter} from "react-router";
import Header from "./Header";


class CreateTeam extends Component {
    constructor(props) {
        super(props);

        this.selectedImage = null;
        this.teamNameInput = React.createRef();
    }

    onDrop(pictureFile, pictureDataURL) {
        this.selectedImage = pictureFile[0];
    }

    onCreateButtonClicked() {
        const teamName = this.teamNameInput.current.value.trim();

        if (teamName.length === 0) {
            return alert('specify name of the team!');
        }

        const teamData = {
            name: teamName,
            // image: this.selectedImage,
            contestId: this.props.contest.id
        }

        this.props.onCreateTeam(teamData)
    }

    render() {
        const { contest } = this.props;

        if (typeof contest === 'undefined') {
            this.props.onRefreshContest();

            return <div/>
        }

        const navBarElements = [
            HomeElement,
            ContestsElement,
            new NavBarElement('Contest', `/contests/view/${contest.id}`),
            new NavBarElement('Teams', `/contests/${contest.id}/teams`),
            new NavBarElement('Create team', this.props.match.url)
        ];

        return (
            <div>
                <Header navBarElements={navBarElements} />
                Team name <input ref={this.teamNameInput}/>
                <ImageUploader
                    withIcon={true}
                    buttonText="Choose image"
                    onChange={this.onDrop.bind(this)}
                    imgExtension={[".jpg", ".gif", ".png", ".gif"]}
                    maxFileSize={5242880}
                    singleImage={true}
                  />
                <button onClick={this.onCreateButtonClicked.bind(this)}> Create team </button>
            </div>
        )
    }
}


export  default withRouter(CreateTeam);

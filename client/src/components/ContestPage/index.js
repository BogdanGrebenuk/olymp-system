import React, { Component } from 'react';
import { withRouter } from "react-router";
import moment from "moment";

import TaskList from "../../containers/TaskList";
import '../../assets/styles/App.scss';
import '../../assets/styles/ContestPage.scss'
import HeaderImage from '../HeaderImage'
import Header from "../Header";

import {HomeElement, ContestsElement, NavBarElement} from '../../utils';


class ContestPage extends Component {

    constructor(props) {
        super(props);
    }

    render() {
        const { user, contest } = this.props;

        if (typeof contest === 'undefined') {
            this.props.onRefreshContest();
            return <div/>
        }

        const tempImage = "https://cdn2.cppinvestments.com/wp-content/uploads/2020/01/512x512_Logo.png";
        let imageUrl;
        if (contest.imagePath == null) {
            imageUrl = tempImage;
        }
        else {
            imageUrl = `http://localhost:8000/${contest.imagePath}`;
        }

        const startDate = moment(new Date(contest.startDate));
        const endDate = moment(new Date(contest.endDate));

        let navBarElements = [
                HomeElement,
                ContestsElement,
                new NavBarElement('Teams', `/contests/${contest.id}/teams`),
                new NavBarElement('Solutions', `/contests/${contest.id}/solutions`),
                new NavBarElement('Leaderboard', `/contests/${contest.id}/leader-board`)
            ];

        if (user.role === 'organizer') {
            navBarElements = navBarElements.concat([
                new NavBarElement('Create task', `/contests/${contest.id}/tasks/new`)
            ])
        }

        return (
            <div>
                <Header navBarElements={navBarElements}/>
                <div className="page">

                    <HeaderImage title={contest.name} description={contest.description} imageUrl={imageUrl} adminMode={true} />

                    <div className="content">
                        <div className="information-block">
                            <div className="">
                                <h6>Beginning date</h6>
                                <p> {startDate.format('MM/DD/YYYY h:mm a')} </p>
                            </div>
                            <div className="spacer" />
                            <div>
                                <h6> Ending date </h6>
                                <p> {endDate.format('MM/DD/YYYY h:mm a')} </p>
                            </div>
                            <div className="spacer" />
                            <div>
                                <h6> Max teams </h6>
                                <p> {contest.maxTeams} </p>
                            </div>
                            <div className="spacer" />
                            <div>
                                <h6> Max participants in team </h6>
                                <p> {contest.maxParticipantsInTeam} </p>
                            </div>
                        </div>
                        <div className="contests-list">
                            <TaskList contest={contest}/>
                        </div>
                    </div>

                </div>
            </div>
        )
    }
}


export default withRouter(ContestPage);
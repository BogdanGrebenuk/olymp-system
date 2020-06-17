import React, { Component } from 'react';
import { withRouter } from "react-router";
import {ContestsElement, HomeElement, NavBarElement} from "../utils";
import Header from "./Header";
import MemberListContainer from "../containers/MemberList";
import InviteBlockContainer from "../containers/InviteBlock";

import "../assets/styles/TeamPage.scss"

class TeamPage extends Component {

    render() {
        const { user, team, contest } = this.props;

        if (typeof team === 'undefined') {
            this.props.onRefreshTeams();
            return <div/>
        }

        if (typeof contest === 'undefined') {
            this.props.onRefreshContest();
            return null;
        }

        const navBarElements = [
            HomeElement,
            ContestsElement,
            new NavBarElement(contest.name, `/contests/view/${team.contestId}`),
            new NavBarElement('Teams', `/contests/${team.contestId}/teams`),
            // new NavBarElement('Team', this.props.match.url)
        ];

        return (
            <>
                <Header navBarElements={navBarElements}/>
                <div className="page">
                    <h3> {team.name} </h3>
                    <MemberListContainer team={team}/>

                    <div className="delimiter" />

                    {
                        team.trainerId === user.id
                            ? <InviteBlockContainer team={team}/>
                            : null
                    }
                </div>
            </>
        )
    }
}


export default withRouter(TeamPage);

import React, { Component } from 'react';
import { withRouter } from "react-router";
import {ContestsElement, HomeElement, NavBarElement} from "../utils";
import Header from "./Header";
import MemberListContainer from "../containers/MemberList";
import InviteBlockContainer from "../containers/InviteBlock";


class TeamPage extends Component {

    render() {
        const { user, team } = this.props;

        if (typeof team === 'undefined') {
            this.props.onRefreshTeams();
            return <div/>
        }

        const navBarElements = [
            HomeElement,
            ContestsElement,
            new NavBarElement('Contest', `/contests/view/${team.contestId}`),
            new NavBarElement('Teams', `/contests/${team.contestId}/teams`),
            new NavBarElement('Team', this.props.match.url)
        ];

        return (
            <div>
                <Header navBarElements={navBarElements}/>
                <div>
                    <h3> {team.name} </h3>
                    <MemberListContainer team={team}/>

                    {
                        team.trainerId === user.id
                            ? <InviteBlockContainer team={team}/>
                            : null
                    }

                </div>
            </div>
        )
    }
}


export default withRouter(TeamPage);

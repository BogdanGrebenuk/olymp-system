import React, { Component } from 'react';
import {withRouter} from "react-router";

import Header from "./Header";
import TeamListContainer from "../containers/TeamList";
import {ContestsElement, HomeElement, NavBarElement} from "../utils";


class TeamsPage extends Component {
    render() {
        const { user, contest } = this.props;

        if (typeof contest === 'undefined') {
            this.props.onRefreshContest();
            return <div/>
        }

        let navBarElements = [
            HomeElement,
            ContestsElement,
            new NavBarElement(contest.name, `/contests/view/${contest.id}`),
            new NavBarElement('Teams', this.props.match.url),
        ]

        if (user.role === 'trainer') {
            navBarElements = navBarElements.concat([
                new NavBarElement('Create team', `/contests/${contest.id}/teams/new`),
            ]);
        }

        return (
            <>
                <Header navBarElements={navBarElements}/>
                <div className="page">
                    <TeamListContainer contest={contest}/>
                </div>
            </>
        )
    }

}


export default withRouter(TeamsPage);
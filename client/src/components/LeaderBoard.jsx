import React, { Component } from "react";
import {withRouter} from "react-router";

import Header from "./Header";
import {ContestsElement, HomeElement, NavBarElement} from "../utils";
import LeaderBoardTableContainer from "../containers/LeaderBoardTable";


class LeaderBoard extends Component {
    render() {
        const { contest } = this.props;
        if (typeof contest === 'undefined') {
            this.props.onRefreshContest();
            return null;
        }

        const navBarElements = [
            HomeElement,
            ContestsElement,
            new NavBarElement(contest.name, `/contests/view/${contest.id}`)
        ];

        return (
            <div>
                <Header navBarElements={navBarElements}/>
                <div className='page'>
                    <LeaderBoardTableContainer contest={contest}/>
                </div>
            </div>
        )
    }
}


export default withRouter(LeaderBoard);
import React, { Component } from "react";
import {withRouter} from "react-router";

import SolutionsTableContainer from "../containers/SolutionsTable";
import Header from "./Header";
import {ContestsElement, HomeElement, NavBarElement} from "../utils";


class SolutionsPage extends Component {
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
                    <SolutionsTableContainer contest={contest}/>
                </div>
            </div>
        )
    }
}


export default withRouter(SolutionsPage);
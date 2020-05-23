import React, { Component } from "react";
import {withRouter} from "react-router";

import SolutionsTableContainer from "../containers/SolutionsTable";
import Header from "./Header";
import {ContestsElement, ContestsNewElement, HomeElement} from "../utils";


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
            ContestsNewElement
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
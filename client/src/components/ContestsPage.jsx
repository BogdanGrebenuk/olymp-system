import React, { Component } from 'react';
import { withRouter } from "react-router";

import ContestListContainer from "../containers/ContestList";
import PageDescriptionHeader from "./PageDescriptionHeader";


class ContestsPage extends  Component {

    onCreateContestClicked() {
        this.props.history.push('/contests/new');
    }

    render() {
        return (
            <div className='page'>
                <PageDescriptionHeader description='Contests'/>
                <ContestListContainer/>
                <button onClick={this.onCreateContestClicked.bind(this)}> Create contest </button>
            </div>
        )
    }

}


export default withRouter(ContestsPage);
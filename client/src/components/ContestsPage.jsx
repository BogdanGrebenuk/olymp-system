import React, { Component } from 'react';
import { withRouter } from "react-router";

import {HomeElement, ContestsElement, ContestsNewElement} from '../utils';


import ContestListContainer from "../containers/ContestList";

import '../assets/styles/ContestsPage.scss'
import Header from "./Header";

class ContestsPage extends  Component {

    render() {
        const { user } = this.props;

        let navBarElements = [HomeElement, ContestsElement];
        if (user.role === 'organizer') {
            navBarElements = navBarElements.concat([ContestsNewElement]);
        }

        return (
            <>
                <Header navBarElements={navBarElements}/>
                <div className='page'>
                    <ContestListContainer/>
                </div>
            </>
        )
    }

}


export default withRouter(ContestsPage);
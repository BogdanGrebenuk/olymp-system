import React, { Component } from 'react';
import { withRouter } from "react-router";
import {Link} from "react-router-dom"

import defaultImg from '../assets/images/logo-og.png'

import ContestListContainer from "../containers/ContestList";
import HeaderImage from './HeaderImage'

import '../assets/styles/ContestsPage.scss'

class ContestsPage extends  Component {

    onCreateContestClicked() {
        this.props.history.push('/contests/new');
    }

    render() {
        return (
            <div className='page'>
                
                <ContestListContainer/>


                {/* <button onClick={this.onCreateContestClicked.bind(this)}> Create contest </button> */}
            </div>
        )
    }

}


export default withRouter(ContestsPage);
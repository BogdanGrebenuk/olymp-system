import React, { Component } from 'react';
import { withRouter } from "react-router";

import '../App.css';


class ContestItem extends Component {

    onContestSelected() {
        this.props.history.push(
            '/contests/view/'.concat(this.props.contest.id)
        )
    }

    onReadMoreButtonClicked(e) {
        e.stopPropagation()
    }

    render() {
        const { contest } = this.props;
        return (
            <div className='card-block' onClick={this.onContestSelected.bind(this)}>
                <div className='card-image-div'>
                    <img className='card-image' src="https://cdn2.cppinvestments.com/wp-content/uploads/2020/01/512x512_Logo.png"/>
                </div>

                <div className='card-content'>
                    <h3 className='card-title'> {contest.name} </h3>
                    <h4 className='card-main-text'> {contest.description} </h4>
                    <button className='card-button' onClick={this.onReadMoreButtonClicked.bind(this)}> Read more </button>
                </div>
            </div>
        )
    }

}


export default withRouter(ContestItem);
import React, { Component } from 'react';

import ContestItem from './ContestItem';

import '../assets/styles/App.scss';


class ContestList extends Component {

    componentDidMount() {
        this.props.onFetchContests();
    }

    render() {
        const { contests } = this.props;

        return (
            <div className="contest-list">
                {
                    contests.map(
                        contest => <ContestItem key={contest.id} contest={contest}/>
                    )
                }
            </div>
        )
    }

}


export default ContestList;
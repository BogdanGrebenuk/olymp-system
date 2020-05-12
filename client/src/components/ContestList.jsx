import React, { Component } from 'react';

import ContestItem from './ContestItem';

import '../assets/styles/App.scss';


class ContestList extends Component {

    componentDidMount() {
        this.props.onFetchContests();
    }

    render() {
        //const { contests } = this.props;
        const contests = [
            { id: 1, name: "Name", description: "Description" },
            { id: 2, name: "Name 2", description: "Description" },
            { id: 3, name: "Name 3", description: "Descriptionnf dsfgsfgd zrgaer eERTAETHRSTH" },
            { id: 4, name: "Name 4", description: "Descriptionnf dsfgsfgd zrgaer eERTAETHRSTH" },
            { id: 4, name: "Name 4", description: "Descriptionnf dsfgsfgd zrgaer eERTAETHRSTH" },
            { id: 4, name: "Name 4", description: "Descriptionnf dsfgsfgd zrgaer eERTAETHRSTH" },
            { id: 4, name: "Name 4", description: "Descriptionnf dsfgsfgd zrgaer eERTAETHRSTH" },
            { id: 4, name: "Name 4", description: "Descriptionnf dsfgsfgd zrgaer eERTAETHRSTH" }
        ];

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
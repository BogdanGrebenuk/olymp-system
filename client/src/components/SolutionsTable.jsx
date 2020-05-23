import React, { Component } from 'react';

import SolutionsTableRowContainer from "../containers/SolutionsTableRow";

import "../assets/styles/SolutionsTable.scss"

class SolutionsTable extends Component {
    componentDidMount() {
        this.props.onFetchContestSolutions(
            this.props.contest.id
        );
    }

    render() {
        const { contest, solutions } = this.props;
        return (
            <table>
                <thead>
                    <tr>
                        <th> Team</th>
                        <th> Task </th>
                        <th> Language </th>
                        <th> Passed </th>
                    </tr>
                </thead>
                <tbody>
                    {
                        solutions.map(
                            (solution, i) => <SolutionsTableRowContainer key={i} contest={contest} solution={solution}/>
                        )
                    }
                </tbody>
            </table>
        )
    }
}


export default SolutionsTable;
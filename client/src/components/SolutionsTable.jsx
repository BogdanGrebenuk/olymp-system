import React, { Component } from 'react';

import SolutionsTableRowContainer from "../containers/SolutionsTableRow";


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
                <tr>
                    <th> Team</th>
                    <th> Task </th>
                    <th> Language </th>
                    <th> Passed </th>
                </tr>
                {
                    solutions.map(
                        (solution, i) => <SolutionsTableRowContainer key={i} contest={contest} solution={solution}/>
                    )
                }
            </table>
        )
    }
}


export default SolutionsTable;
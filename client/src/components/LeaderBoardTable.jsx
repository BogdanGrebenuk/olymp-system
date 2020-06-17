import React, { Component } from "react";
import {withRouter} from "react-router";

import "../assets/styles/SolutionsTable.scss"


class LeaderBoardTable extends Component {
    componentDidMount() {
        this.props.onFetchLeaderBoard(this.props.contest.id);
    }

    render() {
        const { leaderBoard } = this.props;

        return (
            <table>
                <thead>
                    <tr>
                        <th>№</th>
                        <th>Team</th>
                        <th>Solved tasks</th>
                        <th>Score</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        leaderBoard.map(
                            (teamInfo, i) => {
                                return (
                                    <tr>
                                        <td> {i+1} </td>
                                        <td> {teamInfo.name} </td>
                                        <td> {teamInfo.solvedTasksAmount} </td>
                                        <td> {teamInfo.score} </td>
                                    </tr>
                                )
                            }
                        )
                    }
                </tbody>
            </table>
        )
    }
}


export default withRouter(LeaderBoardTable);
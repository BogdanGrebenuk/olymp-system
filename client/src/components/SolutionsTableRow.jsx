import React, { Component } from 'react';
import {withRouter} from "react-router";


class SolutionsTableRow extends Component {
    render() {
        const { solution, team, task } = this.props;
        if (typeof team === 'undefined') {
            this.props.onRefreshTeams();
            return null;
        }
        if (typeof task === 'undefined') {
            this.props.onRefreshTask();
            return null;
        }
        return (
            <tr>
                <td> {team.name} </td>
                <td> {task.name} </td>
                <td> {solution.language} </td>
                <td> {solution.isPassed.toString()} </td>
            </tr>
        )
    }
}


export default withRouter(SolutionsTableRow);
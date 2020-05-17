import React, { Component } from 'react';
import { withRouter } from "react-router";


class TeamItem extends Component {
    onAcceptButtonClicked(e) {
        e.stopPropagation();
        this.props.onAcceptInvite(this.props.invite.id);
    }

    onDeclineButtonClicked(e) {
        e.stopPropagation();
        this.props.onDeclineInvite(this.props.invite.id);
    }

    onTeamSelected() {
        const contestId = this.props.team.contestId;
        const teamId = this.props.team.id;
        this.props.history.push(
            `/contests/${contestId}/teams/${teamId}/view`
        );
    }

    render() {
        const { team, invite } = this.props;
        return (
            <div onClick={this.onTeamSelected.bind(this)}>
                <h3> {team.name} </h3>
                {
                    invite == null
                        ? null
                        : (
                            <div>
                                <button onClick={this.onAcceptButtonClicked.bind(this)}> Accept </button>
                                <button onClick={this.onDeclineButtonClicked.bind(this)}> Decline </button>
                            </div>
                        )

                }
            </div>
        )
    }
}


export default withRouter(TeamItem);

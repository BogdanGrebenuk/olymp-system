import React, { Component } from 'react';
import { withRouter } from "react-router";


class MemberItem extends Component {
    onDeleteButtonClicked() {
        this.props.onDeleteMember(this.props.member.id);
        this.props.onFetchTeamMembers(this.props.team.contestId, this.props.team.id);
    }

    render() {
        const { user, team, member } = this.props;
        return (
            <div className="member-item">
                <h6> {member.email} </h6>
                <p> {member.firstName} {member.lastName} </p>
                {
                    user.id === team.trainerId
                        ? <button onClick={this.onDeleteButtonClicked.bind(this)}> Delete </button>
                        : null
                }
            </div>
        )
    }
}


export default withRouter(MemberItem);

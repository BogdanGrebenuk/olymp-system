import React, { Component } from 'react';
import { withRouter } from "react-router";


class InviteItem extends Component {

    onDeleteButtonClicked() {
        this.props.onDeleteMember(this.props.invite.id);
    }

    render() {
        const { invite } = this.props;
        return (
            <div className="invite-item">
                <h6>{invite.email}</h6>
                <p> {invite.firstName} {invite.lastName} </p>
                <button onClick={this.onDeleteButtonClicked.bind(this)}> Delete </button>
            </div>
        )
    }
}


export default withRouter(InviteItem);

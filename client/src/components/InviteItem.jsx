import React, { Component } from 'react';
import { withRouter } from "react-router";


class InviteItem extends Component {

    onDeleteButtonClicked() {
        this.props.onDeleteMember(this.props.invite.id);
    }

    render() {
        const { invite } = this.props;
        return (
            <div>
                <h3> {invite.email} </h3>
                <p> {invite.firstName} {invite.lastName} </p>
                <button onClick={this.onDeleteButtonClicked.bind(this)}> Delete </button>
            </div>
        )
    }
}


export default withRouter(InviteItem);

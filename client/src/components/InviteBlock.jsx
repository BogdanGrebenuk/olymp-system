import React, { Component } from 'react';
import { withRouter } from "react-router";
import InviteListContainer from "../containers/InviteList";


class InviteBlock extends Component {
    constructor(props) {
        super(props);

        this.userEmailInput = React.createRef();
    }

    onInviteClicked() {
        const userEmail = this.userEmailInput.current.value.trim();

        if (userEmail.length === 0) {
            return alert('specify user email!');
        }

        const inviteData = {
            email: userEmail,
            teamId: this.props.team.id
        }

        this.props.onInviteUser(inviteData);
    }

    render() {
        const { team, user } = this.props;
        return (
            <div>
                <input ref={this.userEmailInput}/>
                <button onClick={this.onInviteClicked.bind(this)}> Invite </button>
                <InviteListContainer team={team}/>
            </div>
        )
    }
}


export default withRouter(InviteBlock);

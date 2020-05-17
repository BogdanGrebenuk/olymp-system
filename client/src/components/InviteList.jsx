import React, { Component } from 'react';
import { withRouter } from "react-router";

import InviteItemContainer from "../containers/InviteItem";


class InviteList extends Component {

    componentDidMount() {
        this.props.onFetchInvites(this.props.team.contestId, this.props.team.id);
    }

    render() {
        const { invites } = this.props;
        return (
            <div>
                {invites.map((invite, i) => {
                    return <InviteItemContainer key={i} invite={invite}/>
                })}
            </div>
        )
    }
}


export default withRouter(InviteList);

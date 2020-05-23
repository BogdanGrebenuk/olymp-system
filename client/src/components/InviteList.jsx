import React, { Component } from 'react';
import { withRouter } from "react-router";

import InviteItemContainer from "../containers/InviteItem";

import "../assets/styles/InviteList.scss"

class InviteList extends Component {

    componentDidMount() {
        this.props.onFetchInvites(this.props.team.contestId, this.props.team.id);
    }

    render() {
        const { invites } = this.props;
        return (
            <div style={{ display: "flex", alignItems: "center", flexDirection: "column" }}>
                {
                    invites.length !== 0
                    ?
                        <>
                            <h4>Invited people</h4>
                            <div className="invite-list">
                                {invites.map((invite, i) => {
                                    return <InviteItemContainer key={i} invite={invite}/>
                                })}
                            </div>
                        </>
                    : null
                }
            </div>
        )
    }
}


export default withRouter(InviteList);

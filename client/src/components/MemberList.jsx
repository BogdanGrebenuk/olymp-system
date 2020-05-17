import React, { Component } from 'react';
import { withRouter } from "react-router";
import MemberItemContainer from "../containers/MemberItem";

import "../assets/styles/MemberList.scss"

class MemberList extends Component {
    componentDidMount() {
        this.props.onFetchTeamMembers(
            this.props.team.contestId,
            this.props.team.id
        );
    }

    render() {
        const { team, members } = this.props;

        return (
            <div style={{ display: "flex", alignItems: "center", flexDirection: "column" }}>
                {
                    members.length !== 0
                    ?
                        <>
                            <h4>Members</h4>
                            <div className="member-list">
                                {members.map((member, i) => {
                                    return (
                                        // внутри MemberItem будут кнопки "удалить"
                                        <MemberItemContainer key={i} team={team} member={member}/>
                                    )
                                })}
                            </div>
                        </>
                    : null
                }
            </div>
        )
    }
}


export default withRouter(MemberList);

import React, { Component } from 'react';
import { withRouter } from "react-router";
import MemberItemContainer from "../containers/MemberItem";


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
            <div>
                {members.map((member, i) => {
                    return (
                        // внутри MemberItem будут кнопки "удалить"
                        <MemberItemContainer key={i} team={team} member={member}/>
                    )
                })}
            </div>
        )
    }
}


export default withRouter(MemberList);

import React, { Component } from 'react';
import {withRouter} from "react-router";

// import TeamItem from "./TeamItem";
import TeamItemContainer from "../containers/TeamItem";

import '../assets/styles/App.scss';


class TeamList extends Component {
    componentDidMount() {
        this.props.onFetchTeams(this.props.contest.id);
        if (this.props.user.role === 'participant') {
            this.props.onFetchInvitesForContest(this.props.contest.id);
        }
    }

    render() {
        const { teams, invites } = this.props;
        // console.log(invites)
        // console.log(teams)
        let teamToInvite = {};
        for (let invite of invites) {
            teamToInvite[invite.teamId] = invite;
        }
        // console.log('sssssss', teamToInvite)
        return (
            <div className='flex-container-column'>
                {teams.map((team, id) => {
                    return <TeamItemContainer
                        invite={teamToInvite.hasOwnProperty(team.id) ? teamToInvite[team.id] : null}
                        key={id}
                        team={team}
                    />
                })}
            </div>
        )
    }

}


export default withRouter(TeamList);

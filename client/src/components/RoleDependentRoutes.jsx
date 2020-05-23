import React, { Component } from 'react';
import {Route} from "react-router";
import ContestsPageContainer from "../containers/ContestsPage";
import CreateContestContainer from "../containers/CreateContest";
import ContestPageContainer from "../containers/ContestPage";
import CreateTaskContainer from "../containers/CreateTask";
import TaskPageContainer from "../containers/TaskPage";
import CreateTeamContainer from "../containers/CreateTeam";
import TeamsPageContainer from "../containers/TeamsPage";
import TeamPageContainer from "../containers/TeamPage";
import SolutionsPageContainer from "../containers/SolutionsPage";


class RoleDependentRoutes extends Component {
    render() {
        const { user } = this.props;

        if (user == null) {
            return <div/>
        }

        let routesInfo = [
            {path: '/contests', component: ContestsPageContainer},
            {path: '/contests/view/:contestId', component: ContestPageContainer},
            {path: '/contests/:contestId/teams', component: TeamsPageContainer},
            {path: '/contests/:contestId/teams/:teamId/view', component: TeamPageContainer},
            {path: '/contests/:contestId/tasks/:taskId/view', component: TaskPageContainer},
            {path: '/contests/:contestId/solutions', component: SolutionsPageContainer},
            // {path: '/contests/:contestId/solutions/:solutionId/view', component: SolutionPageContainer}
        ];

        if (user.role === 'organizer') {
           routesInfo = routesInfo.concat([
               {path: '/contests/new', component: CreateContestContainer},
               {path: '/contests/:contestId/tasks/new', component: CreateTaskContainer},
           ])
        } else if (user.role === 'trainer') {
            routesInfo = routesInfo.concat([
                {path: '/contests/:contestId/teams/new', component: CreateTeamContainer}
            ]);
        }

        return (
            <div>
                {routesInfo.map((routeInfo, i) => {
                    return <Route
                        exact
                        path={routeInfo.path}
                        component={routeInfo.component}
                        key={i}
                    />
                })}
            </div>
        );
    }
}


export default RoleDependentRoutes;
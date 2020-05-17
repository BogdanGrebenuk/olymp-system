import axios from "axios";


String.prototype.format = function () {
    let i = 0, args = arguments;
    return this.replace(/{}/g, function () {
        return typeof args[i] != 'undefined' ? args[i++] : '';
    });
};


const BASE_URL = 'http://localhost:8000/'
const API_URL = BASE_URL.concat('api/');

const GET_CONTESTS_URL = API_URL.concat('contests');
const GET_CONTEST_URL = API_URL.concat('contests/{}');
const POST_CONTESTS_URL = API_URL.concat('contests');
const GET_TASKS_URL = API_URL.concat('contests/{}/tasks');
const GET_TASK_URL = API_URL.concat('contests/{}/tasks/{}')
const POST_TASKS_URL = API_URL.concat('tasks');
const POST_SOLUTION = API_URL.concat('solutions');
const REGISTER_USER_URL = BASE_URL.concat('users');
const AUTHENTICATE_USER_URL = BASE_URL.concat('login');
const GET_CURRENT_USER_URL = API_URL.concat('users/me')
const POST_TEAM_URL = API_URL.concat('teams')
const GET_TEAMS_URL = API_URL.concat('contests/{}/teams')
const GET_TEAM_MEMBERS_URL = API_URL.concat('contests/{}/teams/{}/members')
const DELETE_TEAM_MEMBER_URL = API_URL.concat('invites/{}')
const POST_TEAM_MEMBER_URL = API_URL.concat('invites')
const GET_USERS_URL = API_URL.concat('users')
const GET_INVITES_FOR_TEAM_URL = API_URL.concat('contests/{}/teams/{}/invites')
const GET_INVITES_FOR_CONTEST_URL = API_URL.concat('invites/received')
const ACCEPT_INVITE_URL = API_URL.concat('invites/{}/accept')
const DECLINE_INVITE_URL = API_URL.concat('invites/{}/decline')


function getToken() {
    return localStorage.getItem('token');
}


export function fetchContestService(contestId, token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    return axios.get(GET_CONTEST_URL.format(contestId), {
        headers: {
            Authorization: 'Bearer '.concat(token)
        }
    });
}


export function fetchContestsService(token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    return axios.get(GET_CONTESTS_URL, {
        headers: {
            Authorization: 'Bearer '.concat(token)
        }
    });
}


export function createContestService(contestData, token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    const formData = new FormData();

    formData.append('image', contestData.image);
    formData.append('name', contestData.name);
    formData.append('description', contestData.description);
    formData.append('max_teams', contestData.maxTeams);
    formData.append('max_participants_in_team', contestData.maxParticipantsInTeam);
    formData.append('start_date', contestData.beginningDate);
    formData.append('end_date', contestData.endingDate);

    return axios.post(
        POST_CONTESTS_URL, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
                Authorization: 'Bearer '.concat(token)
            }
        }
    );
}


export function fetchTaskService(contestId, taskId, token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }

    const url = GET_TASK_URL.format(contestId, taskId);
    return axios.get(url, {
        headers: {
            Authorization: 'Bearer '.concat(token)
        }
    })
}


export function fetchTasksService(contestId, token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    const url = GET_TASKS_URL.format(contestId);
    return axios.get(url, {
        headers: {
            Authorization: 'Bearer '.concat(token)
        }
    });
}


export function createTaskService(
    contestId,
    taskName,
    description,
    maxCPU,
    maxMemory,
    taskIOs,
    token
) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
   return axios.post(
       POST_TASKS_URL,
       {
           name: taskName,
           contest_id: contestId,
           input_output: taskIOs,
           description,
           max_cpu_time: maxCPU,
           max_memory: maxMemory
       },
       {
            headers: {
                Authorization: 'Bearer '.concat(token)
            }
       }
   )
}


export function submitSolutionService(taskId, code, language, token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    return axios.post(POST_SOLUTION, {
        task_id: taskId,
        code,
        language
    }, {
        headers: {
            Authorization: 'Bearer '.concat(token)
        }
    })
}

export function registerUserService(userData, token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    return axios.post(REGISTER_USER_URL, {
       first_name: userData.firstName,
       last_name: userData.lastName,
       patronymic: userData.patronymic,
       email: userData.email,
       password: userData.password,
       role: userData.role
    }, {
        headers: {
            Authorization: 'Bearer '.concat(token)
        }
    });
}

export function authenticateUserService(userData, token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    return axios.post(AUTHENTICATE_USER_URL, {
        email: userData.email,
        password: userData.password
    }, {
        headers: {
            Authorization: 'Bearer '.concat(token)
        }
    })
}


export function fetchCurrentUserService(token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    return axios.get(GET_CURRENT_USER_URL, {
        headers: {
            Authorization: 'Bearer '.concat(token)
        }
    })
}


export function createTeamService(teamData, token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    return axios.post(POST_TEAM_URL, {
        name: teamData.name,
        contest_id: teamData.contestId,
        // image: teamData.image
    }, {
        headers: {
            Authorization: 'Bearer '.concat(token)
        }
    })
}


export function fetchTeamsService(contestId, token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    return axios.get(GET_TEAMS_URL.format(contestId), {
        headers: {
            Authorization: 'Bearer '.concat(token)
        }
    });
}


export function fetchTeamMembersService(contestId, teamId, token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    return axios.get(GET_TEAM_MEMBERS_URL.format(contestId, teamId), {
        headers: {
            Authorization: 'Bearer '.concat(token)
        }
    });
}


export function deleteMemberService(memberId, token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    return axios.delete(DELETE_TEAM_MEMBER_URL.format(memberId), {
        headers: {
            Authorization: 'Bearer '.concat(token)
        }
    });
}


export function inviteUserService(inviteData, token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    return axios.post(POST_TEAM_MEMBER_URL, {
        email: inviteData.email,
        team_id: inviteData.teamId
    }, {
        headers: {
            Authorization: 'Bearer '.concat(token)
        }
    })
}


export function getUsersService(token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    return axios.get(GET_USERS_URL, {
        headers: {
            Authorization: 'Bearer '.concat(token)
        }
    });
}


export function getInvitesForTeamService(contestId, teamId, token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    return axios.get(GET_INVITES_FOR_TEAM_URL.format(contestId, teamId), {
        headers: {
            Authorization: 'Bearer '.concat(token)
        }
    })
}


export function getInvitesForContestService(contestId, token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    return axios.get(GET_INVITES_FOR_CONTEST_URL, {
        params: { 'contest_id': contestId },
        headers: {
            Authorization: 'Bearer '.concat(token)
        }
    })
}


export function acceptInviteService(inviteId, token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    return axios.put(ACCEPT_INVITE_URL.format(inviteId), {}, {
        headers: {
            Authorization: 'Bearer '.concat(token)
        }
    });
}


export function declineInviteService(inviteId, token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    return axios.put(DECLINE_INVITE_URL.format(inviteId), {}, {
        headers: {
            Authorization: 'Bearer '.concat(token)
        }
    });
}

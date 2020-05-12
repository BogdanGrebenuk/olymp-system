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
const POST_TASKS_URL = API_URL.concat('tasks');
const POST_SOLUTION = API_URL.concat('solutions');
const REGISTER_USER_URL = BASE_URL.concat('user');
const AUTHENTICATE_USER_URL = BASE_URL.concat('login');


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


export function createContestService(contestName, contestDescription, imageData, token) {
    if (typeof token === 'undefined') {
        token = getToken();
    }
    const formData = new FormData();

    formData.append('image', imageData);
    formData.append('name', contestName);
    formData.append('description', contestDescription);

    return axios.post(
        POST_CONTESTS_URL, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
                Authorization: 'Bearer '.concat(token)
            }
        }
    );
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
       // name: taskName,
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

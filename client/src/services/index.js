import axios from "axios";


String.prototype.format = function () {
    let i = 0, args = arguments;
    return this.replace(/{}/g, function () {
        return typeof args[i] != 'undefined' ? args[i++] : '';
    });
};


const API_URL = 'http://localhost:8000/api/';

const GET_CONTESTS_URL = API_URL.concat('contests');
const GET_CONTEST_URL = API_URL.concat('contests/{}')
const POST_CONTESTS_URL = API_URL.concat('contests');
const GET_TASKS_URL = API_URL.concat('contests/{}/tasks')
const POST_TASKS_URL = API_URL.concat('tasks')
const POST_SOLUTION = API_URL.concat('solutions')


export function fetchContestService(contestId) {
    return axios.get(GET_CONTEST_URL.format(contestId));
}


export function fetchContestsService() {
    return axios.get(GET_CONTESTS_URL);
}


export function createContestService(contestName, contestDescription, imageData) {
    const formData = new FormData();

    formData.append('image', imageData);
    formData.append('name', contestName);
    formData.append('description', contestDescription);

    console.log(formData);

    return axios.post(
        POST_CONTESTS_URL, formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }
    );
}


export function fetchTasksService(contestId) {
    const url = GET_TASKS_URL.format(contestId);
    return axios.get(url);
}


export function createTaskService(
    contestId,
    taskName,
    description,
    maxCPU,
    maxMemory,
    taskIOs
) {
   return axios.post(POST_TASKS_URL, {
       // name: taskName,
       contest_id: contestId,
       input_output: taskIOs,
       description,
       max_cpu_time: maxCPU,
       max_memory: maxMemory
   })
}


export function submitSolutionService(taskId, code, language) {
    return axios.post(POST_SOLUTION, {
        task_id: taskId,
        code,
        language
    })
}

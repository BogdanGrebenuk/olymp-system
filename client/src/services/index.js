import axios from "axios";


const URL = 'http://localhost:8000/api/';


export function fetchContestsService() {
    const url = URL.concat('contests');
    return axios.get(url);
}

export const GET_CONTESTS = 'GET_CONTESTS';
export const SET_CONTESTS = 'SET_CONTESTS';


export function getContests() {
    return {
        type: GET_CONTESTS,
        payload: {}
    }
}

export function setContests(contests) {
    return {
        type: SET_CONTESTS,
        payload: { contests }
    }
}

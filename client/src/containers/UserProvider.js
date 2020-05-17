import { connect } from 'react-redux';


import UserProviderComponent from "../components/UserProvider";
import {getCurrentUser, getUsers} from "../actions";


const onFetchUser = dispatch => () => {
    dispatch(getCurrentUser());
}


const onFetchUsers = dispatch => () => {
    dispatch(getUsers());
}


const mapDispatchToProps = dispatch => {
    return {
        onFetchUser: onFetchUser(dispatch),
        onFetchUsers: onFetchUsers(dispatch)
    }
}


const UserProviderContainer = connect(null, mapDispatchToProps)(UserProviderComponent);

export default UserProviderContainer;

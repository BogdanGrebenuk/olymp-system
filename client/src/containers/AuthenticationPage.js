import { connect } from 'react-redux';

import AuthenticationPageComponent from "../components/AuthenticationPage";
import { authenticateUser } from "../actions";


const onAuthenticateUser = dispatch => userData => {
    dispatch(authenticateUser(userData));
}


const mapDispatchToProps = dispatch => {
    return {
        onAuthenticateUser: onAuthenticateUser(dispatch)
    }
}


const AuthenticationPageContainer = connect(null, mapDispatchToProps)(AuthenticationPageComponent);

export default AuthenticationPageContainer;
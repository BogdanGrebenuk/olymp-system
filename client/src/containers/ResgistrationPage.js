import { connect } from "react-redux";

import RegistrationPageComponent from "../components/RegistrationPage";
import { registerUser } from "../actions";


const onRegisterUser = dispatch => (userData) => {
    dispatch(registerUser(userData));
}


const mapDispatchToProps = dispatch => {
    return {
        onRegisterUser: onRegisterUser(dispatch)
    }
}


const RegistrationPageContainer = connect(null, mapDispatchToProps)(RegistrationPageComponent);

export default RegistrationPageContainer;
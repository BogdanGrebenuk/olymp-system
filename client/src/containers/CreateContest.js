import { connect } from 'react-redux';

import CreateContestComponent from "../components/CreateContest";
import { createContest } from "../actions";


const onCreateContest = dispatch => (name, description) => {
    dispatch(createContest(name, description));
}


const mapDispatchToProps = dispatch => {
    return {
        onCreateContest: onCreateContest(dispatch)
    }
}


const CreateContestContainer = connect(null, mapDispatchToProps)(CreateContestComponent);


export default CreateContestContainer;

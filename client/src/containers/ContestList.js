import { connect } from 'react-redux';

import ContestListComponent from "../components/ContestList";
import {getContests} from "../actions";


const onFetchContests = dispatch => () => {
    dispatch(getContests());
}


const mapStateToProps = state => {
    return {
        contests: Object.values(state.contests)
    }
};


const mapDispatchToProps = dispatch => {
    return {
        onFetchContests: onFetchContests(dispatch)
    }
}


const ContestListContainer = connect(mapStateToProps, mapDispatchToProps)(ContestListComponent);


export default ContestListContainer;

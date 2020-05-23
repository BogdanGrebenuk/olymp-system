import { connect } from 'react-redux';

import SolutionsTableComponent from "../components/SolutionsTable";
import {getSolutionsForContest} from "../actions";


const onFetchContestSolutions = dispatch => contestId => {
    dispatch(getSolutionsForContest(contestId));
}


const mapStateToProps = (state, ownProps) => {
    return {
        contest: ownProps.contest,
        solutions: Object.values(state.solutions)
    }
}


const mapDispatchToProps = (dispatch) => {
    return {
        onFetchContestSolutions: onFetchContestSolutions(dispatch)
    }
}


const SolutionsTableContainer = connect(mapStateToProps, mapDispatchToProps)(SolutionsTableComponent);


export default SolutionsTableContainer;

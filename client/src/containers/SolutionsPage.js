import { connect } from 'react-redux';

import SolutionsPageComponent from "../components/SolutionsPage";
import {getContest} from "../actions";


const onRefreshContest = (dispatch, contestId) => () => {
    dispatch(getContest(contestId));
}


const mapStateToProps = (state, ownProps) => {
    return {
        contest: state.contests[ownProps.match.params.contestId]
    }
}


const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onRefreshContest: onRefreshContest(dispatch, ownProps.match.params.contestId)
    }
}


const SolutionsPageContainer = connect(mapStateToProps, mapDispatchToProps)(SolutionsPageComponent);


export default SolutionsPageContainer;

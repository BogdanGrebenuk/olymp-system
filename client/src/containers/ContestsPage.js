import { connect } from 'react-redux';

import ContestsPageComponent from "../components/ContestsPage";


const mapStateToProps = state => {
    return {
        user: state.currentUser
    }
}


const ContestsPageContainer = connect(mapStateToProps, null)(ContestsPageComponent);


export default ContestsPageContainer;

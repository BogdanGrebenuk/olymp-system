import { connect } from 'react-redux';


import RoleDependentRoutes from "../components/RoleDependentRoutes";


const mapStateToProps = state => {
    return {
        user: state.currentUser
    }
}


const RoleDependentRoutesContainer = connect(mapStateToProps, null)(RoleDependentRoutes);

export default RoleDependentRoutesContainer;

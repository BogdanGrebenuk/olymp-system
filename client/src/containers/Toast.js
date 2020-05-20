import { connect } from 'react-redux';

import ToastComponent from "../components/Toast";

import {removeFirstToast} from '../actions';


const onRemoveFirstToast = dispatch => {
    dispatch(removeFirstToast());
}


const mapStateToProps = state => {
    return {
        toastMessages: state.toastMessages
    }
}

const mapDispatchToProps = dispatch => {
    return {
        onRemoveFirstToast: onRemoveFirstToast(dispatch)
    }
}


const ToastContainer = connect(mapStateToProps, mapDispatchToProps)(ToastComponent);

export default ToastContainer;

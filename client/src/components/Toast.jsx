import React, { Component } from "react";
import {ToastsContainer, ToastsStore, ToastsContainerPosition} from "react-toasts";


class Toast extends Component {
    render() {
        const { toastMessages } = this.props;
        if (toastMessages.length !== 0) {
            const message = toastMessages[0];
            if (message.type === 'success') {
                ToastsStore.success(message.message);
            }
            else if (message.type === 'error') {
                ToastsStore.error(message.message);
            }

        }
        return <ToastsContainer store={ToastsStore} position={ToastsContainerPosition.TOP_LEFT}/>
    }
}


export default Toast;
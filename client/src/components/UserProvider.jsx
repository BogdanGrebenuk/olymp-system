import React, { Component } from 'react';
import {withRouter} from "react-router";


class UserProvider extends Component {
    componentDidMount() {
        const location = this.props.location.pathname;
        if (location === '/authenticate' || location === '/register') {
            return
        }
        this.props.onFetchUser();
        this.props.onFetchUsers();
    }

    render() {
        return <div/>;
    }
}


export default withRouter(UserProvider);

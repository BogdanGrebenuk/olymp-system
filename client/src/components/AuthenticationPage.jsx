import React, { Component } from 'react';


class AuthenticationPage extends Component {

    constructor(props) {
        super(props);

        this.emailInput = React.createRef();
        this.passwordInput = React.createRef();
    }

    onAuthenticateButtonClicked() {
        const email = this.emailInput.current.value.trim();
        const password = this.passwordInput.current.value.trim();

        if ([email, password].some(el => el.length === 0)) {
            return alert('fill all the fields!')
        }

        const userData = { email, password };

        this.props.onAuthenticateUser(userData);
    }

    render() {
        return (
            <div>
                <input ref={this.emailInput}/>
                <input ref={this.passwordInput}/>
                <button onClick={this.onAuthenticateButtonClicked.bind(this)}> Sign in </button>
            </div>
        )
    }
}


export default AuthenticationPage;
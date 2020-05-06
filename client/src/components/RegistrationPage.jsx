import React, { Component } from 'react';


class RegistrationPage extends Component {

    constructor(props) {
        super(props);

        this.emailInput = React.createRef();
        this.passwordInput = React.createRef();
        this.roleInput = React.createRef();
    }

    onRegisterButtonClicked() {
        const email = this.emailInput.current.value.trim();
        const password = this.passwordInput.current.value.trim();
        const role = this.roleInput.current.value.trim();

        const userData = {
            firstName: 'Вася',
            lastName: 'Пупкин',
            patronymic: 'Каво',
            email,
            password,
            role
        };

        this.props.onRegisterUser(userData);
    }

    render() {
        // TODO: fetch it from api
        const roles = ['trainer', 'participant', 'organizer'];
        return (
            <div>
                <input ref={this.emailInput}/>
                <input ref={this.passwordInput}/>
                <select ref={this.roleInput}>
                    {roles.map((role, i) => <option key={i} value={role}> {role} </option>)}
                </select>
                <button onClick={this.onRegisterButtonClicked.bind(this)}> Register </button>
            </div>
        )
    }
}


export default RegistrationPage;
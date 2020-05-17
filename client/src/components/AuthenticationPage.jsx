import React, { Component } from 'react';
import Header from "./Header";
import {HomeElement} from "../utils";


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
        const navBarElements = [HomeElement];
        return (
            <>
                <Header navBarElements={navBarElements}/>
                <div className="page">
                    <ul className="create-form">
                        <li>
                            <label>Email <span className="required">*</span></label>
                            <input ref={this.emailInput} type="text" className="field-long" />
                        </li>
                        <li>
                            <label>Password <span className="required">*</span></label>
                            <input ref={this.passwordInput} type="password" className="field-long"/>
                        </li>
                        <li>
                            <button className='submit-button' onClick={this.onAuthenticateButtonClicked.bind(this)}> Sign in </button>
                        </li>
                    </ul>
                </div>
            </>
        )
    }
}


export default AuthenticationPage;
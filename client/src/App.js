import React, { Component } from 'react';
import createSagaMiddleware from 'redux-saga';
import { BrowserRouter } from 'react-router-dom';
import { Route } from 'react-router';
import { Provider } from 'react-redux';
import { applyMiddleware, createStore, compose } from "redux";

import AuthenticationPageContainer from "./containers/AuthenticationPage";
import RegistrationPageContainer from "./containers/ResgistrationPage";
import UserProviderContainer from "./containers/UserProvider";
import RoleDependentRoutesContainer from "./containers/RoleDependentRoutes";

import mainReducer from "./reducers";
import rootSaga from "./sagas";
import ToastContainer from "./containers/Toast";


const sagaMiddleware = createSagaMiddleware();
const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const store = createStore(
    mainReducer,
    composeEnhancers(applyMiddleware(sagaMiddleware))
);

sagaMiddleware.run(rootSaga);


class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <BrowserRouter>
                    <Route path={'/register'} component={RegistrationPageContainer}/>
                    <Route path={'/authenticate'} component={AuthenticationPageContainer}/>
                    {/* <UserProviderContainer/> */}
                    <RoleDependentRoutesContainer/>
                    <ToastContainer/>
                </BrowserRouter>
            </Provider>
        )
    }
}


export default App;

import React, { Component } from 'react';
import createSagaMiddleware from 'redux-saga';
import { BrowserRouter } from 'react-router-dom';
import { Route } from 'react-router';
import { Provider } from 'react-redux';
import { applyMiddleware, createStore, compose } from "redux";

import ContestsPage from "./components/ContestsPage";
import CreateContest from "./containers/CreateContest";
import ContestPage from "./containers/ContestPage"
import CreateTaskContainer from "./containers/CreateTask";
import TaskPageContainer from "./containers/TaskView";

import mainReducer from "./reducers";
import rootSaga from "./sagas";


const sagaMiddleware = createSagaMiddleware();
const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose
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
                    <Route exact path='/contests' component={ContestsPage}/>
                    <Route exact path='/contests/new' component={CreateContest}/>
                    <Route exact path='/contests/view/:contestId' component={ContestPage}/>
                    <Route exact path='/contests/:contestId/tasks/new' component={CreateTaskContainer}/>
                    <Route path='/contests/:contestId/tasks/:taskId/view' component={TaskPageContainer}/>
                </BrowserRouter>
            </Provider>
        )
    }
}


export default App;

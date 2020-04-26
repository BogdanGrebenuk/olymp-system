import React, { Component } from 'react';
import createSagaMiddleware from 'redux-saga';
import { BrowserRouter } from 'react-router-dom';
import { Route } from 'react-router';
import { Provider } from 'react-redux';
import { applyMiddleware, createStore } from "redux";

import ContestPage from "./components/ContestPage";
import ContestsPage from "./components/ContestsPage";
import TaskPage from "./components/TaskPage";
import mainReducer from "./reducers";
import rootSaga from "./sagas";


const sagaMiddleware = createSagaMiddleware();
const store = createStore(
    mainReducer,
    applyMiddleware(sagaMiddleware)
);

sagaMiddleware.run(rootSaga);


class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <BrowserRouter>
                    <Route exact path='/contests' component={ContestsPage}/>
                    <Route exact path='/contests/:contestId' component={ContestPage}/>
                    <Route exact path='/contests/:contestId/tasks/:taskId' component={TaskPage}/>
                </BrowserRouter>
            </Provider>
        )
    }
}


export default App;

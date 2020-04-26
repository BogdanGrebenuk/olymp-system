import React, { Component } from 'react';

import ContestListContainer from "../containers/ContestList";

class ContestsPage extends  Component {
    render() {
        return (
            <div>
                <h3> Contest page </h3>
                <ContestListContainer/>
            </div>
        )
    }
}


export default ContestsPage;
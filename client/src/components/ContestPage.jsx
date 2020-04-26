import React, { Component } from 'react';

import TaskList from "./TaskList";


class ContestPage extends Component {

    render() {
        const { contest } = this.props;

        return (
            <div>
                <div>
                    <div> Contest photo </div>
                    <div> Contest description </div>
                </div>

                <TaskList/>

            </div>
        )
    }

}


export default ContestPage;
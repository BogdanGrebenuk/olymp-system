import React, { Component } from 'react';


class TaskPage extends Component {

    render() {
        const { task } = this.props;

        return (
            <div>
                <div> Task name </div>
                <div> Task description </div>
                <div> Code block </div>
                <div> Submit </div>
            </div>
        )
    }

}


export default TaskPage;
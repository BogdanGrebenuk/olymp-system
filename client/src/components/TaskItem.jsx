import React, { Component } from 'react';


class TaskItem extends Component {
    render() {
        const { task } = this.props;
        return (
            <div>
                <div> Task name </div>
            </div>
        )
    }
}


export default TaskItem;
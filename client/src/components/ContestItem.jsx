import React, { Component } from 'react';


class ContestItem extends Component {

    render() {
        const { contest } = this.props;
        return (
            <div>
                <div> Description </div>
                <div> Date of beginning/ending contest, amount of tasks, amount of commands </div>
                <div> Links to rating table, link to info  </div>
            </div>
        )
    }

}


export default ContestItem;
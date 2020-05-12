import React, { Component } from 'react';
import { withRouter } from "react-router";

import TaskList from "../../containers/TaskList";
import '../../assets/styles/App.scss';
import '../../assets/styles/ContestPage.scss'
import TaskPageContainer from "../../containers/TaskView";
import HeaderImage from '../HeaderImage'

class ContestPage extends Component {

    constructor(props) {
        super(props);
        this.isRefreshed = false;
    }

    addTaskButtonClicked() {
        const contestId = this.props.contest.id;
        this.props.history.push(`/contests/${contestId}/tasks/new`);
    }

    render() {
        // const { contest } = this.props;

        // if (typeof contest === 'undefined') {
        //     if (this.isRefreshed) {
        //         return <div> Contest not found! </div>
        //     }
        //     this.isRefreshed = true;
        //     this.props.onRefreshContest();
        //     return <div> Wait... </div>
        // }

        const tempImageUrl = 'https://images.pexels.com/photos/34153/pexels-photo.jpg?auto=compress&cs=tinysrgb&h=350';

        return (
            <div className="page">

                <HeaderImage title={'Title'} description={'Description'} imageUrl={tempImageUrl} adminMode={true} />

                <div className="content">
                    <div className="information-block">
                        <h6>Small title</h6>
                        <p>Some information</p>
                    </div>
                    <div className="contests-list">
                        <TaskList />
                    </div>
                </div>

            </div>
        )
    }
}


export default withRouter(ContestPage);
import React, { Component } from 'react';
import { withRouter } from "react-router";

import TaskList from "../../containers/TaskList";
import '../../App.css';
import './styles.css'
import TaskPageContainer from "../../containers/TaskView";
import PageDescriptionHeader from "../PageDescriptionHeader";


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
        const { contest } = this.props;

        if (typeof contest === 'undefined') {
            if (this.isRefreshed) {
                return <div> Contest not found! </div>
            }
            this.isRefreshed = true;
            this.props.onRefreshContest();
            return <div> Wait... </div>
        }

        const tempImageUrl = 'https://images.pexels.com/photos/34153/pexels-photo.jpg?auto=compress&cs=tinysrgb&h=350';

        return (
            <div>

                {/*<PageDescriptionHeader description={contest.name}/>*/}

                <div className='flex-container-column'>
                    <div className='photo-header'>
                        <img src={tempImageUrl}/>
                    </div>
                    <div className='contest-main'>
                        <div className='info-block'> Useful info </div>
                        <TaskList contest={contest}/>
                    </div>
                </div>

            </div>
        )
    }
}


export default withRouter(ContestPage);
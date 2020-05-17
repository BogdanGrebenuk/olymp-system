import React, { Component } from 'react';
import { withRouter } from "react-router";
import {Link} from "react-router-dom";

import '../assets/styles/ContestItem.scss';


class ContestItem extends Component {

    onContestSelected() {
        this.props.history.push(
            '/contests/view/'.concat(this.props.contest.id)
        )
    }

    onReadMoreButtonClicked(e) {
        e.stopPropagation()
    }

    render() {
        const { contest } = this.props;
        const tempImage = "https://cdn2.cppinvestments.com/wp-content/uploads/2020/01/512x512_Logo.png";
        let imageUrl;
        if (contest.imagePath == null) {
            imageUrl = `url(${tempImage})`
        }
        else {
            imageUrl = `url(http://localhost:8000/${contest.imagePath})`
        }
        return (
            <div className="contest">
                <div className="contest-image" style={{ backgroundImage: `${imageUrl}` }} />
                <div className="contest-information">
                    <h1>{contest.name}</h1>
                    <h3>{contest.description}</h3>
                    <Link to={`/contests/view/${contest.id}`}>Read more</Link>
                </div>
            </div>
        )
    }

}


export default withRouter(ContestItem);
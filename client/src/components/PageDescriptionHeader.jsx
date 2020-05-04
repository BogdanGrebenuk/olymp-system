import React, { Component } from 'react';


class PageDescriptionHeader extends Component {
    render() {
        const {description} = this.props;

        return (
            <div>
                <h3 className='page-description-header'> {description} </h3>
            </div>
            );
    }

}

export default PageDescriptionHeader;
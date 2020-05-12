import React, { Component } from 'react';
import ImageUploader from "react-images-upload";

import '../../assets/styles/CreateContest.scss';


class CreateContest extends Component {

    constructor(props) {
        super(props);
        this.contestNameInput = React.createRef();
        this.contestDescription = React.createRef()
        this.selectedImage = null;
    }

    createContestButtonClicked() {
        const contestName = this.contestNameInput.current.value.trim();
        if (contestName.length === 0) {
            return alert('Contest name can\'t be empty!');
        }
        const contestDescription = this.contestDescription.current.value.trim();
        if (contestDescription.length === 0) {
            return alert('Contest description can\'t be empty!');
        }

        // const imageData = new FormData();
        // imageData.append('file', this.selectedImage);

        this.props.onCreateContest(contestName, contestDescription, this.selectedImage);
    }

    onDrop(pictureFile, pictureDataURL) {
        this.selectedImage = pictureFile[0];
    }

    render() {
        return (
            <div className='page'>
                <h1>Create contest</h1>
                <ul className="create-form">
                    <li>
                        <label>Contest name <span className="required">*</span></label>
                        <input ref={this.contestNameInput} type="text" className="field-long"/>
                    </li>
                    <li>
                        <label> Description <span className="required">*</span></label>
                        <textarea ref={this.contestDescription} className="field-long field-textarea"/>
                    </li>
                    <ImageUploader
                        withIcon={true}
                        buttonText="Choose image"
                        onChange={this.onDrop.bind(this)}
                        imgExtension={[".jpg", ".gif", ".png", ".gif"]}
                        maxFileSize={5242880}
                        singleImage={true}
                      />
                    <li>
                        <button className='submit-button' onClick={this.createContestButtonClicked.bind(this)}> Create</button>
                    </li>
                </ul>
            </div>
        )
    }

}


export default CreateContest;

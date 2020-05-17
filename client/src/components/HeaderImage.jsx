import React, { Component } from 'react';
import ImageUploader from 'react-images-upload';

import defaultImg from '../assets/images/logo-og.png'

import '../assets/styles/HeaderImage.scss'

export default class HeaderImage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            image: this.props.imageUrl ? this.props.imageUrl : defaultImg,
            title: this.props.title,
            description: this.props.description,
            changeTitle: false,
            changeDescription: false,
        }
    }

    onDrop(pictureFile, pictureDataURL) {
        this.setState({ image: pictureFile[0] }, () => console.log(this.state.image));
    }
    handleChange(e) {
        const { target: { name, value } } = e;
        this.setState({ [name]: value });
    }

    render() {
        return(
            <div className="header-image" style={{ backgroundImage: `url(${this.state.image})` }}>
                <div style={{ flex: 0.85, flexDirection: "column" }}>
                    {
                        this.props.adminMode && this.state.changeTitle
                        ?
                            <input
                                type="text"
                                name="title"
                                className="title-input"
                                defaultValue={this.state.title}
                                onBlur={() => this.setState({ changeTitle: false })}
                                onChange={this.handleChange.bind(this)}
                                autoComplete="off"
                            />
                        : <h1 onClick={() => this.setState({ changeTitle: true })}>{this.state.title}</h1>
                    }
                    {
                        this.props.adminMode && this.state.changeDescription
                        ?
                            <input
                                type="text"
                                name="description"
                                className="description-input"
                                defaultValue={this.state.description}
                                onBlur={() => this.setState({ changeDescription: false })}
                                onChange={this.handleChange.bind(this)}
                                autoComplete="off"
                            />
                        : <h3 onClick={() => this.setState({ changeDescription: true })}>{this.props.description}</h3>
                    }
                </div>
                <div style={{ flex: 0.15, flexDirection: "row-reverse" }}>
                    {
                        this.props.adminMode
                        ?
                            <div className="buttons">
                                <ImageUploader
                                    onChange={this.onDrop.bind(this)}
                                    withIcon={false}
                                    withLabel={false}
                                    fileContainerStyle={{
                                        background: 'none',
                                        width: "fit-content",
                                        height: 0,
                                        margin: 0
                                    }}
                                    buttonStyles={{
                                        background: 'none',
                                        fontFamily: "Open Sans",
                                        padding: 0,
                                        fontSize: 15
                                    }}
                                    buttonText='Upload image'
                                    imgExtension={['.jpg', '.gif', '.png', '.gif']}
                                    maxFileSize={5242880}
                                />
                            </div>
                        : null
                    }
                </div>
            </div>
        )
    }
}
import React, {Component} from 'react'
import { NavLink } from "react-router-dom"

import '../assets/styles/Header.scss'


class Header extends Component {
    render() {
        const { navBarElements } = this.props;
        return (
            <div className="header">
                {navBarElements.map((el, i) => {
                    return <NavLink exact to={el.link} activeClassName="active" key={i}>{el.name}</NavLink>
                })}
                <NavLink exact to={'/authenticate'} activeClassName="active">Log out</NavLink>
            </div>
        )
    }
}

export default Header;

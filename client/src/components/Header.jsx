import React from 'react'
import { Link, NavLink } from "react-router-dom"

import '../assets/styles/Header.scss'

export default function Header() {
    return (
        <div className="header">
            <NavLink to="/" activeClassName="active" exact>Home</NavLink>
            <NavLink to="/contests" activeClassName="active" exact>Contests</NavLink>
            <NavLink to="/contests/new" activeClassName="active" exact>Create contest</NavLink>
        </div>
    )
}
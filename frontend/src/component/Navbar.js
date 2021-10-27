import React, { Component } from 'react'

export default class Navbar extends Component {
    render() {
        return (
            <nav className="navbar">
                <div className="container-fluid">
                    <div className="navbar-header">
                        <a href="javascript:void(0);" className="bars" onClick={this.props.onBarClick} ></a>
                        <a className="navbar-brand" href="">ADMINBSB - MATERIAL DESIGN</a>
                    </div>
                </div>
            </nav>
        )
    }
}

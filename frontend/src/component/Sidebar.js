import React, { Component } from 'react'
import userIcon from 'adminbsb-materialdesign/images/user.png'

export default class Sidebar extends Component {

    state = {
        defaultClass: "btn-group user-helper-dropdown"
    }

    constructor(props) {
        super(props);
        this.divref = React.createRef();
    }

    componentWillMount() {
        document.addEventListener("mousedown", this.handleMouseClick, false);
    }

    componentWillUnmount() {
        document.removeEventListener("mousedown", this.handleMouseClick, false);
    }

    handleMouseClick = (event) => {
        if (event.target === this.divref.current) {
            console.log("Click Element");
            return;
        } else {
            console.log("Click Outside");
            this.setState({ defaultClass: "btn-group user-helper-dropdown" });
        }
    };

    showMenu = () => {
        if (this.state.defaultClass == "btn-group user-helper-dropdown") {
            this.setState({ defaultClass: "btn-group user-helper-dropdown open" })
        } else {
            this.setState({ defaultClass: "btn-group user-helper-dropdown" })
        }
    }

    render() {
        return (
            <div>
                <section>
                    <aside id="leftsidebar" className="sidebar">

                        <div className="user-info">
                            <div className="image">
                                <img src={userIcon} width="48" height="48" alt="User" />
                            </div>
                            <div className="info-container">
                                <div className="name" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">John Doe</div>
                                <div className="email">john.doe@example.com</div>

                                <div className={this.state.defaultClass} onClick={this.showMenu} ref={this.divref}>

                                    <i className="material-icons" data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">keyboard_arrow_down</i>
                                    <ul className="dropdown-menu pull-right">
                                        <li><a href="javascript:void(0);"><i className="material-icons">person</i>Profile</a></li>
                                        <li role="separator" className="divider"></li>
                                        <li><a href="javascript:void(0);"><i className="material-icons">group</i>Followers</a></li>
                                        <li><a href="javascript:void(0);"><i className="material-icons">shopping_cart</i>Sales</a></li>
                                        <li><a href="javascript:void(0);"><i className="material-icons">favorite</i>Likes</a></li>
                                        <li role="separator" className="divider"></li>
                                        <li><a href="javascript:void(0);"><i className="material-icons">input</i>Sign Out</a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div className="menu">
                            <ul className="list">
                                <li className="header">MAIN NAVIGATION</li>
                                <li className="active">
                                    <a href="index.html">
                                        <i className="material-icons">home</i>
                                        <span>Home</span>
                                    </a>
                                </li>
                            </ul>
                        </div>

                        <div className="legal">
                            <div className="copyright">
                                &copy; 2016 - 2017 <a href="javascript:void(0);">AdminBSB - Material Design</a>.
                            </div>
                            <div className="version">
                                <b>Version: </b> 1.0.5
                            </div>
                        </div>

                    </aside>
                    <aside id="rightsidebar" className="right-sidebar">
                        <ul className="nav nav-tabs tab-nav-right" role="tablist">
                            <li role="presentation" className="active"><a href="#skins" data-toggle="tab">SKINS</a></li>
                            <li role="presentation"><a href="#settings" data-toggle="tab">SETTINGS</a></li>
                        </ul>

                    </aside>
                </section>
            </div>
        )
    }
}

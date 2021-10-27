import React, { Component } from 'react';
import Overlay from './Overlay';
import PageLoader from './PageLoader';
import Navbar from './Navbar';
import Sidebar from './Sidebar';
import HomeComponent from './HomeComponent';
import GoogleFontLoader from 'react-google-font-loader';
import 'adminbsb-materialdesign/css/themes/all-themes.css'


export default class MainComponent extends Component {

    state = {
        bodyClass: "theme-red ls-closed",
        displayOverlay: "none",
        width: window.screen.width,
    };


    onBarClick = () => {
        if (this.state.bodyClass == "theme-red ls-closed overlay-open") {
            this.setState({ bodyClass: "theme-red ls-closed" });
            this.setState({ displayOverlay: "none" });
        } else if (this.state.bodyClass == "theme-red ls-closed") {
            this.setState({ bodyClass: "theme-red ls-closed overlay-open" });
            this.setState({ displayOverlay: "block" });
        }
    };


    render() {
        if (window.screen.width > 1150) {

            document.getElementById("root").className = "theme-red";
        } else {
            document.getElementById("root").className = this.state.bodyClass;
        }
        return (
            <React.Fragment>
                <GoogleFontLoader
                    fonts={[
                        {
                            font: 'Roboto',
                            weights: [400, 700],
                        }
                    ]}
                    subsets={['cyrillic-ext', 'latin']}
                />
                <GoogleFontLoader
                    fonts={[
                        {
                            font: 'Material+Icons',
                        }
                    ]}
                />

                <Overlay display = {this.state.displayOverlay} />
                <PageLoader />
                <Navbar onBarClick = {this.onBarClick} />
                <Sidebar />
                <HomeComponent />
            </React.Fragment>
        )
    }
}

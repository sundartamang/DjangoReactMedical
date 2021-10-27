import React, { Component } from 'react'

export default class PageLoader extends Component {
    render() {
        return (
            <div classNameName="page-loader-wrapper" style={{display:"none"}}>
                <div classNameName="loader">
                    <div classNameName="preloader">
                        <div classNameName="spinner-layer pl-red">
                            <div classNameName="circle-clipper left">
                                <div classNameName="circle"></div>
                            </div>
                            <div classNameName="circle-clipper right">
                                <div classNameName="circle"></div>
                            </div>
                        </div>
                    </div>
                    <p>Please wait...</p>
                </div>
            </div>
        )
    }
}

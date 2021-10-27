import React, { Component } from 'react'

export default class Overlay extends Component {
    render() {
        return (
            <div class="overlay" style={{display : this.props.display}}></div>
        )
    }
}

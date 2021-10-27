import React, { Component } from 'react';
import GoogleFontLoader from 'react-google-font-loader';
import 'adminbsb-materialdesign/plugins/bootstrap/css/bootstrap.css';
import 'adminbsb-materialdesign/plugins/node-waves/waves.css';
import 'adminbsb-materialdesign/plugins/animate-css/animate.css';
import 'adminbsb-materialdesign/css/style.css';
import AutheHandler from '../utils/AutheHandlers';
import Config  from '../utils/Config';
import {Redirect} from 'react-router-dom';

export default class Login extends Component {

    state = {
        username :"",
        password : "",
        btnDisabled : true,
        loginStatus : 0,
    }

    formSubmit = (event) =>{
        event.preventDefault()
        console.log(this.state)
        this.setState({loginStatus:1})
        AutheHandler.login(this.state.username, this.state.password, this.HandleAjaxresponse)
    }
    saveInput = (event) =>{
        var key = event.target.name;
        this.setState({[key] : event.target.value});
        if(this.state.username !="" && this.state.password != ""){
            this.setState({btnDisabled:false})
        }else{
            this.setState({btnDisabled:true})
        }
    }

    HandleAjaxresponse= (data) =>{
        if(data.error){
            this.setState({loginStatus:400})
        }else{
            this.setState({loginStatus:200})
            window.location = Config.homeurl
        }
    }

    getMessage = () =>{
        if(this.state.loginStatus === 0){
            return "";
        }else if(this.state.loginStatus === 1){
            return (
                <div className="alert alert-warning">
                    <strong>umm </strong> wait a minute !
                </div>
            )
        }
        else if(this.state.loginStatus === 200){
            return (
                <div className="alert alert-success">
                    <strong>Welcome </strong> you are login !
                </div>
            )
        }
        else if(this.state.loginStatus === 400){
            return (
                <div className="alert alert-danger">
                    <strong>opps </strong> womething went wrong !
                </div>
            )
        }
    }

    render() {

        if(AutheHandler.loggedIn){
            return <Redirect to = {Config.homeurl}/>
        }

        return (
            <div className="login-page">
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


                <div className="login-box">
                    <div className="logo">
                        <a href="">Admin<b>BSB</b></a>
                        <small>Django React Medical Store</small>
                    </div>
                    <div className="card">
                        <div className="body">
                            <form id="sign_in" method="POST" onSubmit={this.formSubmit}>
                                <div className="msg">Sign in to start your session</div>
                                {this.getMessage()}
                                <div className="input-group">
                                    <span className="input-group-addon">
                                        <i className="material-icons">person</i>
                                    </span>
                                    <div className="form-line">
                                        <input 
                                            type="text" 
                                            className="form-control" 
                                            name="username" 
                                            placeholder="Username" 
                                            required autofocus 
                                            onChange = {this.saveInput}
                                        />
                                    </div>
                                </div>
                                <div className="input-group">
                                    <span className="input-group-addon">
                                        <i className="material-icons">lock</i>
                                    </span>
                                    <div className="form-line">
                                        <input 
                                            type="password" 
                                            className="form-control" 
                                            name="password" 
                                            placeholder="Password" 
                                            required 
                                            onChange = {this.saveInput}
                                        />
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-xs-8 p-t-5">
                                        <input type="checkbox" name="rememberme" id="rememberme" className="filled-in chk-col-pink" />
                                        <label for="rememberme">Remember Me</label>
                                    </div>
                                    <div className="col-xs-4">
                                        <button disabled={this.state.btnDisabled} className="btn btn-block bg-pink waves-effect" type="submit">SIGN IN</button>
                                    </div>
                                </div>
                                <div className="row m-t-15 m-b--20">
                                    <div className="col-xs-6">
                                        <a href="">Register Now!</a>
                                    </div>
                                    <div className="col-xs-6 align-right">
                                        <a href="">Forgot Password?</a>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

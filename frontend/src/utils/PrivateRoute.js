import React, { Component } from "react";
import { Route, Redirect } from "react-router-dom";
import AutheHandler from "./AutheHandlers";

export var PrivateRoute = ({ component: Component, ...rest }) => (
        <Route
            {...rest}
            render={(props) =>
                AutheHandler.loggedIn() ? <Component {...props} /> : <Redirect to="/" />
            }
        />
    );

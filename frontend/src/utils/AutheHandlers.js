import axios from 'axios';
import Config from './Config';
import {reactLocalStorage} from 'reactjs-localstorage';

class AutheHandler {
    static login(username, password, callback) {
        axios
            .post(Config.loginUrl, { username: username, password: password })
            .then(function (response) {
                if(response.status === 200){
                    reactLocalStorage.set("token", response.data.access)
                    reactLocalStorage.set("refresh", response.data.refresh)
                    callback({"error":false, "message":"Login successfull"})
                }
            })
            .catch(function (error) {
                callback({"error":true, "message":"Invalid username or password"})
            });
    }

    static loggedIn(){
        if(reactLocalStorage.get("token") && reactLocalStorage.get("refresh")){
            return true;
        }else{
            return false;
        }
    }

}
export default AutheHandler;
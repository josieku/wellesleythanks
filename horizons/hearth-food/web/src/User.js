import React, { Component } from "react";

export default class User extends Component{
  render(){
    return(
      <div>
        <Route
          exact={true}
          path='/user/:id'
          render={({ match }) => ()}
        />
      </div>
    )
  }
};

import React, { Component } from "react";

export default class ConsumerProfile extends Component{

  render(){
    const user = this.props.profile;
    const self = this.props.user;
    return(
      <div>
        <p>Consumer Profile</p>
        <h4>{user.firstName}</h4>
        <img src={user.picture}/>
        {user.verified ? <p>Verified</p> : null }
        <p>Preferences:
          <ul>{user.preferrences.map(pref => <li>{pref}</li>)}</ul>
        </p>
        {self._id === user._id ? <Link to={`/user/${self._id}/edit`}>Edit Profile</Link>: null}
      </div>
    )
  }
};

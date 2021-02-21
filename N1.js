import React, { Component} from 'react'


class N1 extends Component {

   render () {

   return (

   <header id = "title">
      <a href = "/head"
      onClick = {function(e) {
      e.preventDefault();
      this.props.onChangePage();
      }.bind(this)}>

         {this.props.title}   
      </a>
   </header>

      );
   }
}

export default N1;



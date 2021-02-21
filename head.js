import React, { Component} from 'react'


class Head extends Component {

   render () {

   return (

   <div id ="head">
      <div>
      <img src = "C:\Users\pc\Desktop\im coder\example1-2\src\memo.jpg"></img>
      </div>
      
      <div>
         <h7>
            <b>  
               <a href = "/head"
                  onClick = {function(e) {
                  e.preventDefault();
                  this.props.onChangePage();
                  }.bind(this)}>

                     {this.props.title}
               </a>
            </b>
         </h7> 
         <br/>
         {this.props.desc}
      </div>

      <div>
      </div>
   </div>
      );
   }
}

export default Head;



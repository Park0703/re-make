import {
   BrowserRouter as router,
   Switch,
   Route,
   Link
} from "react-router-dom";
import React, {Component} from 'react';
import Head from './Components/head.js';
import N3 from './Components/N3.js';
import N2 from './Components/N2.js';
import N1 from './Components/N1.js';
import './App.css';

class App extends Component {
constructor(props) {
   super(props);    
   this.state = {
      mode : "home",
      head_contents : {
         title : 'it\'s title', 
         desc : 'it\'s description'
      },
      contents : [
         {id : 1, title : 'red', desc : 'red is sexy'},
         {id : 2, title : 'yellow', desc : 'yellow is cute'},
         {id : 3, title : 'blue', desc : 'blue is cool'},
         {id : 4, title : 'white', desc : 'white is innocent'},
         {id : 5, title : 'black', desc : 'black is heavy'}
      ]
   }}

   render () {

   return (
      <div id = "outline">
           <Head 
               title = {this.state.head_contents.title}
               desc = {this.state.head_contents.desc}
               onChangePage = {function () {
               this.setState({
                  mode : "home"
                  })}.bind(this)}> 

           </Head>
.
         <div id = "frontline">

            <N1
               > </N1>

            <N2> </N2>
            
            <N3> </N3>
        </div>
            .

         <div id = "bottom"> bottom </div>
      </div>
      );
   }
}

export default App;

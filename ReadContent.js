import React, { Component} from 'react'
import './ReadContent.css';

class ReadContent extends Component {
  render() {
    return (
      <div id = 'Control-div'>
      <article>
        <h2>
          {this.props.title}
        </h2>
        
          {this.props.desc}
      </article>
      </div>
      );
    }
  }

export default ReadContent;

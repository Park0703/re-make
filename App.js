import React, { Component } from 'react'
import TOC from './components/TOC'
import Content from './components/Content'
import Subject from './components/Subject'

class App extends Component {
  render() {
    return (
      <div>
        <Subject title='WEB' sub='world wide web!'></Subject> 
        <Subject title='props ㅈ듀' sub='sub라고 입력된 props'></Subject>
        <TOC></TOC>
        <Content></Content>
      </div>
    )
  }
}

export default App;




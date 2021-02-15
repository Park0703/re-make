import React, { Component } from 'react'

class Control extends Component {
  render() {
    return (
      <ul>
      <li><a href="/create" onClick={function(e){
        e.preventDefault();
        this.props.onChangeMode('create');
      }.bind(this)}
      >create</a></li>

      <li><a href="/update"  onClick={function(e){
        e.preventDefault();
        this.props.onChangeMode('update');
      }.bind(this)}
      >update</a></li>

      {/* 링크로 delete를 하면 마구잡이 삭제를 할 수도 있음 */}
      <li><input  onClick={function(e){
        e.preventDefault();
        this.props.onChangeMode('delete');
      }.bind(this)} type="button" value="delete"
      ></input></li> 

    </ul>
    );
  }
}

export default Control;
// 이벤트 걸때 그걸 못하게 하는 preventDefault();

//immutable, state props, 
// router 페이지 전환, url만으로는 페이지 전환이 안됨
// ui만 바꾸면 됨, url에 따라 컴포넌트가 달라질 수 있음
// 퍼머링크, 플러그인

// npm run eject 하면 마음대로 수정할 수 있음
// redux, react native
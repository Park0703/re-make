// 로딩하는 명령어가 필요함
import React, { Component } from 'react'

class TOC extends Component {
  render() {
    let lists = [];
    let data = this.props.data;
    let i = 0;
    while(i < data.length) {
      lists.push(
         // 여러개 목록 자동생성할때
        <li key={data[i].id}> 
          <a 
          href = {"/content/" + data[i].id}
          data-id = {data[i].id} 
          onClick = {function(e) {
             // 이벤트가 일어난 a 테그 의 target 속성이 중요
             // dataset 속성
             e.preventDefault();
             this.props.onChangePage(e.target.dataset.id);
          }.bind(this)} // bind는 함수에 두번째 인자 값을 첫번째 매개변수값으로 넣어 줄 수 있음
          >{data[i].title}
          </a>
        </li>);
      i = i+1;
    }


    return (
      <nav>
        <ul>
           {lists}
        </ul>
      </nav>
    );
  }
}

// 수많은 변수들을 외부에서도 사용할 수 있게 
export default TOC;
//이거 덕분에 toc의 변수들을 가져다 쓸수 있개ㅔ 됨
// app.js에 import toc from './components/toc'
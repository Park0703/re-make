import React, { Component} from 'react'

class TOC extends Component {
  render() {
    // 미리 state에서 data값을 지정을 한다음, 뽑아쓰기 위해 배열 작성
    let lists = [];
    let data = this.props.data;
    let i = 0;
    while(i < data.length) {
      // 반복문 돌리고 생성된 data를 자동으로 list 배열에 추가
      lists.push(
        // list의 key?는 상위컴포넌트 data에서 지정한 id의 숫자를 차례로 넘기면서 리스트 생성
        <li key = {data[i].id}>
          <a
            // /content/이걸 어떻게? + 순서를 쭉쭉 , 설정된 contents도 아님
            href = {"/content/" + data[i].id}
            // 다시한번 id 지정 '-'은 무슨 의미???이 걸로 뭘한다고?
            data-id = {data[i].id}
            onClick = {function (e) {
              e.preventDefault();
              //이걸 확인하려면 react developer tools가 필요하다. 이걸로 무슨 톱니를 만들지? 어떤 영향을 주지?
              this.props.onChangePage(e.target.dataset.id);
            }.bind(this)}>
            {/* 타이틀로 보여주기, i번째 data의 title state */}
              {data[i].title}
          </a>
        </li>
      ); i++;
    }

    return (      //nav???
      <div id = 'Control-div'>
      <nav>        
        <ul>
          {/* 리스트 조건이랑, 리스트 작성이랑 따로 만들었구나 */}
          {lists}
        </ul>
      </nav>
      </div>
      );
    }}

export default TOC;

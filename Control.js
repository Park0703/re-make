import React, { Component} from 'react'

class Control extends Component {
  render() {

    return (
      // 실질적인 클릭과 모드 변경은 여기서
      <div id = 'Control-div'>
      <ul>
        <li>
          <a 
            href = '/- Create -'
            onClick = {function (e) {
              e.preventDefault();
              // onChangeMode, onChangePage로 다 설정할 수 있나?
              this.props.onChangeMode('create');
            }.bind(this)}>
            - Create -
          </a>
        </li>

        <li>
          <a 
            href = '/- Update -'
            // 클릭을 하면 함수 실행 굿, 그런데 e는 어떤 역할이지? 2를 언제 삽입했지?
            onClick = {function (e) {
              e.preventDefault();
              this.props.onChangeMode('update');
            }.bind(this)}>
            - Update -
          </a>
        </li>

        <li>
          <input
            onClick = {function (e) {
              e.preventDefault();
              this.props.onChangeMode('delete');
            }.bind(this)} 
            // type의 종류, submit, button, 
            type = 'button'
            // 이름은 value
            value = 'Delete'>
          </input>
        </li> 
      </ul>
      </div>
      )
    }
  }

export default Control;

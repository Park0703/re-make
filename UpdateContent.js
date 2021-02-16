import React, { Component} from 'react'

class UpdateContent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      id : this.props.data.id,
      title: this.props.data.title,
      desc : this.props.data.desc
    }
      this.inputFormHandler = this.inputFormHandler.bind(this);
  }
  // 인풋폼 헨들러 와 그 내부 [] : value 어떻게 해석해야할까?
  inputFormHandler(e) {
    this.setState({[e.target.name]:e.target.value});
  }

  render() {

    return (
      <div id='Control-div'>
      <article>
        <h2>
          Update
        </h2>

        <form 
          //  action, create_process? , method 사용법
          action = '/create_process' 
          method='post'
          // submit에 데이터를 추가?
          onSubmit  ={function (e) {
            e.preventDefault();
            this.props.onSubmit(
              this.state.id,
              this.state.title,
              this.state.desc
              );
            }.bind(this)}
          >
            {/* hidden인데 이것의 역할? 무엇을 서로 주고받을까? id 부여하고 표시해서 체크하는 기능 */}
          <input type = 'hidden' name = 'id' value = {this.state.id}></input>

          <p>
            <input
              type = 'text'
              // name이 실질적인 value값을 주고 받는 기능을 할까?
              name = 'title'
              placeholder = 'Title'
              // value를 title로 지정하면 app component까지 올라가려나
              value = {this.state.title}
              // inputFormHandler 
              onChange = {this.inputFormHandler}
            ></input>
          </p>

          <p>
            <textarea
              onChange = {this.inputFormHandler}
              name = 'desc'
              placeholder = 'Description'
              value = {this.state.desc}>
            </textarea>
          </p>

          <p>
            <input 
              type = 'submit'
              value = 'Submit'>
            </input>
          </p>

        </form>
        {this.props.desc}
      </article>
      </div>
      )
    }
  }

export default UpdateContent;

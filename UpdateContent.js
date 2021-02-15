import React, { Component } from 'react'


class UpdateContent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      id:this.props.data.id,
      title:this.props.data.title,
      desc:this.props.data.desc
    }
      this.inputFormHandler = this.inputFormHandler.bind(this);
    }
    inputFormHandler(e) {
      this.setState({[e.target.name]:e.target.value}); // title, desc를 구분하는 []
    }

  render() {
    console.log('UpdateContent render');
    return (
      <article>
        <h2>
            Update
        </h2> 
        {/* react가 아니면 데이터전송, post를 해야 url에 노출이 안됨 */}
        <form action='/create_process' method='post'
          onSubmit={function (e) {
            e.preventDefault();
            // debugger;
            this.props.onSubmit(
              this.state.id,
              this.state.title,
              this.state.desc
              /* react가 아니면 데이터전송, post를 해야 url에 노출이 안됨 */
              );
            // 정보를 추가시키고 싶으면
          }.bind(this)}
        >
          <input type='hidden' name='id' value={this.state.id}></input> 
          {/* 존재하지만 눈에 보이지 않는 hidden */}
          <p>
            <input 
              type='text' 
              name='title' 
              placeholder='title'
              value={this.state.title} // 이러면 고정값이 되기때문에 state
              onChange={this.inputFormHandler} // bind가 this.inputFormHandler = this.inputFormHandler.bind(this);으로 생략
            ></input> 
          </p>

          <p>
            <textarea 
              onChange={this.inputFormHandler}
              name='desc' placeholder='description' value={this.state.desc}>
            </textarea>
            {/* react는 html이 아니다. 해석은 해주지만 값이 이상하게 나온다 */}
          </p>

          <p>
            <input type='submit'>
            </input>
          </p>

        </form>
         {this.props.desc}
      </article>
    );
  }
}

export default UpdateContent;
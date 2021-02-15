import React, { Component } from 'react'


class CreateContent extends Component {
  render() {
    return (
      <article>
        <h2>
            Create
        </h2> 
        {/* react가 아니면 데이터전송, post를 해야 url에 노출이 안됨 */}
        <form action='/create_process' method='post'
          onSubmit={function (e) {
            e.preventDefault();
            // debugger;
            this.props.onSubmit(
            e.target.title.value,
            e.target.desc.value);
            alert('submit');
            // 정보를 추가시키고 싶으면
          }.bind(this)}
        >
          <p>
            <input type='text' name='title' placeholder='title'>
            </input>
          </p>

          <p>
            <textarea name='desc' placeholder='description'>
            </textarea>
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

export default CreateContent;
import React, { Component} from 'react'

class CreateContent extends Component {
  render() {

    return (
      <div id = 'Control-div'>
      <article>
        <h2>
          Create
        </h2>

      <form
        // /create_process????
        action = '/create_process'
        method = 'post'
        // onsubmit??? 아마 버튼이겠지?
        onSubmit = {function (e) {
          e.preventDefault();
          this.props.onSubmit(
            // 입력값이 두개 title, desc , 이걸 어떻게 도출해내지?
            e.target.title.value,
            e.target.desc.value);
          alert('submit');
        }.bind(this)}
        >
          {/* title 입력창 */}
          <p>
            <input
              type = 'text' name = 'title' placeholder = 'Title'>
            </input>
          </p>
          {/* desc입력창 */}
          <p>
            <textarea
              name = 'desc' placeholder = 'Description'>
            </textarea>
          </p>
          {/* 버튼 */}
          <p>
            <input
            // 왜 한글로 번역이 되어있지? 별도로 value를 지정하지 않아서
              type = 'submit'
              value = 'Submit'>
            </input>
          </p>

      </form>  
        {/* desc를 알려줌 */}
        {this.props.desc}
      </article>
      </div>
      );}}

export default CreateContent;

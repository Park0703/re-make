// index에서는 react만 가져왔는데 여기는 React,{component}는 파일안의 펑션, 변수, 요소 //함수형이면 상고나없음
import React, { Component} from 'react'
import Subject from './Components/Subject'
import TOC from './Components/TOC'
import Control from './Components/Control'
import ReadContent from './Components/ReadContent'
import CreateContent from './Components/CreateContent'
import UpdateContent from './Components/UpdateContent'
import './App.css';
import './Components/ReadContent.css';

// as class type, 최상위 컴포넌트를 방출한다.
class App extends Component {
  //여기서 props값들 지정 render보다 먼저 실행하면서 그 컴포넌트를 초기화시켜주고 싶을때, 기본값 지정
  constructor(props) {
    // %% constructor, super, (value)는 어떤역할을 할까?, 최상위기본형
    super(props);
    // %% max_content_id를 어떻게 해석해야할까? 어떻게 값을 지정할까? 변수형 props
    this.max_content_id = 3;
    // %% 드디어 state, props와의 상관관계를 어떻게 찾을 수 있을까?, 메모에는 state값을 사전 정의 객체형 props를 가지고 // state 말만 지정, 간혹 react에서 props, state라는 용어로 값을 지정하는 경우가 있어 에러가 생길 수가 있음
    this.state = {
      // %% mode, 지정값에 대한 동작을 어떻게 풀어나가고, 유지관리하는 방법
      mode : 'create',
      // %% selected_content_id의 의미란?, 2의 의미는? 
      selected_content_id : 2,
      // 아하! 여기서 각각 모드, 컴포넌트의 각각 state를 지정하는 구나, props ref 지정하는 방법과 다르다.
      subject : {
        title : 'It\'s Web Pirate, Guys!',
        sub :'Be ambitious or Be careful.'
      }, Welcome : {
        title : 'welcome to the land',
        desc : 'Hello, Foreigner!'
      }, contents : [
        {id : 1, title : "HTML", desc : 'HTML is for Information.'},
        {id : 2, title : "CSS", desc : 'CSS is for Design.'},
        {id : 3, title : "JavaScript", desc : 'JavaScript is for Interactive.'}
      ]
    }} // app의 props인 state, state의 props인 subject, mode 등등, contents의 props
    // mode는 props, 'create'가 state, 고정된 props에서 나온 초기값 value 값을 최상위 컴포넌트 app에서 하위 콤포넌트로 보내주고, 그걸 화면에 구현 // state 값은 변경가능, 

    // get''이라는 함수가 따로 있는 건가???
  getReadContent() {
    let i = 0;
    // contents : [ {id : 1, title : "HTML", desc : 'HTML is for Information.'},] => let data = this.state.contents[i]; =>  {this.props.title}
    while (i < this.state.contents.length) {
      let data = this.state.contents[i];
      // 둘다 똑같은 사전지정 state인데 i를 돌려서 나온 data의 id로 결정
      // data의 id props를 계속 돌리는데, 돌리는 와중에 미리 지정된 state의 selected contents id와 같으면
      if(data.id === this.state.selected_content_id) {
        // 그 시점의 data 값을 알려줘, data object index를 보여주는데 희안한게 왜 id는 안보여주지???
        return data;
        break;
      } i ++;
    }}

    // getContent 와 getRead content의 차이는? 왜 서로 분리해놨지? 보여주는 것과 다른 것?
    getContent() {
      // _title, desc은 입력값이라 알겠는데 article은 왜 필요할까? => article로 구현
      let _title, _desc, _article = null;
      let _content = this.getReadContent();
      // mode 입력값별 달리만들겠다.
      if (this.state.mode === 'welcome') {
        // _title은 별게 없고, Welcome의 title을 꺼내오는 것
        _title = this.state.Welcome.title;
        _desc = this.state.Welcome.desc;
        // 기본 홈 설정, i를 돌려서 맞는 값을 지정하겠다.
        // state - welcome - title, desc를 가져와 달라
        _article = <ReadContent title = {_title} desc = {_desc}></ReadContent>
        
      } else if (this.state.mode === 'read') {
        // mode마다 _article이 달라진다. article은 readcontent로 값이 변한다. i를 돌려서 맞는 값을 지정하겠다.
        _article = <ReadContent title = {_content.title} desc = {_content.desc}></ReadContent>

      } else if (this.state.mode === 'create') {
        _article = <CreateContent
          onSubmit = {function (_title, _desc) {
            // 도대체 뭔소리인지, 왜 +1을 하지? 새로 만든애를 추가하는 거였던거임,
            this.max_content_id = this.max_content_id + 1;
            // array 배열로 새로 만들어서 하나 꺼내오기
            let _contents = Array.from(this.state.contents);
            // 하위 컴포넌트의 입력값을 밀어넣어주기
            _contents.push({id : this.max_content_id, title : _title, desc : _desc});
            // state를 바꿀 때
            this.setState({
              // 새로 만들어진걸로 업데이트
              contents : _contents,
              // 모드는 read로 복귀
              mode:'read',
              // 보고 싶은 id
              selected_content_id : this.max_content_id
            });
          }.bind(this)}>
        </CreateContent>

        //클릭해서 update가 되면?
      } else if (this.state.mode === 'update') {
        // _content 가 grc 함수를 실행
        _content = this.getReadContent();
        //article은 updatecontent인데 
        _article = <UpdateContent
          // data 값은 read content이고, 이게 어떤 역할??
          data = {_content}
          //
          onSubmit = {function (_id, _title, _desc) {
            let _contents = Array.from(this.state.contents);
            let i = 0;
            while (i <_contents.length) {
              if (_contents[i].id === _id) {
                _contents[i] = {
                  id : _id, title : _title, desc : _desc };
                break;
              } i ++;
            }
            this.setState({
              contents : _contents,
              mode : 'read'
            });
          }.bind(this)}>
          </UpdateContent>
      } return _article;
    }

  render() {
    return (
      
      // div에 classNAme을 app으로 넣는게 무슨 의미지?
      <div className="App">
        {/* 여기서 state값과 component내 {this.props.title, sub}를 연결한다. */}
        {/* subject : { title : 'It\'s Web Pirate, Guys!' } => 하위값 title={상위값 this.state.subject.title} => {this.props.title} */}
        <Subject
          title = {this.state.subject.title}
          sub = {this.state.subject.sub}
          //onChangePage 이벤트 시 동작함수
          onChangePage = {function(){
            alert('It\'s a Trap!');
            this.setState({mode:'welcome'});
          }.bind(this)}>
          </Subject>

          <br/>

        <Subject
          onChangePage={function(){
            alert('It\'s a Trap!');
            this.setState({mode:'welcome'});
          }.bind(this)} 
          title = "Cool Guys!" sub = 'ㅋㅋㅋㅋ'> </Subject>

          <br/>
          <div id = 'App-div'>
        <Control onChangeMode = {function (_mode) {
          if (_mode === 'delete') {
            if (window.confirm('really')) {
              let _contents = Array.from(this.state.contents);
              let i = 0;
              while (i < _contents.length) {
                if(_contents[i].id === this.state.selected_content_id) {
                  _contents.splice(i, 1);
                  break;
                } i++;
              }
              this.setState({
                mode : 'welcome',
                contents : _contents
              })
              alert('delete')}
          } else {
            this. setState({mode : _mode})
          }}.bind(this)}>
        </Control>
        
        <br/>

        <TOC
          // 왜 id를 넣었을까?
          onChangePage={function(id) {
            alert('What\'up!');
            // state 변경이겠지?
            this.setState({
              mode:'read',
              // 무슨 역할을 할까?
              selected_content_id : Number(id)
            });}.bind(this)}
            // 하위 컴포넌트에서 지정한 값 불러내기
            // contents : [{id : 1, title : 'HTML', desc : "html is for information"}] => data = {this.state.contents} => {data[i].title}
            // contents는 배열, data는 contents를 그대로 불러냄, 값은 data[i] 인덱스의 title라는 props를 꺼냄
          data = {this.state.contents}>
        </TOC>

        <br/>

        {this.getContent()}
        </div>
      </div>
      )}}

export default App;

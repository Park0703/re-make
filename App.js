import React, { Component } from 'react'
import TOC from './components/TOC'
import ReadContent from './components/ReadContent'
import UpdateContent from './components/UpdateContent'
import CreateContent from './components/CreateContent'
import Subject from './components/Subject'
import Control from './components/Control'
import './App.css';

class App extends Component {
  constructor(props) {
    super(props) ;
    // 컴포넌트가 실행될때  render보다 먼저 실행하면서 그 컴포넌트를 초기화시켜주고 싶을때
    // constructor안에다가 코드 작성
    this.max_content_id = 3;
    this.state = {
    mode : "create",
    selected_content_id:2,
    subject : {
      title : 'fuck out', 
      sub : 'World wide web!'
    },
    welcome : {
      title : 'welcome', 
      sub : 'hello, react'
    },
    contents : [
      {id : 1, title : 'HTML', desc : "html is for information"},
      {id : 2, title : 'CSS', desc : "CSS is for design"},
      {id : 3, title : 'JS', desc : "html is for interactive"}
    ]}}// state 값을 초기화 시킴

    getReadContent() {
      let i = 0;
      while(i < this.state.contents.length) {
        let data = this.state.contents[i];
        if(data.id === this.state.selected_content_id) {
          return data; // 클릭했을때 페이지 넘겨주기
          break;
        }
        i = i+1;
    }}

    getContent(){
      let _title, _desc, _article = null;
      if (this.state.mode === 'welcome') {
        _title = this.state.welcome.title;
        _desc = this.state.welcome.desc;
        _article = <ReadContent title = {_title} desc={_desc}>
  
        </ReadContent>
      } else if (this.state.mode === 'read') {
        var _content = this.getReadContent();
        // mode가 welcome일때도, else if read 일때도 readcontent 유지
        _article = <ReadContent title = {_content.title} desc={_content.desc}></ReadContent>
  
      } else if (this.state.mode === 'create') {
        _article = <CreateContent onSubmit={function(_title, _desc){
          this.max_content_id = this.max_content_id + 1;
          // this.state.contents.push( // 이렇게 직접 수정하면 react가 인식할 수 없음 setState
          //   {id:this.max_content_id, title : _title, desc :_desc}
          //   ); // push는 성능 개선 시 굉장히 까다로움
        //   let _contents = this.state.contents.concat(
        //     {id:this.max_content_id, title : _title, desc :_desc})
           let _contents = Array.from(this.state.contents); // 얘도 원본 교체
           // 모든 데이터에 불변, immutatble. 
           _contents.push({id:this.max_content_id, title : _title, desc :_desc});
        this.setState({
              contents:_contents,
              mode:'read',
              selected_content_id:this.max_content_id
            }); // 추가의 좋은 방법은 concat이 더 좋음, 원본을 바꾸지 않기 때문, 새로운 배열을 return
          //새로운 content 추가
        //   object.assign({}, a); 
          console.log(_title, _desc);
        }.bind(this)}>
        </CreateContent>
  
      } else if (this.state.mode === 'update') {
        _content = this.getReadContent();
         _article = 
        <UpdateContent 
            data={_content} 
            onSubmit={function(_id, _title, _desc) {
               let _contents = Array.from(this.state.contents); // 배열을 만들어줌
               //오리지날 콘텐츠를 만들지 않고, 새로운 콘텐츠를 복제해서 만듬
               // => 원본을 바꾸지 않는 기법, 나중에 튜닝할때 필요함
               // 핵심은 복제를 한 애를 업데이트 값으로 집어넣는다.
               // this.max_content_id = this.max_content_id + 1; create할때나 값을 올리는 기능
               // let _Contents = this.state.contents.concat(
               //    {id:this.max_content_id, title : _title, desc :_desc});
               let i = 0;
               while (i<_contents.length) {
                  if(_contents[i].id === _id){
                     _contents[i] = {
                        id:_id, title:_title, desc:_desc};
                     break;
                  }
                  i++;  
               }
               this.setState({
                  contents:_contents,
                  mode:'read'
                  });
            console.log(_title, _desc);
            }.bind(this)}>

        </UpdateContent>
      }
      return _article;
    }

  render() {
    
    return (
      <div className="App">

        <Subject 
        title={this.state.subject.title} 
        sub={this.state.subject.sub} // 이렇게 불러옴
        onChangePage={function(){
          alert('hello');
          this.setState({mode:"welcome"});
        }.bind(this)} // onChangePage 로 이벤트 호출
        >
          </Subject> 

        <Subject title='props ㅈ듀' sub='sub라고 입력된 props'></Subject>
        
        <TOC 
          onChangePage={function(id){
            alert('hi');
            this.setState({
              mode:'read',
              selected_content_id:Number(id) //debugger로 state id값을 반영
            }); 
            // 다른 페이지 오픈하고 싶을 때 
          }.bind(this)}
        data={this.state.contents}>          
        </TOC>

        <Control onChangeMode= {function(_mode){
           if(_mode === 'delete') {
            if(window.confirm('really?')) { //확인을 누르면 컨펌이 true가 됨
               let _contents = Array.from(this.state.contents);
               let i = 0;
               while (i < _contents.length) {
                  if(_contents[i].id === this.state.selected_content_id) {
                     _contents.splice(i, 1); // 원하는 값을 제거한다.
                     break;
                  }
                  i ++;
               }
               this.setState({ // 삭제하고 나서 보여주고 싶은 것
                  mode:'welcome',
                  contents:_contents
               })
               alert('delete')
            }
           } else {

           
          this.setState({
            mode:_mode
          })}
        }.bind(this)}>
        </Control>

        {/* <ReadContent title = {_title} desc={_desc}></ReadContent> */}
        {this.getContent()}
      </div>
        )}}

export default App;



// 값 입력하기
// 1. 직접 입력 <h1> 내용 </h1>

// 2. 컴포넌트에 별도 지정 
// 상위 컴포넌트 내 내용으로 컴포넌트 입력 <subject title="내용"> 
// 내용 컴포넌트 내 원하는 내용 입력 title = {this.subject.title}

// 3. state로 전달 
// 상위 컴포넌트 constructor this.state={subject : {title : "내용"}}
// 컴포넌트 <Subject title={this.state.subject.title} state 불러오기
// 내용 컴포넌트 내 원하는 내용 입력 title = {this.subject.title}


// 역동성을 위한 events ex) 출력
// render 불러오기, 구현하기
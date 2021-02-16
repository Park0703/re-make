import React, { Component} from 'react'

class Subject extends Component {
   render() {

      return (

         // header 그냥 지정한 건데, div로 하면 안되나?
         <div id = 'article-div'>
         <header>
        {/* %% a의 기능은? href='/'이라 했는데 무슨기능? function에 빈 것과  e(event)의 차이 */}
            <h1>
               <a href="/{this.props.title}" onClick={function(e){
                  // props의 지정은 어디에?, 바꾸기? 어떤 동작을
                  // 동작은 상위 콤포넌트에서 지정함, 그럼 여기엔 왜 표시했지?
                  e.preventDefault();
                  this.props.onChangePage();
                  //bind(this)로 다시 묶어주기, onclick을 하면 이름없는 function이 실행되는데, 
                  //onChangePage인 props가 app에만 설명이 되있는데, app이 subject에게 props(title, sub, onChangePage)를 넘겨줬는데, 
                  // subject의 하위 a테그에 상위 props를 가지지 못하니
                  // bind는 한단계 상위 태그의 props를 가져오는거, this는 매개변수의 이름으로 묶는데, 흔히 말하는 this랑은
                  }.bind(this)}>
                     
                     <br/>
                     {this.props.title}
               </a>
            </h1>
               {/* this.props의 지정된 sub, component이니 최상위 component에서 props의 집합을 정의해줄 것이다. */}
                WEB PIRATE : {this.props.sub}
         </header>
         </div>
         );
      }
   }

export default Subject;

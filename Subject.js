import React, { Component } from 'react'

class Subject extends Component {
  render() {
    return (
      <header> 
        <h1><a href="/" onClick={function(e){
          console.log(e);
          // e.preventDefault();
          this.props.onChangePage();
          // this.state.mode = 'welcome'; // 함수형 실행으론 this를 알수없음
          // this.setState({ //thi.state.mode만 하면 react가 못알아먹음
          //   mode: "welcome" //react가 알아먹게 하기 위해서는 setState로 
          // }); //constructor는 편하게 해도 된다.
        }.bind(this)}> 
        {/* bind로 this를 component로 만들어 줘야함 */}
        {this.props.title}
        </a></h1> 
        {/* //refactoring */}
        {this.props.sub}
      </header>
    );
  }
}

export default Subject;
// 이벤트 걸때 그걸 못하게 하는 preventDefault();
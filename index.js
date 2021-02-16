// react에서 React library를 가져온다.
import React from 'react';
// %% react dom 부분 rendering
import ReactDOM from 'react-dom';
// app 매인 파일, 하위콤포넌트에서 app component를 가져온다
import App from './App';


// react dom으로 렌더링을 하고, class app component를 실행한다.
ReactDOM.render(
    <App />,
  // %% document가 뭐지? getElementbyId가 뭐지? id = root는 어디 지정 되어있지? 역할이 뭐지? react-dom의 root 라는 클래스네임을 가져옴, 
  document.getElementById('root')
);


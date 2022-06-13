# 피그마

- figma 링크 : [Django 프로젝트 - FigJam (figma.com)](https://www.figma.com/file/1MNv5IX3SogCRUtb0odNde/Django-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8?node-id=0%3A1)
- 초안  


    ![Django](https://user-images.githubusercontent.com/89643366/173344603-e0649fe5-6ae1-4eb1-a438-850811b5daba.png)

    
    ![Django2](https://user-images.githubusercontent.com/89643366/173346061-66b46868-7374-4e63-864d-dea2d90e3e45.png)


# 기능명세서

- 홈 페이지
    - 학습된 머신러닝 모델을 통해 평점이 높은 순서대로 영화가 랜덤으로 보여집니다.
    - 상단바의 [로고] [홈] [마이페이지] [로그인 or 로그아웃] click으로 해당 페이지로 이동합니다.
        - 로그인(인증)상태에 따라 로그인과 로그아웃이 번갈아가며 보여집니다.
    - 영화를 누르면 해당되는 영화의 상세 페이지로 이동합니다.
    
- 영화 상세 페이지
    - 상단 - 홈 페이지에서 누른 영화의 상세 내용[ 이미지 | 제목 | 장르 | 개요 ]을 보여줍니다.
    - 중간 - 리뷰 작성하기 버튼으로 모달창을 띄워 평점을 등록합니다.
    - 하단 - 학습된 머신러닝 모델을 이용하여 추천 영화들을 보여줍니다.
        - 내가 작성한 리뷰에서 평점이 높은 영화들의 태그들을 모델에 적용시킵니다.
        - 로그인(인증)상태가 되어있을 때에만 보여집니다. 미인증상태시, 추천영화는 랜덤으로 보여집니다.
        
- 내 평점 등록 - 모달
    - 평점을 등록할 영화의 제목이 보여지며, 평점은 range slider로 조절합니다.
    - 로그인(인증)상태가 되어있을 때에만 보여집니다.
        - 미인증상태시, ‘로그인이 필요한 작업입니다’ 에러메세지를 보여줍니다.
    
- 회원가입/로그인 페이지
    - 페이지 이름을 누르면 홈 페이지로 이동합니다.
    - 아이디와 비밀번호를 입력해 회원가입 또는 로그인을 할 수 있습니다.
    
- 마이 페이지
    - 로그인(인증)상태가 되어있을 때에만 접근이 가능합니다.
    - 로그인한 사용자가 작성한 영화 리뷰 리스트가 보여집니다.
    - 영화 리뷰 리스트의 구성 요소는 `영화 제목, 평점, 작성시간, 삭제 버튼` 입니다.
    - 페이지별 리스트을 보여주는 것이 아닌 스크롤 방식을 택해 사용자가 작성한 리스트를 보여줍니다.
    - (추가) 리스트의 영화 제목을 누르면 상세 페이지로 이동합니다.

# 컨벤션

### 💚 Git

- 브랜치 관리 전략 참고사항
    
    ![image](https://user-images.githubusercontent.com/89643366/169194210-7acb7256-91e9-43cd-b02f-8fbf30b829d6.png)
    
    ```jsx
    main(master) : 테스트 서버에서 테스트가 끝나고 운영서버로 배포 할 수 있는 브랜치
    feature : 기능을 개발하는 브랜치
    hotfix  : 운영중인 버전에서 발생한 버그를 수정 하는 브랜치
    ```
    
- 브랜치
    - user
    - post
    - movie
    - recommend

- 커밋 메세지

```jsx
Commit Type
- Feat : 새로운 기능 추가/수정/삭제
- Fix : 버그 수정
- Docs : 문서 수정
- Design : CSS 등 사용자 UI 디자인 변경
- Style: 코드에 영향을 주지 않는 변경사항 /  코드 포맷 변경, 새미 콜론 누락, 코드 수정이 없는 경우
- Comment : 필요한 주석 추가 및 변경
- Refactor: 코드 리팩토링
- Test: 테스트 코드/기능 추가
- Rename : 파일 혹은 폴더명을 수정하거나 옮기는 작업만인 경우
- Remove : 파일을 삭제하는 작업만 수행한 경우

Subject
- 50자를 넘기지 않고, 커밋 타입을 준수함.

 Body
- 72자를 넘기지 않고, 모든 커밋에 본문 내용을 작성할 필요는 없음.
```

### 💚 코드

- Frontend
    
    ```html
    클래스명(- 사용) : form-control  
    아이디명(카멜 케이스) : navbarNav
    따옴표 : ""
    요소의 속성(큰 따옴표) : type="button"
    하이퍼링크 : 사용시 a 태그 포함
    img 태그 : alt="" 꼭 표시
    ```
    
- JavaScript
    
    <aside>
    💡 Ex) mac book, num
    
    1. 파스칼 케이스 : MacBook, Num
    
    2. 카멜 케이스 : macBook, num
    
    3. 스네이크 케이스 : _macBook, _num
    
    4. 헝가리안 케이스 : isMacBook, isNum, strMacBook, strNum
    
    </aside>
    
    <aside>
    💡 1. 파스칼 케이스
    
    </aside>
    
    ```jsx
    // 클래스
    class MyStudent {
    		...
    };
    ```
    
    ```jsx
    // 객체를 export 할 때
    const MyObject = {
    		...
    };
    export default MyObject;
    ```
    
    <aside>
    💡 2. 카멜 케이스
    
    </aside>
    
    ```jsx
    // 변수와 상수
    let num = 123;
    let str = 'hello';
    
    // 함수
    function myFunction() {
    	...
    }
    
    // 객체
    const thisIsMyObject = {
    	...
    };
    ```
    
- Python
    
    <aside>
    💡 1. 일반 변수
    
    </aside>
    
    ```python
    a = 'MacBook'
    
    # 스네이크 케이스
    my_num = 3
    ```
    
    <aside>
    💡 2. 함수
    
    </aside>
    
    ```python
    def get_user_info():
      ...
    ```
    
    <aside>
    💡 3. 클래스
    
    </aside>
    
    ```python
    # 첫 글자 대문자
    class CatchFish():
    	...
    ```
    

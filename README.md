# 🎬 프로젝트 주제

### 개인별 맞춤 영화 추천 서비스
: 사용자가 작성한 영화 리뷰를 토대로 영화를 추천

<br>

# ⚙ 개발환경
## back-end : <img src="https://img.shields.io/badge/python-3.8.6-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">

## front-end : <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> 

<br>

## 기능명세서

- 상단바
    - 상단바의 [로고] [검색] [마이페이지] [로그인 or 로그아웃] click으로 해당 페이지로 이동합니다.
        - 로그인(인증)상태에 따라 로그인과 로그아웃이 번갈아가며 보여집니다.
    - 검색창의 검색어를 포함한 영화를 검색합니다.
    
- 아이템 협업 필터링
    - 선호하는 영화를 체크하여 학습된 머신러닝 모델으로 유사도를 계산합니다.
    
- 메인 페이지
    - 아이템 협업 필터링의 결과값이 보여집니다.
    - 높은 평점 위주의 영화를 랜덤으로 보여집니다.
        - 영화 이미지-제목-tag를 확인합니다.
    - 영화를 누르면 해당 영화의 상세 페이지로 이동합니다.
    - Tag 이름을 누르면 Tag에 포함된 영화들만 보여집니다.
    
- 영화 상세 페이지
    - 상단 - 홈 페이지에서 누른 영화의 상세 내용[ 이미지 | 제목 | 장르 | 개요 ]을 보여집니다.
    - 중간 - 리뷰 작성하기 버튼으로 평점을 등록합니다.
    - 하단 - 학습된 머신러닝 모델을 이용하여 추천 영화들을 보여집니다.
        - 상단에서 보여지는 영화와 중복되지 않은 영화들을 랜덤으로 보여집니다.
        - 영화를 클릭시 해당 영화의 상세 페이지로 이동합니다.
        - 로그인(인증)상태가 되어있을 때에만 보여집니다. 미인증상태시, 추천영화는 랜덤으로 보여집니다.
        
- 내 평점 등록 및 수정
    - 평점을 등록할 영화의 제목이 보여지며, 평점은 range slider로 조절합니다.
    - 로그인(인증)상태가 되어있을 때에만 보여집니다.
        - 미인증상태시, ‘로그인이 필요한 작업입니다’ 에러메세지를 나타냅니다.
    - 평점 및 리뷰를 수정할 때 다음과 같이 작동합니다.
        - 평점 수정 o, 리뷰 수정 o
        - 평점 수정 o, 리뷰 수정 x
        - 평점 수정 x, 리뷰 수정 o
        - 평점 수정 x, 리뷰 수정 x (해당 경우, `내용수정이 완료되지 않았습니다` 라는 에러 메세지를 나타냅니다.)
    - 취소 키를 누르면 마이페이지로 이동하게 되고, 작성 버튼을 누르면 게시글이 작성된 후 마이페이지로 이동합니다.
    
- 회원가입/로그인 페이지
    - 로고를 누르면 홈 페이지로 이동합니다.
    - 아이디와 비밀번호를 입력해 회원가입 또는 로그인을 할 수 있습니다.
        - 회원가입은 아이디와 패스워드가 6자리 이상 이여야 가능합니다.
        - 아이디가 중복되면 회원가입이 불가합니다.
    - 로그인이 된 상태에선 회원가입/로그인 페이지에 접속이 불가합니다.
    
- 신규회원 - 영화 선호도 체크 페이지
    - tag 1개 당 평점이 가장 높은 영화를 하나씩 보여줍니다.
    - 원하는 영화가 없을시 새로고침을 통해서 새로운 영화를 랜덤으로 보여줍니다.
    - 영화를 선택 후 OK 버튼을 클릭하여 메인페이지로 이동합니다.
    - 선택 없이 OK버튼 클릭하면 ‘영화를 선택해주세요’ 메세지와 함께 선호도 체크 첫 화면으로 돌아갑니다.
    
- 마이 페이지
    - 로그인(인증)상태가 되어있을 때에만 접근이 가능합니다.
    - 로그인한 사용자(작성자)의 작성한 영화 리뷰 리스트가 보여집니다.
    - 영화 리뷰 리스트의 구성 요소는 `영화 제목, 평점, 작성시간, 수정, 삭제 버튼` 입니다.
    - 페이지별 리스트을 보여주는 것이 아닌 스크롤 방식으로 작성된 리뷰 리스트를 볼 수 있습니다.

## API 명세서
![image](https://user-images.githubusercontent.com/104754104/185304655-bb3b9c48-bf96-4b65-9e87-e41cfb916ab0.png)

## DATABASE
<img width="869" alt="스크린샷 2022-08-18 오후 2 32 37" src="https://user-images.githubusercontent.com/99387514/185301691-43d8d591-3e61-4a5f-bb02-96506e20f3f4.png">

## 와이어프레임
<details>
<summary>
    click!
</summary>

![image](https://user-images.githubusercontent.com/89643366/173344603-e0649fe5-6ae1-4eb1-a438-850811b5daba.png)

![image](https://user-images.githubusercontent.com/89643366/173346061-66b46868-7374-4e63-864d-dea2d90e3e45.png)

</details> 


## 컨벤션

### 💚 Git
    
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
- Add : 새로운 파일 추가
- Refactor: 코드 리팩토링
- Test: 테스트 코드/기능 추가
- Rename : 파일 혹은 폴더명을 수정하거나 옮기는 작업만인 경우
- Remove : 파일을 삭제하는 작업만 수행한 경우

Subject
- 50자를 넘기지 않고, 커밋 타입을 준수함.

 Body
- 72자를 넘기지 않고, 모든 커밋에 본문 내용을 작성할 필요는 없음.
```

    

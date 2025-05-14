# chorongyi 

## Hecto AI Challenge
>중고차 이미지를 분석해 차종을 분류하는 AI 모델 개발 </br>
>핵심 기능만 구현한 MVP 모델 목표


## Architecture
### Server Architecture

[//]: # (<!-- 아키텍처 이미지 그려서 넣을 예정 -->)


## Tech Stack

- Python, FastAPI, SQLAlchemy, Pixi
- PyTorch, Cuda
- PostgreSQL, Docker
- React

## Developer

|                 |   | |
| --- | --- | --- |
| [양원준(yangwonjoon)](https://github.com/yangwonjoon) | [김소은]() | [이선호(08166)](https://github.com/08166) |
| mvp ~ front ~ AI  |  mvp ~ backend ~ AI  | mvp ~ backend ~ AI |


## Convention

## Commit

| 태그 이름  | 설명                            |
|-----------|-------------------------------|
| FEAT      | 새로운 기능 추가 |
| FIX       | 버그 수정 |
| CHORE     | 미세한 수정 |
| DOCS      | 문서 수정 |
| INIT      | 초기 설정 |
| TEST      | 테스트 코드, 리팩토링 테스트 코드 추가 |
| RENAME    | 파일 혹은 폴더명을 수정하거나 옮겼을 경우 | 
| STYLE     | 코드 포맷팅, 코드 변경이 없는 경우 |
| REFACTOR  | 코드 리팩토링 |

## Branch

![Git Flow](https://raw.githubusercontent.com/yumyumpot/chorongyi/main/ai/docs/chorong.png)

- **main** : 운영 서버(Production)에 배포 브랜치
- **develop** : 개발이 완료된 후 테스트 개발 서버(Develop) 브랜치
- **feature** : 각 기능을 개발하는 브랜치, 기능 개발 단위로 브랜치 생성 {CHORONG-001}

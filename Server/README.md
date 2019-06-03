Server

Django Rest Framework Ver 1.1

현재 새로운 DB에 맞게 Django 연동 되어 있다.

앞으로 비교 알고리즘을 가중치에 맞게 개선해야 하고

앱과의 POST연동을 해야한다.


Django Rest Framework Ver 2.0 (2019.05.30)_

POST 연동 완료
비교 알고리즘 개선 필요


Django Rest Framework Ver 2.1 (2019.05.31)

1차, 2차 레시피 검색 모두 POST 연동 완료
(DirView라는 DB View를 새로 생성)

레시피 최대 출력 개수 20개로 맞춤

비교 알고리즘 개선 필요
(1. 주재료/부재료 구분)
(2. 재료 비율에 따라 출력)
(3. 최소 레시피 10개)


Django Rest Framework Ver 2.2 (2019.06.03)

오늘의 레시피 구현 완료
주재료/부재료 구분 완료
재료 비율에 따라 출력하기 완료
레시피 이름에 사용자의 재료가 나타나 있으면 우선순위로 출력
(직관성과 대표성 강화)
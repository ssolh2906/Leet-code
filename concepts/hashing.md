# Hashing (set / dict 내부 동작)

> 위치: `Leet-code/concepts/hashing.md`

## 한 줄 요약
- list `in` = 줄 서서 한 명씩 확인 → O(n)
- set `in` = 좌석 번호표 보고 바로 그 자리로 → O(1)
- 차이는 해싱

## 핵심
- Python `set`, `dict` = hash table 구현
- `index = hash(x) % capacity` 로 저장/조회 위치를 한 번에 계산 → O(1)
- collision(같은 칸 충돌) 때문에 엄밀히는 **평균 O(1), 최악 O(n)**

## bucket 사이즈 / resize (걍 굼굼해서 물어봤음)
- load factor(적재율)가 임계치(dict ≈2/3, set ≈3/5) 넘으면 배열 2~4배로 키우고 rehash
- 늘 30~40% 빈 공간 유지 → collision 억제
- resize 1회는 O(n)이지만 자주 안 일어남 → insertion은 **amortized O(1)**

## trade-off
빈 공간 유지 = 메모리 ↑, 속도 ↑ (메모리를 희생해 O(1) 확보)

## 적용 패턴
중복/존재 확인, Two Sum, 빈도 세기(`Counter`) 등 Arrays & Hashing 전반

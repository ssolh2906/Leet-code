# 01. Arrays & Hashing — 패턴 노트

> 위치: `Leet-code/01_Arrays_and_hashing/_notes.md`
> 패턴별 폴더마다 이 `_notes.md` 하나씩 두기. 문제 풀고 핵심 트릭 한 줄씩 적립.

## 패턴 핵심
- HashMap / HashSet 으로 조회를 O(1)로 → 전체 O(n)
- "이미 본 값을 기억"하는 게 기본 발상
- 빈도는 `collections.Counter`, 존재 확인은 `set`

## 문제별 메모
| # | 문제 | 핵심 트릭 | 시간 | 다시 볼 것 |
|---|------|----------|------|-----------|
| 217 | Contains Duplicate | set에 넣으며 `if n in s` 존재 확인 → 중복 시 True | O(n) | ✅ || 1 | Two Sum | 보수(target-n)를 dict에 저장하며 조회 | O(n) | |
| 242 | Valid Anagram | hashing(char count)으로 잘 풀었음 → 맨 앞에 `len` 체크 넣으면 더 좋음. `Counter(s)==Counter(t)` 한 줄도 가능 | O(n) | ✅ |
| 49 | Group Anagrams | 정렬한 문자열을 key로 dict 그룹핑 | | |
| 347 | Top K Frequent | Counter + bucket sort | | |
| 238 | Product Except Self | prefix * suffix, 나눗셈 없이 | | |
| 271 | Encode/Decode Strings | 길이+구분자 프로토콜 | | |
| 128 | Longest Consecutive | set에 넣고 시퀀스 시작점만 확장 | | |

## 복습 체크 (spaced repetition)
- [ ] 1차 풀이
- [ ] 며칠 뒤 아무것도 안 보고 재구현
- [ ] 친구에게 말로 설명

## 347
default dict 밸류로 sorting 하기:  
```
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
```

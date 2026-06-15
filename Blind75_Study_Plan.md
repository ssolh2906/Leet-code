# Blind 75 — 패턴별 학습 플랜 & 트래커

> **목표:** 여름방학 동안 Blind 75 완주
> **친구와 약속:** 주 최소 1문제 (안전장치)
> **실제 권장 페이스:** 주 6~7문제 → 약 11~12주 완주
> **언어 추천:** Python (`collections`, `heapq` 익혀두면 면접·연구에 그대로 쓰임)

**진행법:** 20~30분 혼자 고민 → 안 풀리면 solution 보고 이해 → 아무것도 안 보고 다시 구현 → 며칠 뒤 재복습. 문제마다 "핵심 트릭 한 줄"을 메모하면 그게 패턴 감각이 됩니다.

체크박스: `[ ]` 나 / `[ ]` 친구 — 둘 다 풀면 서로 설명해주기.

---

## 1. Arrays & Hashing (8)
> 핵심: HashMap/HashSet으로 O(n) 조회. 가장 기초, 여기서 자신감 쌓기.

- [v] **#1** Two Sum · Easy · https://leetcode.com/problems/two-sum/
- [ ] **#217** Contains Duplicate · Easy · https://leetcode.com/problems/contains-duplicate/
- [ ] **#242** Valid Anagram · Easy · https://leetcode.com/problems/valid-anagram/
- [ ] **#49** Group Anagrams · Med · https://leetcode.com/problems/group-anagrams/
- [ ] **#347** Top K Frequent Elements · Med · https://leetcode.com/problems/top-k-frequent-elements/
- [ ] **#238** Product of Array Except Self · Med · https://leetcode.com/problems/product-of-array-except-self/
- [ ] **#271** Encode and Decode Strings · Med 🔒 · https://leetcode.com/problems/encode-and-decode-strings/
- [ ] **#128** Longest Consecutive Sequence · Med · https://leetcode.com/problems/longest-consecutive-sequence/

## 2. Two Pointers (3)
> 핵심: 정렬된 배열에서 양끝 포인터를 좁혀가며 O(n).

- [ ] **#125** Valid Palindrome · Easy · https://leetcode.com/problems/valid-palindrome/
- [ ] **#15** 3Sum · Med · https://leetcode.com/problems/3sum/
- [ ] **#11** Container With Most Water · Med · https://leetcode.com/problems/container-with-most-water/

## 3. Sliding Window (4)
> 핵심: 윈도우를 늘리고/줄이며 부분배열·부분문자열 최적화.

- [ ] **#121** Best Time to Buy and Sell Stock · Easy · https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- [ ] **#3** Longest Substring Without Repeating Characters · Med · https://leetcode.com/problems/longest-substring-without-repeating-characters/
- [ ] **#424** Longest Repeating Character Replacement · Med · https://leetcode.com/problems/longest-repeating-character-replacement/
- [ ] **#76** Minimum Window Substring · Hard · https://leetcode.com/problems/minimum-window-substring/

## 4. Stack (1)
> 핵심: LIFO. 괄호 매칭, monotonic stack.

- [ ] **#20** Valid Parentheses · Easy · https://leetcode.com/problems/valid-parentheses/

## 5. Binary Search (2)
> 핵심: 정렬/회전 배열에서 O(log n). 경계 조건 주의.

- [ ] **#153** Find Minimum in Rotated Sorted Array · Med · https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
- [ ] **#33** Search in Rotated Sorted Array · Med · https://leetcode.com/problems/search-in-rotated-sorted-array/

## 6. Linked List (6)
> 핵심: 포인터 조작, dummy node, fast/slow 포인터.

- [ ] **#206** Reverse Linked List · Easy · https://leetcode.com/problems/reverse-linked-list/
- [ ] **#21** Merge Two Sorted Lists · Easy · https://leetcode.com/problems/merge-two-sorted-lists/
- [ ] **#141** Linked List Cycle · Easy · https://leetcode.com/problems/linked-list-cycle/
- [ ] **#143** Reorder List · Med · https://leetcode.com/problems/reorder-list/
- [ ] **#19** Remove Nth Node From End of List · Med · https://leetcode.com/problems/remove-nth-node-from-end-of-list/
- [ ] **#23** Merge k Sorted Lists · Hard · https://leetcode.com/problems/merge-k-sorted-lists/

## 7. Trees (11)
> 핵심: DFS(재귀)/BFS(큐). 트리는 거의 다 재귀로 풀림.

- [ ] **#226** Invert Binary Tree · Easy · https://leetcode.com/problems/invert-binary-tree/
- [ ] **#104** Maximum Depth of Binary Tree · Easy · https://leetcode.com/problems/maximum-depth-of-binary-tree/
- [ ] **#100** Same Tree · Easy · https://leetcode.com/problems/same-tree/
- [ ] **#572** Subtree of Another Tree · Easy · https://leetcode.com/problems/subtree-of-another-tree/
- [ ] **#235** Lowest Common Ancestor of a BST · Med · https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
- [ ] **#102** Binary Tree Level Order Traversal · Med · https://leetcode.com/problems/binary-tree-level-order-traversal/
- [ ] **#98** Validate Binary Search Tree · Med · https://leetcode.com/problems/validate-binary-search-tree/
- [ ] **#230** Kth Smallest Element in a BST · Med · https://leetcode.com/problems/kth-smallest-element-in-a-bst/
- [ ] **#105** Construct Binary Tree from Preorder and Inorder · Med · https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
- [ ] **#124** Binary Tree Maximum Path Sum · Hard · https://leetcode.com/problems/binary-tree-maximum-path-sum/
- [ ] **#297** Serialize and Deserialize Binary Tree · Hard · https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

## 8. Tries (3)
> 핵심: 접두사 트리. 문자열 검색·자동완성.

- [ ] **#208** Implement Trie (Prefix Tree) · Med · https://leetcode.com/problems/implement-trie-prefix-tree/
- [ ] **#211** Design Add and Search Words Data Structure · Med · https://leetcode.com/problems/design-add-and-search-words-data-structure/
- [ ] **#212** Word Search II · Hard · https://leetcode.com/problems/word-search-ii/

## 9. Heap / Priority Queue (1)
> 핵심: `heapq`. 두 개의 heap으로 median 유지.

- [ ] **#295** Find Median from Data Stream · Hard · https://leetcode.com/problems/find-median-from-data-stream/

## 10. Backtracking (2)
> 핵심: 선택 → 재귀 → 선택 취소(undo). 모든 경우의 수 탐색.

- [ ] **#39** Combination Sum · Med · https://leetcode.com/problems/combination-sum/
- [ ] **#79** Word Search · Med · https://leetcode.com/problems/word-search/

## 11. Graphs (7)
> 핵심: DFS/BFS, visited 집합, 위상정렬(topological sort), union-find.

- [ ] **#200** Number of Islands · Med · https://leetcode.com/problems/number-of-islands/
- [ ] **#133** Clone Graph · Med · https://leetcode.com/problems/clone-graph/
- [ ] **#417** Pacific Atlantic Water Flow · Med · https://leetcode.com/problems/pacific-atlantic-water-flow/
- [ ] **#207** Course Schedule · Med · https://leetcode.com/problems/course-schedule/
- [ ] **#261** Graph Valid Tree · Med 🔒 · https://leetcode.com/problems/graph-valid-tree/
- [ ] **#323** Number of Connected Components in an Undirected Graph · Med 🔒 · https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
- [ ] **#269** Alien Dictionary · Hard 🔒 · https://leetcode.com/problems/alien-dictionary/

## 12. 1-D Dynamic Programming (10)
> 핵심: 점화식 세우기. 작은 문제 → 큰 문제. 가장 중요한 패턴.

- [ ] **#70** Climbing Stairs · Easy · https://leetcode.com/problems/climbing-stairs/
- [ ] **#198** House Robber · Med · https://leetcode.com/problems/house-robber/
- [ ] **#213** House Robber II · Med · https://leetcode.com/problems/house-robber-ii/
- [ ] **#5** Longest Palindromic Substring · Med · https://leetcode.com/problems/longest-palindromic-substring/
- [ ] **#647** Palindromic Substrings · Med · https://leetcode.com/problems/palindromic-substrings/
- [ ] **#91** Decode Ways · Med · https://leetcode.com/problems/decode-ways/
- [ ] **#322** Coin Change · Med · https://leetcode.com/problems/coin-change/
- [ ] **#152** Maximum Product Subarray · Med · https://leetcode.com/problems/maximum-product-subarray/
- [ ] **#139** Word Break · Med · https://leetcode.com/problems/word-break/
- [ ] **#300** Longest Increasing Subsequence · Med · https://leetcode.com/problems/longest-increasing-subsequence/

## 13. 2-D Dynamic Programming (2)
> 핵심: 2차원 DP 테이블. grid / 두 문자열 비교.

- [ ] **#62** Unique Paths · Med · https://leetcode.com/problems/unique-paths/
- [ ] **#1143** Longest Common Subsequence · Med · https://leetcode.com/problems/longest-common-subsequence/

## 14. Greedy (2)
> 핵심: 매 순간 국소 최적 선택. Kadane's algorithm.

- [ ] **#53** Maximum Subarray · Med · https://leetcode.com/problems/maximum-subarray/
- [ ] **#55** Jump Game · Med · https://leetcode.com/problems/jump-game/

## 15. Intervals (5)
> 핵심: 시작점 기준 정렬 후 겹침 처리.

- [ ] **#57** Insert Interval · Med · https://leetcode.com/problems/insert-interval/
- [ ] **#56** Merge Intervals · Med · https://leetcode.com/problems/merge-intervals/
- [ ] **#435** Non-overlapping Intervals · Med · https://leetcode.com/problems/non-overlapping-intervals/
- [ ] **#252** Meeting Rooms · Easy 🔒 · https://leetcode.com/problems/meeting-rooms/
- [ ] **#253** Meeting Rooms II · Med 🔒 · https://leetcode.com/problems/meeting-rooms-ii/

## 16. Math & Geometry (3)
> 핵심: 행렬 회전·순회, in-place 조작.

- [ ] **#48** Rotate Image · Med · https://leetcode.com/problems/rotate-image/
- [ ] **#54** Spiral Matrix · Med · https://leetcode.com/problems/spiral-matrix/
- [ ] **#73** Set Matrix Zeroes · Med · https://leetcode.com/problems/set-matrix-zeroes/

## 17. Bit Manipulation (5)
> 핵심: XOR, 비트 시프트, 마스킹.

- [ ] **#191** Number of 1 Bits · Easy · https://leetcode.com/problems/number-of-1-bits/
- [ ] **#338** Counting Bits · Easy · https://leetcode.com/problems/counting-bits/
- [ ] **#190** Reverse Bits · Easy · https://leetcode.com/problems/reverse-bits/
- [ ] **#268** Missing Number · Easy · https://leetcode.com/problems/missing-number/
- [ ] **#371** Sum of Two Integers · Med · https://leetcode.com/problems/sum-of-two-integers/

---

## 📅 12주 추천 스케줄 (주 6~7문제)

| 주차 | 패턴 | 문제 수 |
|------|------|--------|
| 1 | Arrays & Hashing | 8 |
| 2 | Two Pointers + Sliding Window | 7 |
| 3 | Stack + Binary Search + Linked List | 9 |
| 4 | Trees (1/2) | 6 |
| 5 | Trees (2/2) + Tries | 8 |
| 6 | Heap + Backtracking + Graphs (1/2) | 6 |
| 7 | Graphs (2/2) | 5 |
| 8 | 1-D DP (1/2) | 5 |
| 9 | 1-D DP (2/2) + 2-D DP | 7 |
| 10 | Greedy + Intervals | 7 |
| 11 | Math & Geometry + Bit Manipulation | 8 |
| 12 | 복습 + 틀렸던 문제 재도전 (spaced repetition) | — |

> 🔒 = LeetCode Premium 잠금 문제. 무료로 풀려면 NeetCode 또는 LintCode에서 같은 문제 검색하세요.

## 친구와 함께 (이게 핵심 강점)
- 각자 푼 문제를 **말로 설명** → 설명 못 하면 이해 못 한 것
- 같은 문제 각자 풀고 접근법 / 시간복잡도 비교
- 주 1회 짧게 통화해서 막힌 부분 공유

## ML / Bioinformatics 관점
면접 빈출도 높은 **Arrays & Hashing, Two Pointers, Trees, Graphs, DP**에 비중을 더 두세요.

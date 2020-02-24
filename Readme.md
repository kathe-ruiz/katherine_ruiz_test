# Katherine Ruiz - Test
## Question A
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the
x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5)
and (6,8).

#### Example
```
cd QuestionA
python Overlap.py
>>>please text x1:
1
>>>please text x2:
5
>>>please text x3:
3
>>>please text x4:
7
Lines are Overlap
```

## Question B
The goal of this question is to write a software library that accepts 2 version string as input and
returns whether one is greater than, equal, or less than the other. As an example: “1.2” is
greater than “1.1”. Please provide all test cases you could think of.

#### Example

```
cd QuestionB
python CompareVersions.py
>>>please text version 1
1.2
>>>please text version 2
1.4
>>>version 1: 1.2 is less than version 2: 1.4
```

## Question C

We want to optimize every bits of software we write. Your goal is to write a new library that can
be integrated to our stack. Dealing with network issues everyday, latency is our biggest problem.
Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with
time expiration. This library will be used extensively by many of our services so it needs to meet

### Solution

The proposed solution is to handle the data with a hastable structure (dictionary) and a deque,  that will allow to implement the LRU eviction Policy, the cache values has also the possibility to handle time expiration, and it handle network failures within a temporatly log file, so when the sever is restart, it can retreive the latest data:
 
### Example

```
>>>from LRUCache import LRUCache
>>>lru = LRUCache(5)
>>>lru.put(151,492)
>>>lru.put(122,600)
>>>lru.put(23,123,60) # this value will have a TTL of 60 seg
>>>lru.get(151)
492
```

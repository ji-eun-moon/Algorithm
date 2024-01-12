from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        # cache hit
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        # cache miss
        else:
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
            answer += 5

    return answer

print('#1', solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print('#2', solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print('#3', solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print('#4', solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print('#5', solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print('#6', solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
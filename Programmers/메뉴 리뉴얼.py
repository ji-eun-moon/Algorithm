from itertools import combinations
def solution(orders, course):
    answer = []

    # 주문한 메뉴로 만들 수 있는 모든 조합을 만들고, 조합별 카운트 + 1
    menus = {cnt:{} for cnt in course}  # {코스종류 : { 코스구성 : 주문수 } }
    for order in orders:
        for cnt in course:
            for combi in combinations(order, cnt):
                menu = ''.join(sorted(combi))
                menus[cnt].setdefault(menu, 0)  # 키 에러 방지 - 초기 주문수 0으로 초기화
                menus[cnt][menu] += 1

    for cnt in course:
        # course cnt 별 메뉴를 cnt 내림차순 으로 정렬
        new_menu = sorted(menus[cnt].items(), key=lambda x:x[1], reverse=True)
        if new_menu:
            # 정렬한 new_menu의 첫 번째 코스 메뉴의 주문 수가 가장 많은 주문 수
            max_cnt = new_menu[0][1]
            # 최소 2명 이상의 손님으로부터 주문된 코스 메뉴이어야 한다.
            if max_cnt >= 2:
                # 가장 많은 주문 수로 이루어진 코스 메뉴 리스트 생성하고 answer에 추가
                new_menus = [menu[0] for menu in new_menu if menu[1] == max_cnt]
                answer += new_menus

    return sorted(answer)

print('#1', solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print('#2', solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print('#3', solution(["XYZ", "XWY", "WXA"], [2,3,4]))
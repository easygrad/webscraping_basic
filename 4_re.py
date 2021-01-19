import re
# 차량번호는 네 자리 글자 abcd, efgh
# ca?e
# care, cafe, case ...

p = re.compile("ca.e") 
# .(ca.e): 하나의 문자를 의미(한 글자)
# ^(^de): 문자열의 시작을 의미 ex) desk, destination
# $(se$): 문자열의 끝을 의미 ex) case, base

def print_match(m):
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string:", m.string) # 입력받은 문자열
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span():", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")

# m = p.match("careless") # match: 주어진 문자열의 처음부터 일치하는지 확인(뒷부분은 다른게 있어도 노상관)
# print_match(m)

# m1 = p.search("goodcare") # search: 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m1)

lst = p.findall("good care cafe") # findall: 일치하는 모든 것을 리스트 형태로 반환
print(lst)
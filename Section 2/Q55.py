원판의이동경로 = []
def 하노이(원반의수, 시작기둥, 목표기둥, 보조기둥):
    if 원반의수 == 1:
        원판의이동경로.append([시작기둥, 목표기둥]) 
        return None
    하노이(원반의수-1,시작기둥,보조기둥,목표기둥)
    원판의이동경로.append([시작기둥, 목표기둥]) 
    하노이(원반의수-1,보조기둥,목표기둥,시작기둥)

user_input = int(input())
하노이(user_input,'A','C','B')

print(len(원판의이동경로))
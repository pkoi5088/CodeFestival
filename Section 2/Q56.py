nationWidth = {
    'korea': 220877,
    'Rusia': 17098242,
    'China': 9596961,
    'France': 543965,
    'Japan': 377915,
    'England' : 242900,
}

kWidth=nationWidth['korea']
nationWidth.pop('korea')
nations=list(nationWidth.items())
idx=0
for i in range(len(nations)):
    if abs(nations[idx][1]-kWidth)>abs(nations[i][1]-kWidth):
        idx=i
print(nations[idx][0],abs(nations[idx][1]-kWidth))
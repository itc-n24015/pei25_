list_b = []

for i in range(5, 26): 
    if i % 2 == 1:       
        list_b.append(i)

total = sum(list_b)

print("奇数リスト:", list_b)
print("合計:", total)

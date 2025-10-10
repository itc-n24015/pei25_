phrase = 'PythonProgramimming'
list_p = [] # 空のリストを作成
for p in phrase: # 繰り返しで一文字ずつ検査
    if p not in list_p: # pがlist_pにまだ含まれてなければ
        list_p.append(p) # list_pにpを追加
print(len(phrase) - len(list_p)) # 17-11=6つまり重複した文字の数

for p in list_p: 
    print(p, end=""0

print()


# 比較運算子
print(1 == 1)  # True
print(1 != 1)  # False
print(1 > 1)  # False
print(1 < 1)  # False
print(1 >= 1)  # True
print(1 <= 1)  # True

##邏輯運算子
##and運算子
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

##not運算子
print(not True)  # False
print(not False)  # True

##or運算子
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# 優先順序
# 1.()括號
# 2.**次方
# 3. * / // % 乘法 除法 整數除法
# 4. + - 加減
# 5.==,!=, >, <, >=, <= 比較運算子
# 6.not
# 7. and
# 8. or

# 密碼門檢查
password = input("請輸入密碼：")
if password == "1234":
    print("歡迎Jeffrey")
elif password == "5678":
    print("歡迎Mary")
elif password == "orion0715":
    print("歡迎orion")
elif password == "abcd":
    print("歡迎Tom")
else:
    print("密碼錯誤")
# 連續使用if跟使用if elif else的差別
# elif可以排除前面有判斷過的條件，所以縮短判斷條件的複雜度，也節省了時間
# 但是如果是連續使用if，則每個條件都會被判斷一次，可能會浪費時間

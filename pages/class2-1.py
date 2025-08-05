# 比較運算值
print(1 == 1)  # True
print(1 != 1)  # False
print(1 < 1)  # False
print(1 > 1)  # False
print(1 <= 1)  # True
print(1 >= 1)  # True

# # 邏輯運算值
print(True and True)  # True
print(True and False)  # False
print(False and False)  # False
print(False or False)  # False

# # or 運算值
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# # not 運算值
print(not True)  # False
print(not False)  # True

# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減
# 5. == != < > <= >= 比較運算
# 6. not
# 7. and
# 8. or

# # 密碼門檢查
password = input("請輸入密碼:")
if password == "1234":
    print("welcome Leo")
elif password == "12345":
    print("welcome tim")
elif password == "123456":
    print("welcome jack")
else:
    print("密碼錯誤，請重新輸入")
# 連續使用if跟使用if elif else的差別
# elif可以排除前面有判斷過的條件，所以縮短判斷條件的複雜度，也節省了時間
# 但是如果是使用多個if來做獨立判斷，則每個if都會被執行，所以效率較低

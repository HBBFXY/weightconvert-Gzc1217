rate = 2.2046
choice = int(input("1: 千克转磅 2: 磅转千克"))
if choice == 1:
    kg = float(input("请输入千克数："))
    pb = kg * rate
    print("转换后的磅数为：", pb)
elif choice == 2:
    pb = float(input("请输入磅数："))
    kg = pb / rate
    print("转换后的千克数为：", kg)
else:
    print("输入错误")
    exit()

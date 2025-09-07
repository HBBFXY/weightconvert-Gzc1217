weight_str = input().strip()
num = float(weight_str[:-2])
unit = weight_str[-2:]
kg_to_pd = 2.2046
if unit == 'kg':
    converted = num * kg_to_pd
    print(f"对应的英制重量为{converted:.3f}磅")
elif unit == 'pd':
    converted = num / kg_to_pd
    print(f"对应的公制重量为{converted:.3f}千克")

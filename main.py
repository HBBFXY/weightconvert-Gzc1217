weight_input = input()
value = float(weight_input[:-2])
unit = weight_input[-2:]
kg_to_pd = 2
if unit == "kg":
    result = value * kg_to_pd
    print(f"对应的英制重量为{result:.3f}磅")
elif unit == "pd":
    result = value / kg_to_pd
    print(f"对应的公制重量为{result:.3f}千克")

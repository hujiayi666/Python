"""输入顾客所购商品的单价和数量，然后计算出总金额。
如果所购商品的数量大于10，程序会给予10%的折扣优惠；
如果所购商品的数量不大于10，则没有折扣优惠。
要求程序分别输出顾客所购商品的总金额和折后金额"""
unit_price=float(input("输入顾客所购商品的单价:"))
number=int(input("输入顾客所购商品的数量:"))
cost=unit_price*number
if number>10:
    new_cost=cost*0.9
    print(f"顾客所购商品的总金额为{cost},折后金额为{new_cost}")
else:
    print(f"顾客所购商品的总金额为{cost},折后金额为{cost}")










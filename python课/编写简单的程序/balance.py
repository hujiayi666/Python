"""通过下面的步骤可以计算出储蓄账户中以100元人民币为本金，每年5%为复利，三年后的本息总和。
请把下面的文字描述转变为Python代码，然后调试并运行。"""
#创建变量balance，并赋值为100
balance=100
#balance增长5%，并赋值给balance
balance=balance*(1+0.05)**1
#balance增长5%，并赋值给balance
balance=balance*(1+0.05)**1
#balance增长5%，并赋值给balance
balance=balance*(1+0.05)**1
#输出balance的值
print(balance)
#简化代码如下
balance1=100
balance1=balance1*(1+0.05)**3
print(balance1)











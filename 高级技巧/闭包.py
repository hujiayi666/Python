def outer(num1):
    def inner(num2):
        nonlocal num1
        num1+=num2
        print(num1)

    return inner

fn=outer(10)
fn(20)
fn(10)


def account_creat(inital_account):

    def atm(num,deposit=True):
        nonlocal inital_account
        if deposit:
            inital_account+=num
            print(f"存款+{num},账号余额：{inital_account}")
        else:
            inital_account-=num
            print(f"取款-{num},账号余额：{inital_account}")

    return atm

fn1=account_creat(1000)
fn1(100)
fn1(200)
fn1(100,deposit=False)































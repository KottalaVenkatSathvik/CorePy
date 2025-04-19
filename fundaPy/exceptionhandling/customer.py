class CustomerNotFoundError(Exception):
    def __init__(self,arg):
        self.msg=arg

try:
    customerid:int=int(input("enter customer id"))
    if customerid!=456:
        raise CustomerNotFoundError("Customer is not available in the system.")
    else:
        print("Welcome ",customerid)
except CustomerNotFoundError as ex:
    print(ex)

def payment(status_page):
    def check(status):
        if (status=="completed"):
            print("payment is completed successfully")
        elif(status=="pending"):
            print("payment is pendung")
        elif(status=="failed"):
            print("payment is failed")
        else:
            print("invalid detailes")
    return check
@payment
def success():
    print("payment is completed successfully")
success("completed")

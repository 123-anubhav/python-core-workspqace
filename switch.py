a=15
#a=5
match(a):
    case 1: print("this is case 1-block")
    case 5: print("this is case 5-block")
    case 10: print("this is case 10-block")
    case _:print("this is default block")
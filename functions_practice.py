def hello():
    print('Hello friends')

def pack(ryan, kaori, cesar):
    return[ryan, kaori, cesar]

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I eat {my_list[0]}")
            else:
                print(f"Next I eat {my_list[i]}")

hello()
print(pack("ryan","kaori","cesar"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])
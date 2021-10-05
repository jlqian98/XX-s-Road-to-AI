###
# def
###

def kokole():
    print("kokole chi p") 
    print("yyddog")

kokole()



###
# def 参数
###

def kokole(last_name,first_name):
    print(f"hi {last_name} {first_name}") 
    print("yyddog")

kokole("Q","jl")


def increment (number1,number2):
    return number1*number2
print(increment(1,2))


def save_user(**user):
    print(user["id"])

save_user(id=1,name="li",age=2)

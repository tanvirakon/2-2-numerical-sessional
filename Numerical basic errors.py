import math

exact_value=math.pi

appox=3.1416

round_of_error=abs(exact_value-appox)
# print(f"Round of error : {round_off_error}")
print(f"round of error : {round_of_error}")


true_val=10.5
appox_val=10.2
absolute_error=abs(true_val-appox_val)
print(f"absolute error: {absolute_error}")


true_val=10.5
appox_val=10.2
absolute_error=abs(true_val-appox_val)
print(f"relative error: {round((absolute_error*100),10)}%")

true =15.0
appx=14.8

round_off_error=.05


general_error=abs(true-appx)+round_off_error

print(f"general error : {general_error}")
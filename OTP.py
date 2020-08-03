import string
import math as m
import random as r
#Otp function
def one_time_pass():
    
    alphabet= '0123456789'+string.ascii_lowercase+string.ascii_uppercase
    otp=""
    var=len(alphabet)
    for i in range(6):
        otp=otp+alphabet[m.floor(r.random()*var)]
    return (otp)
if __name__== "__main__":
    
    print("The OTP is",one_time_pass())

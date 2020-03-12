
# prog to print simple intrest

# SI = (P*R*T)/100
#Simple interest formula is given by:
#Simple Interest = (P x T x R)/100
#Where,
#P is the principle amount
#T is the time and
#R is the rate

def simple_intrest_cal():
   prrincipalamt = int (input('Enter principal amount'))
   time = int(input('Input Time period in months'))
   Rate = int(input('Enter Rate of intrest '))

   SI = (prrincipalamt * time * Rate)/100
   print('Simple intrest for given value is', SI)



if __name__ == '__main__':
    while True:
        inp = simple_intrest_cal()
        if input('Do you want to continue'):
            if ch.lower()!=['y','yes'] :
               continue
            else:
                break




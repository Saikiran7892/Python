
 
# Words for basic numbers
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty","seventy", "eighty", "ninety"]

num = int(input("Enter a number (0-999): "))

words=''

divisors=[100,10,1]

if num==0:
    print('Zero')
else:
    for d in divisors:
       
       q=num//d

       if num>=100 and q>0:     
           words += ones[q] +' ' + 'hundred'  
           num%=d
           if num>0:
               words+= ' '+ 'and'
       elif num>=20 and q>0:
            words += ' ' + tens[q]
            num%=d
            if num>0:
                words+= ' '
       elif num>=10 and q>0:
            words +=teens[num-10]
            num=0
       elif q>0:
            words +=  ones[q]
            num=0

    print(words)
        
        


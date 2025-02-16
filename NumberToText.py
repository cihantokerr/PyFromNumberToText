
Digits = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0":"Zero"
}

SecondDigits = {
    "2": "Twenty",
    "3": "Thirty",
    "4": "Fourty",
    "5": "Fifty",
    "6": "Sixty",
    "7": "Seventy",
    "8": "Eighty",
    "9": "Ninety",
}

NumbersThatBeginsWith1 = {
    "2": "Twelve",
    "3": "Thirteen",
    "4": "Fourteen",
    "5": "Fifteen",
    "6": "Sixteen",
    "7": "Seventeen",
    "8": "Eighteen",
    "9": "Nineteen",
}



while True:

    NumberText="" #Clearing text for the next input

    #Getting the number input
    NumberInput=input("Please enter a number:")
    
    #For 3 characters length numbers
    if len(NumberInput)==3:

        for i in range(len(NumberInput)):
            
            #Defining the first digit
            if i==0:
                NumberText+=Digits[NumberInput[0]]+" Hundred"

            #Defining the second digit
            elif i==1:
                
                #If the second digit is 0;don't add anything
                if NumberInput[1]=="0":
                    NumberText+=""

                #If the second digit is 1; Add from the numbers that begins with 1;
                elif NumberInput[1]=="1":

                    NumberText=NumberText+" "+NumbersThatBeginsWith1[NumberInput[1]]


                else:
                    NumberText=NumberText+" "+SecondDigits[NumberInput[1]]

            #Defining the 3rd digit
            elif i==2:
                
                #If the 3rd digit is 0;Don't add anything
                if NumberInput[2]=="0":
                    NumberText=NumberText+" "
                
                else:
                    NumberText=NumberText+" "+Digits[NumberInput[2]]


    print(NumberText)



        



            



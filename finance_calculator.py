import math
#Program By: Keamogetswe Mashao
#This program will allow the user to access to different financal calculators
#It wil calculate the investment and bond rates 
#A is the amount of money accumulated after n years, including interest.
#P is the principal amount
#R is the rate and
#T is the time span

#User will select which calculation they would like to perform
menu = """
Pick a calculation (1-2):
   1) Investment
   2) Bond
"""
#condition if the user want to calculate investment
calculation = int(input(menu))
if calculation == 1:
#user will select whether they want simple or compund interest
   menu = """
   Pick an option:
   3) Compound 
   4) Simple
   """

   #condition if user selects compound interest
   option = int(input(menu))
   if option == 3:
   #compund
      def compound_interest(principle, rate, time):
      
      #Calculation/formula for compound interest
         result = principle * (pow((1 + rate / 100), time))
         return result

      #user will input the different amounts required for the calculation
      p = float(input("Enter the principal amount: "))
      r = float(input("Enter the interest rate: "))
      t = float(input("Enter the time in years: "))

      #program will print the amount and interest for the compound formula
      amount = compound_interest(p, r, t)
      interest = amount - p
      print("Compound amount is %.2f" % amount)
      print("Compound interest is %.2f" % interest)

   if option == 4:
   #simple

      def simple_interest(deposit, interest, duration):
      

         result = a*(1+b*c)
         return result

      #user will input the different amounts required for the calculation
      a = float(input("Enter the principal amount: "))
      b = float(input("Enter the interest rate: "))
      c = float(input("Enter the time in years: "))

      #program will print the amount and interest for the simple formula
      final_amount = simple_interest(a, b, c)
      interest = final_amount - a
      print("Simple amount is %.2f" % final_amount)
      print("Simple interest is %.2f" % interest)

      calculation = int(input(menu))

#condition if the user want to calculate bond repayment
if calculation == 2:

   def bond_repayment(rate, time):
    
    #formula for bond repayment
      result = (i*(1 + i)**n) / ((1+i)**n -1)
      return result

   #user will input the different amounts required for the calculation
   i = float(input("Enter the interest rate per month: "))
   n = float(input("Enter the time in years: "))

   bond_final = bond_repayment(i,n)
   #program will print the total bond repayment
   print("bond repayment monthly is " + str(bond_final))


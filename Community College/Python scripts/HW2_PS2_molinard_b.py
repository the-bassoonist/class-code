income = int(input("Enter income as an integer with no commas: "))
#starting the script
while income > 0 :
  income18 = income

  income18_og = income

  income17 = income

  income17_og = income
  
    #tax totals for year 2017
  taxtot1_17= ((9325 * .1))
    
  taxtot2_17 = ((37950-9326) * .15) + taxtot1_17
    
  taxtot3_17 = ((91900-37951) * .25) + taxtot2_17
    
  taxtot4_17 = ((191650-91901) * .28) + taxtot3_17
    
  taxtot5_17 = ((416700-191651) * .33)+ taxtot4_17
    
  taxtot6_17 = ((418400-416701) * .35)+ taxtot5_17
    
    #totals for year 2018

  taxtot1_18 = (9525*.1)
    
  taxtot2_18 = ((38700-9526) * .12) + taxtot1_18
    
  taxtot3_18 = ((82500-38701) * .22) +taxtot2_18
    
  taxtot4_18 = ((157500-82501) * .24) + taxtot3_18
    
  taxtot5_18 = ((200000-157591) * .32) +taxtot4_18
    
  taxtot6_18 = ((500000-200001) * .35)+ taxtot5_18
    
  if income <0  :
    print("")

  if income18 >0 and income18 <= 9525 :
            taxed18 = income18 * .1

  elif income18 >= 9526 and income18 <= 38700 :
            taxed18 = ((income - 9525) * .12) + taxtot1_18

  elif income18 >= 38701 and income18 <= 82500 :
            taxed18 = ((income - 38700) * .22) + taxtot2_18

  elif income >= 82501 and income18 <= 157500 :
            taxed18 = ((income - 82500) * .24) + taxtot2_18

  elif income18 >= 157501 and income18 <=200000 :
            taxed18 = ((income - 157500) * .32) + taxtot4_18

  elif income18 >= 200001 and income18 <= 500000 :
            taxed18 = ((income - 200000) * .35) + taxtot5_18

  elif income >= 500001 :
            taxed18 = ((income-500000)*.37) + taxtot6_18

  else:
      print("")
            
  if income17 >0 and income17 <= 9325 :
            taxed17 = income17*.1

  elif income17 >= 9326 and income17 <= 37950 :
            taxed17 = (income17 - 9325)*.15 + taxtot1_17

  elif income17 >= 37951 and income17 <= 91900 :
          taxed17 = (income17 - 37950) *.25 + taxtot2_17

  elif income17 >= 91901 and income17 <= 191650 :
            taxed17 = (income17-91901) * .28+taxtot3_17

  elif income17 >= 191651 and income17 <= 416700 :
            taxed17 = (income17 - 191650)*.33 + taxtot4_17

  elif income17 >= 416701 and income17 <= 418400 :
            taxed17 = (income17 - 416700)*.35 + taxtot5_17

  elif income17 >= 418401 :
            taxed17 = ((income17 - 418400)*.369) + taxtot6_17

  else:
      print("")

  #other calculations
        
  diff = taxed18 - taxed17

  diffinperc = (((diff) / taxed17) * 100)

  true_perc = abs(diffinperc)

  print("Income: $", \
    format(income17_og, ',.2f'), sep =' ')
  
  print("2017 tax: $", \
    format(taxed17, ',.2f'), sep =' ')

  print("2018 tax: $", \
  format(taxed18, ',.2f'), sep =' ')

  print("Difference: $", \
  format(diff, ',.2f'), sep =' ')

  print("Difference (percent): ", \
  format(true_perc, ',.2f'), sep =' ')
  
#herein lies the loop back to the beginning so long as -1 is not entered. or any negative value for that matter
  
  income = float(input("\nEnter income as an integer with no commas: "))

#Test Runs 
 
#Sample Test Run 1 
#_____________________________________________________________ 
 
#Enter income as an integer with no commas: 8000 
#Income: 8000 
#2017 tax: 800.00 
#2018 tax: 800.00 
#Difference: 0.00 
#Difference (percent): 0.00 
 
#Enter income as an integer with no commas: 15000 
#Income: 15000 
#2017 tax: 1783.75 
#2018 tax: 1609.50 
#Difference: -174.25 
#Difference (percent): 9.77 
 
#Enter income as an integer with no commas: 40000 
#Income: 40000 
#2017 tax: 5738.75 
#2018 tax: 4739.50 
#Difference: -999.25 
#Difference (percent): 17.41 
 
#Enter income as an integer with no commas: 100000 
#Income: 100000 
#2017 tax: 20981.75 
#2018 tax: 18289.50 
#Difference: -2692.25 
#Difference (percent): 12.83 
 
#Enter income as an integer with no commas: 200000 
#Income: 200000 
#2017 tax: 49399.25 
#2018 tax: 45689.50 
#Difference: -3709.75 
#Difference (percent): 7.51 
 
#Enter income as an integer with no commas: 500000 
#Income: 500000 
#2017 tax: 153818.85 
#2018 tax: 150689.50 
#Difference: -3129.35 
#Difference (percent): 2.03 
 
#Enter income as an integer with no commas: 1000000 
#Income: 1000000 
#2017 tax: 351818.85 
#2018 tax: 335689.50 
#Difference: -16129.35 
#Difference (percent): 4.58 
 
#Enter income as an integer with no commas: 10000000 
#Income: 10000000 
#2017 tax: 3915818.85 
#2018 tax: 3665689.50 
#Difference: -250129.35 
#Difference (percent): 6.39 
 
#Enter income as an integer with no commas: -1

#test run2
#Enter income as an integer with no commas: -1

#test run 3\

#Enter income as an integer with no commas: 135798
#Income: $ 135,798.00
#2017 tax: $ 31,004.51
#2018 tax: $ 17,244.90
#Difference: $ -13,759.61
#Difference (percent):  44.38

#Enter income as an integer with no commas: 84201
#Income: $ 84,201.00
#2017 tax: $ 16,788.85
#2018 tax: $ 4,861.62
#Difference: $ -11,927.23
#Difference (percent):  71.04

#Enter income as an integer with no commas: 2304
#Income: $ 2,304.00
#2017 tax: $ 230.40
#2018 tax: $ 230.40
#Difference: $ 0.00
#Difference (percent):  0.00

#Enter income as an integer with no commas: -1

#test run 4
#Enter income as an integer with no commas: 12
#Income: $ 12.00
#2017 tax: $ 1.20
#2018 tax: $ 1.20
#Difference: $ 0.00
#Difference (percent):  0.00

#Enter income as an integer with no commas: 43529871
#Income: $ 43,529,871.00
#2017 tax: $ 16,029,636.69
#2018 tax: $ 16,071,711.72
#Difference: $ 42,075.03
#Difference (percent):  0.26

#Enter income as an integer with no commas: 42318
#Income: $ 42,318.00
#2017 tax: $ 6,318.10
#2018 tax: $ 5,249.34
#Difference: $ -1,068.76
#Difference (percent):  16.92

#Enter income as an integer with no commas: -1

#test run5

#Enter income as an integer with no commas: 69420
#Income: $ 69,420.00
#2017 tax: $ 13,093.60
#2018 tax: $ 11,211.78
#Difference: $ -1,881.82
#Difference (percent):  14.37

#Enter income as an integer with no commas: 813011
#Income: $ 813,011.00
#2017 tax: $ 267,115.35
#2018 tax: $ 266,473.52
#Difference: $ -641.83
#Difference (percent):  0.24

#Enter income as an integer with no commas: 13841
#Income: $ 13,841.00
#2017 tax: $ 1,609.90
#2018 tax: $ 1,470.42
#Difference: $ -139.48
#Difference (percent):  8.66

#Enter income as an integer with no commas: -1



#Berkiel Molinard
#1095255
#Homework 1 Problem set 2
#This program computes data about a given stock
#for simplicity's sake the actual terms will be commented on

#stk_nm <- STocK NaMe
stk_nm = input("Enter the name of the stock:")

#no_shrs <-  Number of SHaReS
no_shrs = float(input("Enter the number of shares bought:"))

#stk_pp <- STocK PurchacePrice
stk_pp = float(input("Enter the price of the stock when first bought:"))

#stk_sp <- STock SalePrice
stk_sp = float(input("Enter the price of the stock at the time of sale:"))

#brk_comm <- BRoKer COMMission
brk_comm = float(input("Enter the brokerage commision:"))

tot_pay = no_shrs * stk_pp
by_tot_comm = no_shrs * stk_pp
tot_sale = no_shrs * stk_sp
sl_tot_comm = tot_sale * brk_comm
nt_gnln = (tot_sale-sl_tot_comm)-(tot_pay + by_tot_comm)

print(

import pandas as pd 
import numpy as np 
import time 
import sys 

csv=(pd.read_csv('/storage/emulated/0/fifa 23/Car_sales.csv'))
df=pd.DataFrame(csv)

while True :
	print('\nWELCOME TO THE MAIN MENU')
	print('\n 1) SHOW COLUMNS')
	print('\n 2) SHOW TOP ROWS')
	print('\n 3) SHOW BOTTOM ROWS')
	print('\n 4) SHOW SPECIFIC COLUMN')
	print('\n 5) ADD A NEW RECORD')
	print('\n 6) DELETE A RECORD')
	print('\n 7) COMPLETE DATASET')
	print('\n 8) CREDITS AND ABOUT THE PROJECT')

	a=int(input('\n Enter Your Choice>>> '))

	if a==1:
		print('Manufacturer, Model, Sales_in_thousands, Price_in_thousands, Horsepower, Fuel_capacity')
		print('\n \nEnter 1 to return back to the Main Menu.')
		print('Enter 2 to exit the code.')
		b=int(input('>>>'))
		if b==1:
			def delay_print(s):
				for c in s:
					sys.stdout.write(c)
					sys.stdout.flush()
					time.sleep(0.2)
			delay_print("Loading...")
		elif b==2: 
			print('Thank You for using.\n Made By : Meghansh Sharma | Class 12 Alpha')
			break 
			
	elif a==2:
		n=int(input("\n Enter Total number of rows you want to see:"))
		print(df.head(n))
		print('\n \nEnter 1 to return back to the Main Menu.')
		print('Enter 2 to exit the code.')
		b=int(input('>>>'))
		if b==1:
			def delay_print(s):
				for c in s:
					sys.stdout.write(c)
					sys.stdout.flush()
					time.sleep(0.2)
			delay_print("Loading...")
		elif b==2: 
			print('Thank You for using.\n Made By : Meghansh Sharma | Class 12 Alpha')
			break 
	
	elif a==3:
		n=int(input('\n Enter Total number of rows you want to see:'))
		print(df.tail(n))
		print('\n \nEnter 1 to return back to the Main Menu.')
		print('Enter 2 to exit the code.')
		b=int(input('>>>'))
		if b==1:
			def delay_print(s):
				for c in s:
					sys.stdout.write(c)
					sys.stdout.flush()
					time.sleep(0.2)
			delay_print("Loading...")
		elif b==2: 
			print('Thank You for using.\n Made By : Meghansh Sharma | Class 12 Alpha')
			break 
	
	elif a==4:
		print('Manufacturer, Model, Sales_in_thousands, Price_in_thousands, Horsepower, Fuel_capacity')
		col=input('\n Enter Column name that you want to see: ')
		print(df[col])
		print('\n \nEnter 1 to return back to the Main Menu.')
		print('Enter 2 to exit the code.')
		b=int(input('>>>'))
		if b==1:
			def delay_print(s):
				for c in s:
					sys.stdout.write(c)
					sys.stdout.flush()
					time.sleep(0.2)
			delay_print("Loading...")
		elif b==2: 
			print('Thank You for using.\n Made By : Meghansh Sharma | Class 12 Alpha')
			break 
			
	elif a==5:
		z=input('\n Enter Manufacturer Name >>>')
		y=input('\n Enter Model Name >>>')
		x=input('\n Enter Sales_In_Thousands >>>')
		w=input('\n Enter Price_In_Thousands >>>')
		v=input('\n Enter Horsepower >>>')
		u=input('\n Enter Fuel_Capacity >>>')
		new={'Manufacturer' : [z], 'Model' : [y], 'Sales_in_thousands' : [x], 'Price_in_thousands' : [w], 'Horsepower' : [v], 'Fuel_capacity' : [u]}
		i=pd.DataFrame(new)
		p=[df,i]
		result=pd.concat(p)
		print(result.loc[:,['Manufacturer', 'Model', 'Sales_in_thousands', 'Price_in_thousands', 'Horsepower', 'Fuel_capacity']])
		print('Thank You for using.\n Made By : Meghansh Sharma | Class 12 Alpha')
		result.to_csv('/storage/emulated/0/fifa 23/Car_sales.csv')
		break 
			
	elif a==6: 
		print(df.loc[:,['Manufacturer', 'Model', 'Sales_in_thousands', 'Price_in_thousands', 'Horsepower', 'Fuel_capacity']])
		csv1=(pd.read_csv('/storage/emulated/0/fifa 23/Car_sales.csv'))
		df1=pd.DataFrame(csv1)
		d=int(input("\nEnter Row Number to Delete >>>"))
		o=df1.drop(d,axis=0)
		def delay_print(s):
				for c in s:
					sys.stdout.write(c)
					sys.stdout.flush()
					time.sleep(0.2)
		delay_print("Deleting...")
		print("\n")
		print(o.loc[:,['Manufacturer', 'Model', 'Sales_in_thousands', 'Price_in_thousands', 'Horsepower', 'Fuel_capacity']])
		o.to_csv('/storage/emulated/0/fifa 23/Car_sales.csv')
		print('Thank You for using.\n Made By : Meghansh Sharma | Class 12 Alpha')
		break 
			
	elif a==7:
		print('\n')
		print(df.loc[:,['Manufacturer', 'Model', 'Sales_in_thousands', 'Price_in_thousands', 'Horsepower', 'Fuel_capacity']])
		print('\n \nEnter 1 to return back to the Main Menu.')
		print('Enter 2 to exit the code.')
		b=int(input('>>>'))
		if b==1:
			def delay_print(s):
				for c in s:
					sys.stdout.write(c)
					sys.stdout.flush()
					time.sleep(0.2)
			delay_print("Loading...")
		elif b==2: 
			print('Thank You for using.\n Made By : Meghansh Sharma | Class 12 Alpha')
			break 
			
	elif a==8:
		print('Made By Meghansh Sharma | Class 12 Alpha \nSession : 2023-24 \nThe Project helps us to manage a complete database of a car dealership. It allows you to create new records and also delete records. It automatically saves all the changes to the Csv file. Thank You for Using and I hope the project left a positive impression on you.')
		print('\n \nEnter 1 to return back to the Main Menu.')
		print('Enter 2 to exit the code.')
		b=int(input('>>>'))
		if b==1:
			def delay_print(s):
				for c in s:
					sys.stdout.write(c)
					sys.stdout.flush()
					time.sleep(0.2)
			delay_print("Loading...")
		elif b==2: 
			print('Thank You for using.\n Made By : Meghansh Sharma | Class 12 Alpha')
			break 
		
	elif a==9:
		print('Thank You for using.\n Made By : Meghansh Sharma | Class 12 Alpha')
		break
		
	else:
		print('\n')
		def delay_print(s):
				for c in s:
					sys.stdout.write(c)
					sys.stdout.flush()
					time.sleep(0.2)
		delay_print("Please Choose a Valid Option. Redirecting to the Main Menu...")	
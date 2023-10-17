import pandas as pd 
import numpy as np 
import time 
import sys 
import matplotlib.pyplot as plt

csv=(pd.read_csv('/storage/emulated/0/fifa 23/Car_sales.csv'))
df=pd.DataFrame(csv)

while True :
	print('\n \n WELCOME TO THE MAIN MENU')
	print('\n 1) SHOW COLUMNS')
	print('\n 2) SHOW TOP ROWS')
	print('\n 3) SHOW BOTTOM ROWS')
	print('\n 4) SHOW SPECIFIC COLUMN')
	print('\n 5) ADD A NEW RECORD')
	print('\n 6) DELETE A RECORD')
	print('\n 7) COMPLETE DATASET')
	print('\n 8) CREDITS AND ABOUT THE PROJECT')
	print('\n 9) TO ENTER THE DATA VISUALIZATION MENU')
	print('\n 10) TO EXIT THE CODE')

	a=(input('\n Enter Your Choice>>> '))

	if a=='1':
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
			
	elif a=='2':
		n=int(input("\n Enter Total number of rows you want to see:"))
		print(df[['Manufacturer', 'Model', 'Sales_in_thousands', 'Price_in_thousands', 'Horsepower', 'Fuel_capacity']].head(n))
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
	
	elif a=='3':
		n=int(input('\n Enter Total number of rows you want to see:'))
		print(df[['Manufacturer', 'Model', 'Sales_in_thousands', 'Price_in_thousands', 'Horsepower', 'Fuel_capacity']].tail(n))
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
	
	elif a=='4':
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
			
	elif a=='5':
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
			
	elif a=='6': 
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
			
	elif a=='7':
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
			
	elif a=='8':
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
		
	elif a=='10':
		print('Thank You for using.\n Made By : Meghansh Sharma | Class 12 Alpha')
		break
		
	elif a=='9':
		while True:
			print('WELCOME TO THE DATA VISUALIZATION MENU. YOU CAN VIEW THE SALES OF THE FOLLOWING MANUFACTURERS IN A BAR GRAPH FORMAT.')
			print('\n 1) ACURA')
			print('\n 2) AUDI')
			print('\n 3) BMW')
			print('\n 4) BUICK')
			print('\n 5) CADILLAC')
			print('\n 6) CHEVROLET')
			print('\n 7) CHRYSLER')
			print('\n 8) DODGE')
			print('\n 9) FORD')
			print('\n 10) HONDA')
			print('\n 11) HYUNDAI')
			print('\n 12) INFINITI')
			print('\n 13) JAGUAR')
			print('\n 14) JEEP')
			print('\n 15) LEXUS')
			print('\n 16) LINCOLN')
			print('\n 17) MITSUBISHI')
			print('\n 18) MERCURY')
			print('\n 19) MERCEDES BENZ')
			print('\n 20) NISSAN')
			print('\n 21) OLDSMOBILE')
			print('\n 22) PLAYMOUTH')
			print('\n 23) PONTIAC')
			print('\n 24) SAAB')
			print('\n 25) SATURN')
			print('\n 26) SUBARU')
			print('\n 27) TOYOTA')
			print('\n 28) VOLKSWAGEN')
			print('\n 29) VOLVO')
			k=input('\n Enter Manufacturer of your choice>>>')
			
			if k=='1':
				sale=[16.919, 39.384, 14.114, 8.588]
				model=['Integra', 'TL', 'CL', 'RL']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')
			
			elif k=='2':
				sale=[20.397,18.78,1.38]
				model=['A4','A6','A8']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')
				
			elif k=='3':
				sale=[19.747,9.231,17.527]
				model=['323i','330i','528i']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')
				
			elif k=='4':
				sale=[91.561,39.35,27.851,83.257]
				model=['Century','Regal','Park Avenue','LeSabre']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')
			
			elif k=='5':
				sale=[63.729,15.943,6.536,11.185,14.785]
				model=['Deville','Seville','Elorado','Catera','Escalade']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')
				
			elif k=='6':
				sale=[145.519,135.126,24.629,42.593,26.402,17.947,32.299,21.855,107.995]
				model=['Cavalier','Malibu','Lumina','Monte Carlo','Camaro','Corvette','Prizm','Metro','Impala']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')
				
			elif k=='7':
				sale=[7.854,32.775,31.148,32.306,13.462,53.48,30.696]
				model=['Coupe','Conv','Concorde','Cirrus','LHS','TOWN','300M']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')
				
			elif k=='8':
				sale=[76.034,4.734,71.186,88.028,0.916,227.061,16.767,31.038,111.313,101.323,181.749]
				model=['Neon','Avenger','Stratus','Intrepid','Viper','Ram Pickup','Ram Wagon','Ram Van','Dakota','Durango','Caravan']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')					
				
			elif k=='9':
				sale=[70.227,113.369,35.068,245.815,175.67,63.403,276.747,155.787,125.338,220.65,540.561]
				model=['Escort','Mustang','Contour','Taurus','Focus','Crown','Explorer','Windstar','Expedition','Ranger','F-Series']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')				
				
			elif k=='10':
				sale=[199.685,230.902,73.203,12.855,76.029]
				model=['Civic','Accord','CR-V','Passport','Odysee']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')					
				
			elif k=='11':
				sale=[41.184,66.692,29.45]
				model=['Accent','Elantra','Sonata']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')
									
			elif k=='12':
				sale=[23.713]
				model=['I30']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')
									
			elif k=='13':
				sale=[15.467]
				model=['S-type']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')
									
			elif k=='14':
				sale=[55.55,80.556,157.04]
				model=['Wrangler','Cherokee','Grand Chero']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')					
				
			elif k=='15':
				sale=[24.07,12.69,3.34,6.375,9.126,51.238]
				model=['ES300','GS300','LS400','LX470','RX300']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')					
				
			elif k=='16':
				sale=[13.79,48.91,22.95]
				model=['Continental','Town Car','Navigator']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')				
				
			elif k=='17':
				sale=[26.23,42.54,55.6,5.7,0.11,11.3,39.348]
				model=['Mirage','Eclipse','Galant','Diamante','3000GT','Montero','Montero Spo.']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')
										
			elif k=='18':
				sale=[14.35,26.5,67.9,81.17,27.6,20.3]
				model=['Mystique','Cougar','Sable','Grand Marq','Mountanier','Villager']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')
								
			elif k=='19':
				sale=[18.39,27.6,16.7,3.31,7.998,1.526,11.592,0.954,28.96]
				model=['C-Class','E-Class','S-Class','SLK','SLK230','CLK Coupe','CL500','M-Class']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')
									
			elif k=='20':
				sale=[42.6,88.09,79.85,27.308,42.57,54.15,65.005]
				model=['Sentra','Altima','Maxima','Quest','Pathfinder','Xterra','Frontier']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')
										
			elif k=='21':
				sale=[1.112,38.554,80.255,14.69,20.017,24.361]
				model=['Cutlass','Intrigue','Alero','Aurora','Bravada','Silhoulette']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')				
				
			elif k=='22':
				sale=[32.734,5.24,24.15,1.87]
				model=['Neon','Breeze','Voyager','Prowler']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')					
					
			elif k=='23':
				sale=[51.645,131.09,19.911,92.364,35.945,35.972,39.572]
				model=['Sunfire','Grand Am','Firebird','Grand Prix','Bonneville','Montana']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')						
					
			elif k=='24':
				sale=[9.191,12.115]
				model=['5-Sep','3-Sep']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')
										
			elif k=='25':
				sale=[80.62,24.5,5.223,8.472,49.9]
				model=['SL','SC','SW','LW','LS']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')					
					
			elif k=='26':
				sale=[47.107,33.028]
				model=['Outback','Forester']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')
										
			elif k=='27':
				sale=[142.53,247.99,63.849,33.269,84.087,65.119,25.106,68.411,9.835]
				model=['Corolia','Camry','Avalon','Celica','Tacoma','Sienna','RAV 4','Runner','Land Cruiser']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')					
					
			elif k=='28':
				sale=[9.76,83.7,51.102,9.569,5.596,49.464]
				model=['Golf','Jetta','Passat','Cabrio','GTI','Beetle']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')
			
			elif k=='29':
				sale=[16.95,3.54,15.24,17.5]
				model=['S40','V40','S70','V70']
				plt.bar(model,sale)
				plt.show()
				
				r=int(input('Enter 1 to return back to the main or Enter 2 to return back to the Visualization Menu.'))
				if r==1:
					break
				else:
					print('\n')
							
	 
					
		else:
		 	 print('\n Please Choose A Valid Option...')
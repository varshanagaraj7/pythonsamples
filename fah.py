def fah_to_cel():
 print("Fahrenheit to Celsius")
 fahrenheit=float(input("enter the value:"))
 celsius=(fahrenheit-32*5/9)
 print(f"celsius value:{fahrenheit:.2f}")

def cel_to_fah():
 print("Celsius to fahrenheit")
 celsius=float(input("enter the value:"))
 fahrenheit=celsius*9/5+32
 print(f"fahrenheit value:{celsius:.2f}")

print("1.conversion of fahrenheit to Celsius:")
print("2.conversion of Celsius to fahrenheit:")

ch=int(input("enter the choice:"))
if (ch==1):
 fah_to_cel()
elif (ch==2):
 cel_to_fah()
else:
 print("enter a valid number")
 

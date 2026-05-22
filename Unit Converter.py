#Unit Converter
print('1.Celsius to Fahrenheit')
print('2.Kilometers to Miles')
print('3.Kilograms to Pounds')
choice = int(input('Enter your choice (1-3): '))
if choice == 1:
    celsius = float(input('Enter temperature in Celsius: '))
    fahrenheit = (celsius * 9/5) + 32
    print(f'{celsius}°C is equal to {fahrenheit}°F')
elif choice == 2:
    kilometers = float(input('Enter distance in Kilometers: '))
    miles = kilometers * 0.621371
    print(f'{kilometers} km is equal to {miles} miles')
elif choice == 3:
    kilograms = float(input('Enter weight in Kilograms: '))
    pounds = kilograms * 2.20462
    print(f'{kilograms} kg is equal to {pounds} pounds')
else:
    print('Invalid choice. Please select a number between 1 and 3.')

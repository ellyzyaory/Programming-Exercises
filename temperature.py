def convert_temp():
    farenheit = int(input("Enter a temperature in Fahrenheit: "))
    print("The temperature in Fahrenheit is: ", farenheit)

    def convert_to_celsius():
        celsius = 5 / 9 * (farenheit - 32)
        print("The temperature in Celsius is: ", celsius)
        return celsius

    def convert_to_kelvin():
        kelvin = convert_to_celsius() + 273.15
        return kelvin
    print("The temperature in Kelvin is: ", convert_to_kelvin())

convert_temp()


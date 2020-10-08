def convert_to_days():
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))
    seconds = int(input("Enter number of seconds: "))

    def get_days():
        return hours/24 + minutes/(24*60) + seconds/(24*3600)

    print("The number of days is: ", round(get_days(),4))

convert_to_days()

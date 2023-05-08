
fields = ('origin', 'destination', 'price', 'date', 'time')
flights = []
while True:
    flight = {}
    for field in fields:
        f = input(f"Insert {field}: ")
        if f == '$':
            print(flights)
            exit(0)
        flight[field] = f
    flights.append(flight)
    print(f"The new flight is: {flight}")



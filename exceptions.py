try:
    age = int(input('Age: '))
    income = 50000
    risk = income / age
    print(risk)
except ZeroDivisionError:
    print("Age can't be zero")
except ValueError:
    print('Invalid value')

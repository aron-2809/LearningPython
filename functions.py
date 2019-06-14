def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print("Welcome aboard")

print("Start")
greet_user("John", last_name="Smith") # Keyword argument should be after positional argument
print("Finish")

def square(number):
    return number * number

print(square(400))
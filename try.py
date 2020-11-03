while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0:
            break
        print("Invalid age entered")
    except Exception as e:
        print(e)

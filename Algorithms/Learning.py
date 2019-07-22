while True:
    try:
        num = float(input("Enter your favourite number: \n"))
        print(20/num)
        break

    except ValueError:
        print("Its a String, enter a number \n")
    except ZeroDivisionError:
        print("Number cannot be divided by 0 \n")
    except:
        break




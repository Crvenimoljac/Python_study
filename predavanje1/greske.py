#try, exception, finally

try: #ako se u bloku try javi greska onda se izvrsava exception
    num=int(input("unesi broj: "))
    r=10/num
    print(r)
except ValueError:
    print("niste uneli int tip.")
except ZeroDivisionError:
    print("nije moguce deliti sa 0")
finally: # uvek se izvrsava i finally je opcionalan
    print("ovaj deo koda se izvrsava bez obzira na gresku da li posotji")
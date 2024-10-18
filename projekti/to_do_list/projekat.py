
todo={
    "posao":{
        1:{
            "bxbc":1
        }
    }
}
def create_new_list(name_list:str)->bool:
    if name_list in todo:
        return False
    todo[name_list]={}
    return True
    
def print_menu():
    print("1. c\n2.r\n3.u\n4.d")

def add_task(task:str,status:int|str=None):
    if len(todo)==0:
        todo[1]={"task" : task,"status":status}
    else:
        todo[len(todo)+1]={"task" : task,"status":status}
    return True


def read():
    if len(todo)==0:
        return "Nema ni jedan zadatak!"
    return todo


def update():
    False
    

def delete():
    False


#glavni program
def main():
    print_menu()
    
    while True:
        option=int(input("opcija"))
        if option==1:
            task=input("Dodaj novi task: ")
            status=input("Dodaj status: ")
            if add_task(task,status):
                print("Uspesno dodat zadatak.")
        elif option==2:
            print(read())
        elif option==3:
            while True:
                new_list=input("lista: ")
                if not create_new_list(new_list):
                    print(f"lista sa {new_list} vec postoji, ako zelisa da prekines unos KRaJ")
                elif new_list=="kraj":
                    break
                else:
                    print(f"lista {new_list} je kreirana")
                    break


    

if __name__=='__main__':
    main()
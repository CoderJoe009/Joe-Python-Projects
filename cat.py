def main():
    number = get_no()
    meow(no)
    
def get_no():
    while True:
        no = int(input("Number: "))
        if no > 0:
            return no
        
        
def meow(no):
    for _ in range(no):
        print("meow")
        
main()            

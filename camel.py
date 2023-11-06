def under(inp):
    list = []
    for char in inp:
        if char.isupper():
            list.extend(['_' , char.lower()])
        else:
            list.append(char)
            
    formatted = ''.join(list).lstrip("_")
    return formatted

def main():
    inp = input("camelCase: ")
    format = under(inp)
    print("snake_case:" , format)  
    
main()              
frac = input("Fraction: ")
res = eval(frac)
forma = "{:.0%}".format(res)

def main():
    while True:
        try:
            if res  >= 0.99 and res <= 1:
                print("F")
            elif res <= 0.01:
                print("E")
            else:
                print(forma)
        except NameError:
            pass
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
        else:
            break
    
main()


    
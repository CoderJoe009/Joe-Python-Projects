ans = input("Greeting: ").lower().strip()
first = ans.split()[0]

if first.lstrip().startswith("hello"):
        print("$0")
elif first.lstrip().startswith("h"):
        print("$20")
else:
        print("$100")
         
   
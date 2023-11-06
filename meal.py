def main():
    time = input("What's the time? ")
    decimal_time = convert(time)
    if 7.0 <= decimal_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= decimal_time <= 13.0:
        print("lunch time")
    elif 18.0 <= decimal_time <= 19.0:
        print("dinner time")
    
def convert(time):
    hrs, mins = map(int, time.split(":"))
    decimal_time = hrs + mins / 60
    return decimal_time

if __name__ == "__main__":
    main()
           
         
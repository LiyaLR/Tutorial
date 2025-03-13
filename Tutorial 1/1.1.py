def conversion(seconds):
   hours = seconds//3600
   minutes = (seconds % 3600)//60
   seconds = seconds % 60
   return f"{int(hours)}:{int(minutes)}:{int(seconds)}"

def main():
   seconds=int(input("Enter the time in seconds:"))
   print(conversion(seconds))

main()

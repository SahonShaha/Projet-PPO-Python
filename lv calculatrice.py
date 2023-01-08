fr = input("Enter your French result: ")
st = input("Enter your ST result: ")
ste = input("Enter your STE result: ")
eng = input("Enter your English result: ")
hist = input("Enter your History result: ")
math = input("Enter your Math result: ")
art = input("Enter your Art result: ")
gym = input("Enter your Gym result: ")
ecr = input("Enter your ECR result: ")




try:
 print(round(((int(fr) * 8) + (int(st) * 4) + (int(ste) * 4) + (int(eng) * 4) + (int(hist) * 4) + (int(math) * 6) + (int(art) * 2) + (int(gym) * 2) + (int(ecr) * 2))/36))
except:
    print("Invalid Results. Please check if you entered the numbers correctly")

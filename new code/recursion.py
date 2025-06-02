def show_profile(**some):
    for key,value in some.items():
        print(f"{key}:{value}")


x=input("Enter your name:")
y=input("Enter your age.")
z=input("Enter your Roll no:")
show_profile(name=x,age=y,Roll_no=z)

def greet(name: str):
    print(f"Hello, {name} !Welcome")

if __name__ == "__main__":
    user_name = input("Enter your name:")
    greet(user_name)
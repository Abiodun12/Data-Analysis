from geometry import calculate_square_footage, calculate_circumference

def main():
    print("Welcome to the Geometry Calculator!")
    print("1. Calculate Square Footage of a House")
    print("2. Calculate Circumference of a Circle")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        length = float(input("Enter the length of the house (in feet): "))
        width = float(input("Enter the width of the house (in feet): "))
        area = calculate_square_footage(length, width)
        print(f"The square footage of the house is: {area} square feet")
    elif choice == 2:
        radius = float(input("Enter the radius of the circle (in feet): "))
        circumference = calculate_circumference(radius)
        print(f"The circumference of the circle is: {circumference} feet")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

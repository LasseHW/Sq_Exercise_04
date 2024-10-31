from module import calculate_area

def main():
    shape = input("Enter shape (circle, square, rectangle): ").lower()
    dimensions = list(map(float, input("Enter dimensions separated by space: ").split()))
    area = calculate_area(shape, *dimensions)
    print(f"The area of the {shape} is {area}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    print(triangle.area(5,5))
    print(triangle.hypothenuse(5,5))

if __name__ == "__main__":
    main()

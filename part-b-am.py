class Vector:
    def __init__(self, components):
        # Initialize with a tuple of numbers
        self.components = tuple(components)

    def __add__(self, other):
        # vector addition
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension")
        
        new_components = []
        for i in range(len(self.components)):
            new_components.append(self.components[i] + other.components[i])
        return Vector(tuple(new_components))

    def __sub__(self, other):
        # vector subtraction
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension")
        
        new_components = []
        for i in range(len(self.components)):
            new_components.append(self.components[i] - other.components[i])
        return Vector(tuple(new_components))

    def __mul__(self, scalar):
        # scalar multiplication
        new_components = []
        for component in self.components:
            new_components.append(component * scalar)
        return Vector(tuple(new_components))

    def __repr__(self):
        # readable output
        return f"Vector{self.components}"

# Test your class with multiple examples
v1 = Vector((1, 2, 3))
v2 = Vector((4, 5, 6))

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")

# Addition
v_add = v1 + v2
print(f"Addition: {v1} + {v2} = {v_add}")

# Subtraction
v_sub = v2 - v1
print(f"Subtraction: {v2} - {v1} = {v_sub}")

# Scalar Multiplication
v_mul = v1 * 3
print(f"Multiplication: {v1} * 3 = {v_mul}")

# Example 2
v3 = Vector((10, 20))
v4 = Vector((5, 5))
print(f"\nVector 3: {v3}")
print(f"Vector 4: {v4}")
print(f"Addition: {v3 + v4}")
print(f"Subtraction: {v3 - v4}")
print(f"Multiplication: {v3 * 0.5}")

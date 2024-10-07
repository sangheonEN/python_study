try:
    import example
except ImportError:
    print("Could not import the example.")

result = example.add(10, 20)

print(f"result : {result}")
import sys

def consume_memory():
    memory_hog = []
    size = 1024 * 1024  # 1 MB
    total_allocated = 0

    try:
        while True:
            memory_hog.append(' ' * size)
            total_allocated += size
            print(f"Allocated {total_allocated / (1024 * 1024)} MB")
    except MemoryError:
        print(f"Memory allocation failed at {total_allocated / (1024 * 1024)} MB")

if __name__ == "__main__":
    consume_memory()

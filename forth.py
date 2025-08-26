def modify_content(content):
    return content.upper()

def main():
    input_filename = input("Enter the filename to read: ")
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
        return
    except IOError:
        print(f"Error: Could not read file '{input_filename}'.")
        return

    modified_content = modify_content(content)
    output_filename = input("Enter the filename to write the modified content: ")
    try:
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(modified_content)
        print(f"Modified content written to '{output_filename}'.")
    except IOError:
        print(f"Error: Could not write to file '{output_filename}'.")

if __name__ == "__main__":
    main()
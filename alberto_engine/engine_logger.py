def append_to_logs( text):
        file_path = 'logs.txt'
        try:
            # Try to open the file in append mode
            with open(file_path, 'a') as file:
                # Append a new line with the provided text
                file.write(text + '\n')
        except Exception as e:
            print(f"Error: {e}")
    
def empty_logs():
    file_path = 'logs.txt'
    try:
        # Open the file in write mode, which truncates the file
        with open(file_path, 'w'):
            pass  # Using 'with' automatically closes the file
        print(f"The file {file_path} has been emptied.")
    except Exception as e:
        print(f"Error: {e}")
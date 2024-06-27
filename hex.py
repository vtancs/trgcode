import sys

def get_color_code(byte, is_ascii=False):
    # For ASCII view in blue
    if is_ascii:
        return 34  # Blue for ASCII characters
    # Color coding for hex view based on byte value
    if byte < 64:
        return 31  # Red
    elif byte < 128:
        return 32  # Green
    elif byte < 192:
        return 33  # Yellow
    else:
        return 34  # Blue

def print_hex_view(file_path, num_bytes=None, char_view=False):
    try:
        with open(file_path, 'rb') as file:
            offset = 0
            while True:
                bytes_to_read = 16 if num_bytes is None else min(16, num_bytes - offset)
                if bytes_to_read <= 0:
                    break
                
                bytes_read = file.read(bytes_to_read)
                if not bytes_read:
                    break

                hex_view = ''
                ascii_view = ''  # To accumulate ASCII characters for the end of the row
                for byte in bytes_read:
                    color_code = get_color_code(byte)
                    hex_view += f'\x1b[{color_code}m{byte:02X}\x1b[0m '
                    if char_view:
                        ascii_color_code = get_color_code(byte, is_ascii=True)
                        char_representation = chr(byte) if 32 <= byte <= 126 else '.'
                        hex_view += f'\x1b[{ascii_color_code}m{char_representation}\x1b[0m '
                    ascii_view += chr(byte) if 32 <= byte <= 126 else '.'

                print(f"{offset:08X}: {hex_view}| {ascii_view}")
                
                offset += len(bytes_read)
    except IOError:
        print(f"Error opening or reading from {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <path_to_binary_file> [-bytes N] [-c]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    num_bytes = None
    char_view = "-c" in sys.argv

    if "-bytes" in sys.argv:
        bytes_index = sys.argv.index("-bytes") + 1
        if bytes_index < len(sys.argv):
            try:
                num_bytes = int(sys.argv[bytes_index])
            except ValueError:
                print("Error: Invalid number of bytes specified.")
                sys.exit(1)

    print_hex_view(file_path, num_bytes, char_view)

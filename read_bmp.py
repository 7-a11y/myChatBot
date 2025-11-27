import sys

def get_color_from_bmp(bmp_path):
    try:
        with open(bmp_path, 'rb') as f:
            data = f.read()
            # BMP header is 54 bytes. 
            # The pixel data starts at offset 54 (usually).
            # 24-bit BMP: BGR format.
            if len(data) < 54 + 3:
                print("BMP too small")
                return
            
            # Seek to pixel array offset
            pixel_offset = int.from_bytes(data[10:14], byteorder='little')
            
            b = data[pixel_offset]
            g = data[pixel_offset + 1]
            r = data[pixel_offset + 2]
            
            print(f"RGB: {r}, {g}, {b}")
            print(f"Hex: #{r:02x}{g:02x}{b:02x}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_color_from_bmp("1x1.bmp")

# Importing the required libraries
import qrcode  # This library is used to generate QR codes
from PIL import Image  # PIL (Pillow) is used to handle image processing

# Function to generate a QR code
def generate_qr(data, version=1, box_size=10, border=4, fill_color="black", back_color="white"):
    """
    Generates a QR code with customizable size and color.
    
    Parameters:
    - data (str): The text or URL to encode in the QR code.
    - version (int): Controls the size of the QR code matrix (1 = 21x21, up to 40).
    - box_size (int): Size of each box in the QR code grid in pixels.
    - border (int): Thickness of the border (minimum is 4).
    - fill_color (str): Color of the QR code (default is black).
    - back_color (str): Background color of the QR code (default is white).
    
    Returns:
    - An Image object of the QR code.
    """
    # Creating a QRCode object with the specified parameters
    qr = qrcode.QRCode(
        version=version,      # The size of the QR code (1 is smallest, 40 is largest)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level (H = high)
        box_size=box_size,    # Size of each square in the QR code
        border=border         # Thickness of the border around the QR code
    )
    
    # Adding the data to the QR code object
    qr.add_data(data)  # The text or URL to encode
    qr.make(fit=True)  # Generates the QR code, ensuring it fits within the defined version and size
    
    # Creating an image from the QR code
    img = qr.make_image(fill_color=fill_color, back_color=back_color)  # Customizing colors
    
    # Returning the generated QR code image
    return img

# Example usage of the function
if __name__ == "__main__":
    # Asking the user for input text or URL to encode
    text = input("Enter the text or URL to generate a QR code: ")
    
    # Asking the user for optional customizations
    print("\nCustomize your QR code:")
    try:
        version = int(input("Version (1-40, default 1): ") or 1)
        box_size = int(input("Box size (pixels, default 10): ") or 10)
        border = int(input("Border size (default 4): ") or 4)
        fill_color = input("Fill color (default black): ") or "black"
        back_color = input("Background color (default white): ") or "white"
    except ValueError:
        print("Invalid input! Using default values.")
        version, box_size, border, fill_color, back_color = 1, 10, 4, "black", "white"
    
    # Generating the QR code
    qr_image = generate_qr(text, version, box_size, border, fill_color, back_color)
    
    # Saving the QR code as an image file
    file_name = input("Enter the file name to save the QR code (e.g., 'my_qr.png'): ")
    qr_image.save(file_name)  # Saving the image to the specified file
    
    print(f"QR code saved as {file_name}")

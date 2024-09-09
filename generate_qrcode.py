import qrcode

# Function to generate QR code using the QR code library;
# this is for personal use only.

def generate_qr_code(data, filename):

    # Creates an instance of a QR code
    qr = qrcode.QRCode(
        version = 1,  # Smallest QR code version
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Allows 7% error correction
        box_size=10,  # Box size for QR code
        border=4,  # Border thickness
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)  # Ensures the QR code fits the data

    # Create a black and white QR code image
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a file with a .png extension
    img.save(filename + ".png")


#Actual implementation of the function
data = "(PUT WEB URL HERE HERE)"
filename = "This_Is_Your_Filename"  # Filename without spaces
generate_qr_code(data, filename)


# Ensures QR code is saved within same file directory
print(f"QR Code generated and saved as {filename}.png")

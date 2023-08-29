# Import QR Code Library
import qrcode

# Function that generates the code in the form of an image
def generate_qrcode(text):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    return qr

def color_qr(fill, background):
    # Ask user what color they'd like the fill and background to be
    #colorlist = ['black','white','red','green','blue','yellow','orange','purple','brown','pink','turquoise', 'violet']
    while True:
        try:
            # Assuming fill and background are not already black and white respectively, ask User for preferred colors
            if fill != 'black' and background != 'white':
                fill = input("What color would you like your code material to be? (The color over the background that shows the actual code): ")
                background = input("What color would you like the background of your code to be? (Do not make it the same as your material color): ")
                if fill == background:
                    raise ValueError
                else:
                    return fill, background
            else:
                return fill, background
            break
        except ValueError:
            print("Material and Background cannot be the same color. It will become impossible to scan.")
    
def create_img(code, fill, background):
    # Creates the qr code image
    img = code.make_image(fill_color = str(fill), back_color = str(background))
    # User decides on filename
    imgname = input("Please input your desired filename, without file extension (File will be a PNG): ")
    # Image file is saved in local directory
    img.save(f"{imgname}.png")
    
        
# Main function
if __name__ == '__main__':
    # Yes and No list for the colorconfirm input
    yeslist = ['Yes', 'yes', 'Y', 'y']
    nolist = ['No', 'no', 'N', 'n']
    
    # Fill and Background string declaration for color_qr
    fill = ''
    background = ''
    
    # User inputs link they would like to generate code for
    link = input("Please enter a link or string you would like to convert into QR Code: ")
    # Code data gets created before the image is made
    code = generate_qrcode(link)
    while True:
        try:
            colorconfirm = input("Would you like to customize the colors of your QR code? (The default will be black on white) Yes/No: ")
        
            if colorconfirm in yeslist:
                fill, background = color_qr(fill, background)
            elif colorconfirm in nolist:
                fill = 'black'
                background = 'white'
                fill, background = color_qr(fill, background)
            elif colorconfirm not in yeslist and colorconfirm not in nolist:
                raise ValueError
            break
        except ValueError:
            print("Neither of those options are valid. Please enter either yes or no.")
        
    create_img(code, fill, background)
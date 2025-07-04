from PIL import Image
import random

def encrypt_image(image_path, output_path, mode='invert'):
    image = Image.open(image_path)
    image = image.convert('RGB')
    pixels = list(image.getdata())

    if mode == 'invert':
        
        encrypted_pixels = [(255 - r, 255 - g, 255 - b) for (r, g, b) in pixels]

    elif mode == 'shuffle':
        encrypted_pixels = pixels[:]
        random.shuffle(encrypted_pixels)
    
    else:
        print("Invalid encryption mode selected.")
        return

    encrypted_image = Image.new('RGB', image.size)
    encrypted_image.putdata(encrypted_pixels)
    encrypted_image.save(output_path)
    print(f"Image saved as {output_path}")

def decrypt_image(image_path, output_path, mode='invert'):
    image = Image.open(image_path)
    image = image.convert('RGB')
    pixels = list(image.getdata())

    if mode == 'invert':
        
        decrypted_pixels = [(255 - r, 255 - g, 255 - b) for (r, g, b) in pixels]

        decrypted_image = Image.new('RGB', image.size)
        decrypted_image.putdata(decrypted_pixels)
        decrypted_image.save(output_path)
        print(f"Decrypted image saved as {output_path}")

    elif mode == 'shuffle':
        print("Cannot decrypt shuffled image without a saved key or seed.")
    else:
        print("Invalid decryption mode.")

if __name__ == "__main__":
    original_image = r"C:\Users\DELL\Pictures\Sent\IMG-20211002-WA0002.jpg" 
    encrypted_image = "encrypted.jpg"     
    decrypted_image = "decrypted.jpg"     

    
    encrypt_image(original_image, encrypted_image, mode='invert')

    decrypt_image(encrypted_image, decrypted_image, mode='invert')

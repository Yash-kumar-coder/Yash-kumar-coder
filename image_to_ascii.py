import requests
from PIL import Image
from io import BytesIO
import math

def get_ascii_art(username, width=48):
    url = f"https://github.com/{username}.png"
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        
        # Convert to grayscale
        img = img.convert("L")
        
        # Calculate aspect ratio, adjusting for font height/width ratio (roughly 0.55 for taller ascii)
        aspect_ratio = img.height / img.width
        new_height = int(width * aspect_ratio * 0.55)
        
        img = img.resize((width, new_height))
        
        # ASCII characters from dark to light
        # Removed the dots at the end to make light background transparent (spaces)
        chars = ["@", "%", "#", "*", "+", "=", "-", ":", " ", " "]
        
        pixels = img.getdata()
        ascii_str = ""
        for i, pixel in enumerate(pixels):
            if i % width == 0 and i != 0:
                ascii_str += "\n"
            # Map pixel value (0-255) to index in chars array
            index = math.floor((pixel / 255) * (len(chars) - 1))
            ascii_str += chars[index]
            
        return ascii_str
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    ascii_art = get_ascii_art("Yash-kumar-coder", width=50)
    if ascii_art:
        print(ascii_art)

#import
from PIL import ImageGrab
from PIL import Image
import pytesseract
import PIL.Image
import cv2

#method to take screenshot of screen 1
def take_screenshot(save_path):
    # Capture the screen
    screenshot = ImageGrab.grab()

    # Save the screenshot
    screenshot.save(save_path)
    return save_path



#main
if __name__ == "__main__":
    # Replace 'your_screenshot_path.png' with the desired path and filename for saving the screenshot
    screenshot_path = 'your_screenshot_path.png'

    # Take a screenshot
    take_screenshot(screenshot_path)
    
    #config
    myconfig= r"--psm 6 --oem 3"
    
    # Read text from the screenshot
    extracted_text = pytesseract.image_to_string(PIL.Image.open(screenshot_path), config = myconfig)
    # Print the extracted text
    print("Extracted Text:")
    print(extracted_text)

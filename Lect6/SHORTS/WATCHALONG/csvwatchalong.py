import csv
import numpy as np
from PIL import Image

def main():
    with open(
        "views.csv", "r", encoding='utf-8') as viewWATCH, open(
            "analysis.csv","w", encoding= 'utf-8') as analysis:
        reader = csv.DictReader(viewWATCH)
        for row in reader:
            brighness = calculate_brightness(f"{row['id']}.jpeg")
            print(round(brighness, 2))



def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L")))/255
    return brightness

main()
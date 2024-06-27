# from text_extraction import extract_text
# from google_books_api import get_best_match
#
# def main(image_path):
#     # Extract text from the image
#     extracted_text = extract_text(image_path)
#     print(f"Extracted Text: \n\n{extracted_text}\n")
#
#     # Get the best matching book using the Google Books API
#     best_match = get_best_match(extracted_text)
#     print(f"Best Match: {best_match}")
#
# if __name__ == "__main__":
#     # Example usage:
#     image_path = r"D:\Computer Vision\OCR_Images\IMG.jpg"
#     main(image_path)

import requests
import cv2
import pytesseract

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image_path):
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform OCR using Tesseract
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(gray, config=custom_config)

    return text.strip()

def search_book(text):
    url = 'https://www.googleapis.com/books/v1/volumes'
    params = {
        'q': text,
        'maxResults': 10,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get('items', [])
    else:
        print(f"Error: {response.status_code}")
        return []

def get_best_match(extracted_text):
    books = search_book(extracted_text)
    if not books:
        return "No matches found."

    # Find the best match based on the highest relevance
    best_match = max(books, key=lambda x: x.get('relevance', 0))

    volume_info = best_match.get('volumeInfo', {})
    title = volume_info.get('title', 'No title')
    authors = volume_info.get('authors', ['Unknown author'])
    return f"{title}, Authors: {', '.join(authors)}"

def main(image_path):
    # Extract text from the image
    extracted_text = extract_text(image_path)
    print(f"Extracted Text: \n\n{extracted_text}\n")

    # Get the best matching book using the Google Books API
    best_match = get_best_match(extracted_text)
    print(f"Best Match: {best_match}")

if __name__ == "__main__":
    # Example usage:
    image_path = r"D:\Computer Vision\OCR_Images\IMG.jpg"
    main(image_path)

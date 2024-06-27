
<h1 align="center">OCR_Translator</h1>

<p align="center">
  <a href="https://www.youtube.com/watch?v=h8sp7vFeV7c"><img src="https://i.imgur.com/gZxakIi.png" alt="YouTube Demonstration" width="800"></a>
</p>

<h2>Description</h2>

<p>The goal of this project was to develop a program taht used AI with OCR (Optical Character Recognition) to analyze images taken in by the program. It takes an image from file path in the program, looks for any text taht in this case will be a page from a book, and tries to find what book that page is from using the Google Books API.</p>

<h2>Languages and Utilities Used</h2>

<ul>
  <li><b>Python</b></li>
  <li><b>Tesseract</b></li>
  <li><b>Google Books API</b></li>
</ul>

<h2>Environments Used</h2>

<ul>
  <li><b>Windows 11</b></li>
  <li><b>PyCharm</b></li>
</ul>

<h2>
<a href="https://github.com/pedromussi1/OCRbookFinder/blob/main/READCODE.md">Code Breakdown Here!</a>
</h2>

<h2>Project Walk-through</h2>

<p>Download files, install Tesseract and Google Books into Python Interpreter. Run main.py file.</p>

<h3>Book Page</h3>

<p align="center">
  <kbd><img src="https://i.imgur.com/jDDXD9P.jpeg" alt="BookPage"></kbd>
</p>

<p>The first step is to take in the book page the program will be analyzing and translating. In my case, I have selected the introduction of the book 'Art of War' by Sun Tzu. The program my identify all the text in the image and translate it.</p>

<h3>Transcribing text in image</h3>

<p align="center">
  <kbd><img src="https://i.imgur.com/8htNEXy.png" alt="TranscribingImage"></kbd>
</p>

<p>The next step is transcribing the image to text and printing it to the console using OCR. We can see from the image above that the program does that correctly. Now what needs to be done is translate it to a language of choice.</p>

<h3>Translating Text</h3>

<p align="center">
  <kbd><img src="https://i.imgur.com/U1XvLjI.png" alt="TranslatingText"></kbd>
</p>

<p>The last step in the program is translating the text that has been transcribed by using the Azure AI Translator. We can see above the translated text. For this example I opted to translate to Brazilian Portuguese.</p>


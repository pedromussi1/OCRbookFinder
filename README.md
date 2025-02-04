
<h1 align="center">OCR_BookFinder</h1>

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

<hr>

<h3>Book Page</h3>

<p align="center">
  <kbd><img src="https://i.imgur.com/GCZqyTU.jpeg" alt="BookPage" width="900"></kbd>
</p>

<p>The first step is to take in the book page the program will be analyzing. The program will identify all the text in the image and try to find what book it is from by using Google Books API.</p>

<hr>

<h3>Transcribing text in image</h3>

<p align="center">
  <kbd><img src="https://i.imgur.com/8Ews4QR.png" alt="TranscribingImage"></kbd>
</p>

<p>The next step is transcribing the image to text and printing it to the console using OCR. We can see from the image above that the program does that correctly. The last part of the program will be to find what book the page is from.</p>

<hr>

<h3>Identifying what Book the text is from</h3>

<p align="center">
  <kbd><img src="https://i.imgur.com/jDpXSXE.png" alt="TranslatingText"></kbd>
</p>

<p>The last step in the program is using the Google Books APi to find what book the page being analyzed is from. The API compares the text we have provided to their library of book titles, trying to find a match. You can see in the image above that the best match the program has found is Frank Herbert's "Dune", which is the correct answer.</p>


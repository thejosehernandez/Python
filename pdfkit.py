#test script

import pdfkit

config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
beforePath = "C:/Users/Jose/Desktop/before/1.html"
afterPath = "C:/Users/Jose/Desktop/after/1.pdf"

pdfkit.from_file(beforePath, afterPath, configuration=config)
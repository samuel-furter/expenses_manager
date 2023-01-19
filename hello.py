from PyPDF2 import PdfReader
import matplotlib

reader = PdfReader("salary\Décompte de salaire decembre 2022.PDF")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n" 

print(text)
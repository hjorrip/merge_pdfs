import sys
import subprocess

# Check if PyPDF2 is installed
try:
    import PyPDF2
except ImportError:
    # PyPDF2 is not installed, so install it via pip
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
    import PyPDF2

# Get the list of input PDF filenames from command line arguments
input_filenames = sys.argv[1:]

# Create a PdfWriter object to hold the merged PDF
pdf_writer = PyPDF2.PdfWriter()

# Loop through each input file
for filename in input_filenames:
    # Open the input file in read-binary mode
    with open(filename, 'rb') as pdf_file:
        # Create a PdfReader object to read the input PDF
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        # Loop through each page in the input PDF and add it to the PdfWriter object
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

# Write the merged PDF to a file named 'merged.pdf'
output_filename = 'merged.pdf'
with open(output_filename, 'wb') as output_file:
    pdf_writer.write(output_file)

# Print the name of the output file
print(f"Merged PDF file created: {output_filename}")

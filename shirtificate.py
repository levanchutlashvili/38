from fpdf import FPDF

# Create a subclass of FPDF to add a header
class Shirtificate(FPDF):
    def header(self):
        # Set the font and size for the header
        self.set_font('Arial', 'B', 15)
        # Add the header text
        self.cell(0, 40, 'CS50 Shirtificate', 0, 0, 'C')
        # Add a line break after the header
        self.ln(20)

# Create a new shirtificate PDF
pdf = Shirtificate(orientation='P', unit='mm', format='A4')
pdf.add_page()

# Disable automatic page breaks
pdf.set_auto_page_break(False)

# Load the image of the shirt and center it horizontally
pdf.image('shirtificate.png', x=50, y=50, w=100)

# Set the font and size for the main text
pdf.set_font('Arial', '', size=50)
# Prompt the user for their name
name = input('Enter your name: ')

# Add the user's name to the PDF
pdf.cell(0, 120, name, 0, 0, 'C', 0)
pdf.ln(10)

# Output the PDF to a file
pdf.output('shirtificate.pdf', 'F')

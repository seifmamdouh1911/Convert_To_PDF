from fpdf import FPDF

# Create a class for the PDF document
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Lecture 02 Summary: Circuit Analysis and Theorems", align="C", ln=True)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

    def add_summary(self, text):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, text)
        self.ln()

# Summary text for Lecture 2 with simplified characters
summary_text_lecture_2 = """
here you can write the content you want to convert it to PDF file.
"""

# Create PDF with the summary content
pdf = PDF()
pdf.add_page()
pdf.add_summary(summary_text_lecture_2)

# Save the PDF to a file
pdf.output("Lecture_02_Summary.pdf")

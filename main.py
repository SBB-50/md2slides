from fpdf import FPDF

pdf = FPDF(orientation="P",unit="pt",format=(1200,900))
pdf.set_top_margin(100)
pdf.set_right_margin(100)

def text(text):
    pdf.set_font('Helvetica', size=48)
    pdf.set_left_margin(200)
    pdf.multi_cell(0,text=text, markdown=True)
    pdf.ln(75)
def title(text):
    pdf.set_font('Helvetica', size=98)
    pdf.set_left_margin(50)
    pdf.cell(40,10,text)
    pdf.ln(100)
def mdtrans(markdown):
    step1 = markdown.replace("*","__")
    step2 = step1.replace("____","**")
    return step2

pdf.add_page()
title("header example")
swag1 = mdtrans("*body text example*")
swag2 = mdtrans("**body text example**")
text(swag1)
text(swag2)
pdf.add_page()
title("page 2 header example")
text("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
text("body text example")
pdf.output("hello_world.pdf")

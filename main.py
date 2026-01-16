from fpdf import FPDF
import sys

if __name__ == "__main__":
    if len(sys.argv) > 2:
        file_path = sys.argv[1]
        file_output_name=sys.argv[2]
    else:
        if len(sys.argv) > 1:
            file_path = sys.argv[1]
            print("output file name not given, outputting to output.pdf")
            file_output_name="output.pdf"
        else:
            print("no input file, exiting")
            quit()

pdf = FPDF(orientation="P",unit="pt",format=(1200,900))
pdf.set_top_margin(100)
pdf.set_right_margin(100)
pdf.add_font("uHelvetica", style="", fname="Helvetica.ttf")
pdf.add_font("uHelvetica", style="b", fname="Helvetica-Bold.ttf")
pdf.add_font("uHelvetica", style="i", fname="Helvetica-Oblique.ttf")
pdf.add_font("uHelvetica", style="bi", fname="Helvetica-BoldOblique.ttf")

#body text function
def text(text):
    pdf.set_font('uHelvetica', size=48)
    pdf.set_left_margin(200)
    pdf.multi_cell(0,text=text, markdown=True)
    pdf.ln(75)
#title function
def title(text):
    pdf.set_font('uHelvetica', size=98)
    pdf.set_left_margin(50)
    pdf.multi_cell(0,text=text,align="L")
    pdf.ln(0)
#markdown translation function
def mdtrans(markdown):
    step1 = markdown.replace("*","__")
    step2 = step1.replace("____","**")
    step3 = step2.replace("-","•")
    return step3
try: 
    with open(file_path) as file:
        content = file.readlines()
    for i in range (len(content)):
        if (content[i][0] == '#'):
            pdf.add_page()
            title(content[i][1:])
        else:
            text(mdtrans(content[i]).removesuffix("\n"))
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print (f'an error occurred: {e}')
pdf.output(file_output_name)

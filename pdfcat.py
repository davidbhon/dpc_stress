#!/env/bin python3
import os, sys

cover_page = 'CUI_1.pdf'
args = None
pdf_rdr = pdf_wtr = None

try:
  import PyPDF2, puremagic
  pdfer = PyPDF2.PdfFileWriter()
except Exception as e:
  print(e) ; print("please pip install pypdf2 puremagic") 
  sys.exit()


def concater(pdflist):
  try:
    for pdf in pdflist:
      pdf_obj = open(pdf, 'rb')
      pdf_rdr = PyPDF2.PdfFileReader(pdf_obj)
      for page_num in range(pdf_rdr.numPages):
        page_obj = pdfReader.getPage(page_num)
        pdf_wtr.addPage(page_obj)
  except:
    print(e) ; print("concater> TBD exception with PDF I/O and/or use of PyPDF2")
    return


def main(args, outfile='concated_files.pdf'):
  # set file list
  concat = [cover_page]

  for pdf in args:
    ftyp = puremagic.magic_file(pdf)
    print(pdf, 'puremagic indicates filetype: ', ftyp)
    if 'pdf' in ftyp:
      concat.append(pdf)
    else:
      print("sorry but puremagic asserts file is not a PDF")
  try:
    pdfOutput = open(outfile, 'wb')
    pdf_wtr.write(pdfOutput)
  except Exception as e:
    print(e)

if __name__ == "__main__":
  if not(len(sys.argv) > 1 ):
    print("please provide at least 2 PDF filenames to concat left to right")
    sys.exit()

  args = sys.argv[1:]
  main(args)

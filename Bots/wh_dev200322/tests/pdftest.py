import os
from pathlib import Path

from borb.pdf.canvas.layout.page_layout.multi_column_layout import SingleColumnLayout
from borb.pdf.canvas.layout.text.paragraph import Paragraph
from borb.pdf.document.document import Document
from borb.pdf.page.page import Page
from borb.pdf.pdf import PDF


class PDF_Document:
    def __init__(self):
        # create an empty Document
        self.__document = Document()

        # create an empty page
        self.__page = Page()

        # add empty page to document
        self.__document.append_page(self.__page)

        # use a PageLayout (SingleColumnLayout in this case)
        self.__layout = SingleColumnLayout(self.__page)

    def getdocument(self):
        return self.__document

    def getpage(self):
        return self.__page

    def getlayout(self):
        return self.__layout

    def save(self, filename):
        with open(Path(f"{filename}.pdf"), "wb") as pdf_file_handle:
            PDF.dumps(pdf_file_handle, self.__document)


if __name__ == '__main__':
    # files stuff
    markname = "watermark"
    docname = "document"
    origname = "original"

    # pdf stuff
    pdf = PDF_Document()
    doc = pdf.getdocument()
    page = pdf.getpage()
    layout = pdf.getlayout()

    # add text to page
    layout.add(Paragraph("hi"))

    # add another one empty page
    doc.append_page(Page())

    # save document
    pdf.save(filename=origname)

    # add watermark
    os.system(
        f"pdftk {origname}.pdf background {markname}.pdf output {docname}.pdf")

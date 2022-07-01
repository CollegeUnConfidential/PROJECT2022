import PyPDF2 as pypdf
import urllib.request as urllib
from io import StringIO, BytesIO

def findInDict(needle, haystack):
    for key in haystack.keys():
        try:
            value=haystack[key]
        except:
            continue
        if key==needle:
            return value
        if isinstance(value,dict):            
            x=findInDict(needle,value)            
            if x is not None:
                return x

def download_pdf(download_url):
    writer = pypdf.PdfFileWriter()
 
    remoteFile = urllib.urlopen(urllib.Request(download_url)).read()
    memoryFile = BytesIO(remoteFile)
    pdfFile = pypdf.PdfFileReader(memoryFile)

    information = pdfFile.getDocumentInfo()
    number_of_pages = pdfFile.getNumPages()

    txt = f"""

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)

    for pageNum in range(pdfFile.getNumPages()):
            currentPage = pdfFile.getPage(pageNum)
            #currentPage.mergePage(watermark.getPage(0))
            writer.addPage(currentPage)
            print(pageNum)




    outputStream = open("output.pdf","wb")
    writer.write(outputStream)
    outputStream.close()


def main():
    pdfURL = 'https://www3.nd.edu/~instres/CDS/2021-2022/CDS_2021-2022.pdf'
    pdfobject = download_pdf(pdfURL)

    
    #pdf=pypdf.PdfFileReader(pdfobject)

    #for i in range(3):
    #    page = pdf.pages[i]
    #    print(f"working on page {i}")
    #    print(page.extract_text())

    #xfa=findInDict('/XFA',pdf.resolvedObjects)
    #xml=xfa[7].getObject().getData()

    #for line in xml: # files are iterable
    #    print(line)

if __name__ == "__main__":
    main()
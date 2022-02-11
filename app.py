from PIL import Image
import os
import pathlib
import  PyPDF2


class ImagesToPdf:
    def __init__(self,img_path,new_pdf_path,file_name):
        self.img_path = img_path
        self.new_pdf_path = new_pdf_path
        self.filename = file_name
        self.ImgToPdf(self.img_path,"temporary")

    
    def ImgToPdf(self,img_path,new_path):
        
        for image in os.listdir(img_path):
            print(image)
            
            #innitializing the image object on picture
            img_complete_path = os.path.join(img_path,image)
            
            img = Image.open(img_complete_path)
            
            #saving images as pdf
            new_file_name = pathlib.Path(image).stem + ".pdf"
            pdf_file_path = os.path.join(new_path,new_file_name)
            
            img.save(pdf_file_path,format="PDF")
            
            self.MergePdf(new_path,self.new_pdf_path,self.filename)
    

    def MergePdf(self,pdf_path,new_pdf_path,new_file_name):
         #creating new pdf object
         pdfMerger = PyPDF2.PdfFileMerger()
         
         #looping through the pdf files
         for pdf in os.listdir(pdf_path):
             pdf_file_path = os.path.join(pdf_path,pdf)
             pdfMerger.append(pdf_file_path)
             
         #saving the pdf file
         new_path = os.path.join(new_pdf_path,new_file_name)
         with open(new_path,"wb") as pdf_file:
             pdfMerger.write(pdf_file)
                
              

ImagesToPdf("pictures","pdf_result","result.pdf")
    
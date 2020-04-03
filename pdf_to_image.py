from pdf2image import convert_from_path, convert_from_bytes

def convert_to_image(pdf_path):
    
    
    des_path = ("./assets/img/")
    images = convert_from_path(pdf_path,dpi=600)

    for i,image in enumerate(images):
        fname = "CV_%i"%(i+1) + ".png"
        image.save(des_path+fname, 'PNG')
        
    print('Convert %s to image: SUCCESS'%pdf_path)


if __name__=="__main__":
    
 PDF_PATHS =["Quang_Nguyen_CV.pdf"]
    
 for path in PDF_PATHS:
    convert_to_image(path)

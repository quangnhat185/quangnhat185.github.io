from pdf2image import convert_from_path, convert_from_bytes
import shutil
import os
def convert_to_image(pdf_path):
    des_path = ("./assets/img/")
    images = convert_from_path(pdf_path,dpi=600)

    for i,image in enumerate(images):
        fname = "CV_%i"%(i+1) + ".png"
        image.save(des_path+fname, 'PNG')        
    print('[INFO] Convert %s to image successfully...'%pdf_path)
    
def update_pdf(pdf_latex_path, new_name):
    if os.path.isfile(new_name):
        os.remove(new_name)
        
    old_name = os.path.basename(pdf_latex_path)
    shutil.copy(pdf_latex_path,"./")
    os.rename(old_name, new_name)
    print("[INFO] Update pdf file successfully...")          

if __name__=="__main__":
    
    # PDF_PATHS = ["Quang_Nguyen_CV.pdf"]
    # update_pdf(PDF_LATEX_PATH,PDF_PATHS[0])
    PDF_PATHS = "Quang_Nhat_Nguyen_Le_CV.pdf"

    convert_to_image(PDF_PATHS)        
    # for path in PDF_PATHS:
    #     convert_to_image(path)

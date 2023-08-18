from fastapi import APIRouter, Query, UploadFile, File
import pdfplumber
import os
import shutil

router = APIRouter()

upload_folder = "/tmp/documents"


def create_file(filedata):
    global upload_folder
    file_object = filedata.file
    # create empty file to copy the file_object to
    if not os.path.exists(upload_folder):
        os.mkdir(upload_folder)
    path = os.path.join(upload_folder, filedata.filename)
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file_object, buffer)

    return path

@router.post("/get_number_of_pages")
def parse_data(
    filedata: UploadFile = File(...)
):
    file = create_file(filedata)
    pdf = pdfplumber.open(file)

    pages = pdf.pages[0]
    total_pages = len(pdf.pages)
    contents = pages.extract_words()

    all_texts = []
    for content in contents:
        text = content["text"]
        all_texts.append(text)

    return {"Total number of pages": total_pages}

@router.post("/get_pdf_contents")
def parse_data(
    filedata: UploadFile = File(...),
    page_num: str = Query(None, description="")
):
    file = create_file(filedata)
    pdf = pdfplumber.open(file)

    pages = pdf.pages[int(page_num)-1]
    contents = pages.extract_words()

    all_texts = []
    for content in contents:
        text = content["text"]
        all_texts.append(text)

    return {"pdf contents": " ".join(all_texts)}
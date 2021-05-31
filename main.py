import pytesseract

from PIL import ImageGrab

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def get_clipboard_img():
    try:
        return ImageGrab.grabclipboard()
    except:
        return None


def get_text_from_img(img):
    img_to_text = pytesseract.image_to_string(img).strip()
    return img_to_text.replace("  ", " ").replace("  ", " ").replace("\n\n", "\n").replace("\n\n", "\n")


def main():

    save_doc = "save_doc.txt"
    text_list = []

    while True:
        clipboard_img = get_clipboard_img()
        if clipboard_img is None:
            continue

        img_to_text = get_text_from_img(clipboard_img)

        if len(text_list) == 0 or text_list[-1] != img_to_text:
            text_list.append(img_to_text)
            str_ret = \
                "---- Image #{} -----------------\n{}\n".format(
                    str(len(text_list)).rjust(5, "0"),
                    img_to_text
                )
            print(str_ret)
            with open(save_doc, "a") as myfile:
                myfile.write(str_ret + "\n")


if __name__ == '__main__':
    main()

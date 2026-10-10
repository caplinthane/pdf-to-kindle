# PyMuPDF import
import pymupdf


def main():
    filename = input("Enter PDF filename: ")

    # opens pdf file
    document = pymupdf.open(filename)

    # creates empty python list
    pages = []

    # prints the actual pdf text
    for page in document:
        text = page.get_text()
        # takes text from page and puts it in the list
        pages.append(text)

    print("Number of pages:", len(pages))

    for number, page in enumerate(pages):
        if len(page) == 0:
            print("Empty page:", number)

    # retrieve eleventh page
    # calls pymupdf layout blocks
    # avoids one long string of text
    cleaned_pages = []

    for page in document:
        blocks = page.get_text("blocks")
        cleaned_blocks = []

        # each block processed in turn
        for block in blocks:
            x0, y0, x1, y1, text, block_number, block_type = block

            cleaned_text = text.strip()
            cleaned_text = cleaned_text.replace("\x07", "")

            if cleaned_text:
                cleaned_blocks.append(cleaned_text)

        cleaned_pages.append(cleaned_blocks)

    print("Number of processed pages:", len(cleaned_blocks))

    for number, page_blocks in enumerate(cleaned_pages):
        print(f"Page {number + 1}: {len(page_blocks)} blocks")


if __name__ == "__main__":
    main()

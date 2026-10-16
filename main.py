# PyMuPDF import
import pymupdf


def main():
    filename = input("Enter PDF filename: ")

    # opens pdf file
    document = pymupdf.open(filename)

    # array to store cleaned text blocks on each pdf page
    cleaned_pages = []

    for page in document:
        blocks = page.get_text("blocks")
        cleaned_blocks = []

        # each block processed in turn
        for block in blocks:
            text = block[4]

            # replace pdf symbols and whitespace
            cleaned_text = text.strip()
            cleaned_text = cleaned_text.replace("\x07", "")

            if cleaned_text:
                cleaned_blocks.append(cleaned_text)

        cleaned_pages.append(cleaned_blocks)

    print("Number of pages:", len(document))
    print("Number of processed pages:", len(cleaned_pages))

    page_number = 10

    if page_number < len(cleaned_pages):
        print(f"\nInspecting page {page_number + 1}:")

        for block_number, block in enumerate(cleaned_pages[page_number]):
            print(f"Block {block_number}: {block!r}")


if __name__ == "__main__":
    main()

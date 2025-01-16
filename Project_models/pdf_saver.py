import os
import asyncio

#This function saves the desired pdf to project file for further use.

# Define the file path to save the text

current_dir = os.path.dirname(os.path.abspath(__file__))
save_folder = os.path.join(current_dir, "documents")
os.makedirs(save_folder, exist_ok=True)  # Ensure the directory exists
txt_file_path = os.path.join(save_folder, "annual_report_2023.txt")

async def save_pdf_as_txt(file_path, save_path):
    from langchain_community.document_loaders import PyPDFLoader

    async def load_pages():
        loader = PyPDFLoader(file_path)
        pages = []
        async for page in loader.alazy_load():
            pages.append(page.page_content)  # Extracting text from each page
        return pages

    # Load pages asynchronously and save to a text file
    pages = await load_pages()
    with open(save_path, "w", encoding="utf-8") as f:
        f.write("\n".join(pages))
    
    print(f"Text extracted and saved to {save_path}")

# Define the PDF path and run the function
file_path = (
    "file path"
)

async def main():
    await save_pdf_as_txt(file_path, txt_file_path)

# Run the asynchronous task
asyncio.run(main())

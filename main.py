import PyPDF2
import pyttsx3


def pdf_to_speech(pdf_path):
    # Initialize text-to-speech engine
    speaker = pyttsx3.init()

    # Open the PDF file
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            # Loop through each page and read the text
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text = page.extract_text()

                if text:
                    print(f"Reading page {page_num + 1}...")
                    speaker.say(text)
                else:
                    print(f"No readable text on page {page_num + 1}.")

            speaker.runAndWait()
    except FileNotFoundError:
        print("PDF file not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")


pdf_to_speech('How_AI_Chatbots_Work.pdf')

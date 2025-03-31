import fitz  # Это PyMuPDF
import os

def extract_images_from_pdf(pdf_path, output_folder="images"):
    # Проверяем, есть ли PDF
    if not os.path.exists(pdf_path):
        print(f"Файл {pdf_path} не найден!")
        return []

    # Открываем PDF
    try:
        pdf = fitz.open(pdf_path)
        print(f"Открыл PDF, страниц: {len(pdf)}")
    except:
        print("Не могу открыть PDF!")
        return []

    # Создаём папку для картинок
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Создал папку {output_folder}")

    image_list = []
    for page_num in range(len(pdf)):
        page = pdf[page_num]
        images = page.get_images(full=True)
        print(f"Страница {page_num + 1}: нашёл {len(images)} картинок")

        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = pdf.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_name = f"{output_folder}/page_{page_num + 1}_img_{img_index}.{image_ext}"
            with open(image_name, "wb") as image_file:
                image_file.write(image_bytes)
            image_list.append(image_name)
            print(f"Сохранил {image_name}")

    pdf.close()
    if not image_list:
        print("Картинок не нашёл!")
    return image_list

if __name__ == "__main__":
    pdf_path = "manga.pdf"  # Замени на имя своего PDF
    images = extract_images_from_pdf(pdf_path)
    print("Готово! Список картинок:", images)
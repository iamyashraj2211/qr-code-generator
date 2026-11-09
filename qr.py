import qrcode


def generate_qr(data: str, filename: str = "qrcode.png"):
    img = qrcode.make(data)
    img.save(filename)
    print(f"QR code successfully saved as {filename}\n")


while True:
    print("--- QR CODE GENERATOR ---")
    print("1. Enter text/data to generate QR code")
    print("2. Enter image/web URL to generate QR code")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        text = input("Enter the text: ").strip()
        generate_qr(text, "text_qr.png")

    elif choice == "2":
        url = input("Enter the URL: ").strip()
        generate_qr(url, "url_qr.png")

    elif choice == "3":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.\n")
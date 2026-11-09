import io
import qrcode
import streamlit as st

st.set_page_config(page_title="QR Code Generator", page_icon=":qrcode:", layout="centered")
st.title("QR Code Generator")
st.write("Generate QR codes for text or URLs easily.")

user_input = st.text_area("Enter text or URL:", height=100)

if st.button("Generate QR Code"):
    if user_input:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(user_input)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image to a BytesIO object
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)

        st.image(img_bytes, caption="Generated QR Code", use_column_width=True)
        st.download_button(
            label="Download QR Code",
            data=img_bytes,
            file_name="qrcode.png",
            mime="image/png"
        )
    else:
        st.warning("Please enter some text or URL to generate a QR code.")
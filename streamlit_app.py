import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# 앱 제목
st.title("QR 코드 생성기")
st.write("텍스트를 입력하면 QR 코드를 생성합니다.")

# 사용자 입력
text = st.text_input("QR 코드에 포함할 텍스트를 입력하세요:")

# QR 코드 생성 버튼
if st.button("Generate QR Code"):
    if text.strip():
        # QR 코드 생성
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        # QR 코드를 이미지로 변환
        img = qr.make_image(fill="black", back_color="white")

        # 이미지를 화면에 표시
        st.image(img, caption="생성된 QR 코드", use_column_width=True)

        # QR 코드 다운로드
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        st.download_button(
            label="QR 코드 다운로드",
            data=buffer,
            file_name="qrcode.png",
            mime="image/png"
        )
    else:
        st.error("텍스트를 입력해주세요!")

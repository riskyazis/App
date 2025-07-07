
import streamlit as st

# Judul dan Gambar Hint
st.set_page_config(page_title="Ucapan Ulang Tahun", layout="centered")
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://i.pinimg.com/originals/e9/e0/35/e9e03538f6ab69c626cfbdb8cc7bc4a3.gif"
             style="width: 300px; border-radius: 15px; box-shadow: 0 0 10px rgba(0,0,0,0.3);" />
        <h3>Petunjuk ada di sini... 😏</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Password Input
password_input = st.text_input("🔐 Masukkan password:", type="password")

# Target password
real_password = "iloveyou"

# Simpan jumlah percobaan salah
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# Cek password
if password_input:
    if password_input == real_password:
        st.success("✅ Password benar!")

        st.markdown(
            """
            <div style="
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(to right, #fbc2eb, #a6c1ee);
                padding: 30px;
                border-radius: 20px;
                text-align: center;
                color: #333;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                margin-top: 30px;
            ">
                <h2>🎉 Selamat Ulang Tahun! 🎂</h2>
                <p style="font-size: 18px;">
                    Hai <b>__________</b>,<br><br>
                    Di usia yang ke-<b>___</b> ini, semoga kamu selalu sehat, bahagia, dan sukses dalam setiap langkahmu!<br><br>
                    Dengan cinta,<br>
                    <b>__________</b>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.session_state.attempts += 1
        hint = " ".join(real_password[:st.session_state.attempts])
        st.error("❌ Password salah!")
        st.info(f"🔎 Petunjuk tambahan: `{hint}`")

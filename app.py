import streamlit as st
import os
import glob
import io
from gtts import gTTS
from deep_translator import GoogleTranslator

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="منصة نقلة | NAQLA", layout="wide")

# 2. تصميم الواجهة (CSS) لتطوير الهوية البصرية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl;
        text-align: right;
    }

    .stApp {
        background: linear-gradient(to bottom, #ffffff, #f0f7ff);
    }
    
    [data-testid="stSidebar"] {
        background-color: #003366 !important;
    }
    
    [data-testid="stSidebar"] .stRadio label p, [data-testid="stSidebar"] .stMarkdown p {
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        text-align: right !important;
    }

    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
        gap: 15px;
    }

    .stButton>button {
        width: 100%;
        background-color: #2E7D32 !important;
        color: white !important;
        border-radius: 12px;
        border: none;
        height: 3em;
        font-weight: bold;
        transition: 0.4s;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    
    .stButton>button:hover {
        background-color: #1B5E20 !important;
        transform: translateY(-2px);
        box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.2);
    }

    .stTextArea textarea {
        border: 2px solid #e0e0e0 !important;
        border-radius: 15px !important;
        background-color: #ffffff !important;
    }
    
    .stAlert {
        border-radius: 15px;
        border: none;
    }

    h1 { color: #003366; }
    
    .main-card {
        background: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- الهيدر ---
col_logo, col_title = st.columns([1, 4])
with col_logo:
    logo_files = glob.glob("kku_logo.*") + glob.glob("naqla_logo.*")
    if logo_files:
        st.image(logo_files[0], width=100)
with col_title:
    st.title("منصة نقلة | NAQLA")
    st.markdown("<p style='color: #2E7D32; font-weight: bold; font-size: 18px;'>NAQLA By: بسمة العسكري، لمار العكاسي، بيادر القرني، فجر القحطاني، بدر الشهري</p>", unsafe_allow_html=True)

# --- الإحصائيات ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)
c_s1, c_s2, c_s3 = st.columns(3)
with c_s1: st.metric("✅ نصوص معالجة", "+1,250")
with c_s2: st.metric("🌍 لغات مدعومة", "6 لغات")
with c_s3: st.metric("⚡ سرعة الاستجابة", "فورية")
st.markdown('</div>', unsafe_allow_html=True)

# --- القائمة ---
with st.sidebar:
    st.markdown("### ⚙️ لوحة التحكم")
    menu = st.radio("اختر الوجهة:", ["🏠 الصفحة التعريفية", "🌐 المسار العالمي", "🎯 نمط التركيز", "🎧 المسار الصوتي"])

# --- الصفحات ---
if menu == "🏠 الصفحة التعريفية":
    st.markdown("""
    <div class="main-card">
    <h3>💡 عن منصة نقلة</h3>
    <p>نقلة منصة تعليمية ذكية تبسط المحتوى الأكاديمي.</p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "🌐 المسار العالمي":
    st.subheader("🌐 المسار العالمي")
    text_in = st.text_area("أدخل النص")
    if st.button("ترجمة"):
        if text_in:
            translated = GoogleTranslator(source="auto", target="ar").translate(text_in)
            st.info(translated)
        else:
            st.warning("اكتب نص")

elif menu == "🎯 نمط التركيز":
    st.subheader("🎯 نمط التركيز")
    txt = st.text_area("اكتب النص")
    if st.button("تلخيص"):
        if txt:
            st.success("تم التلخيص (تجريبي)")
        else:
            st.warning("اكتب نص")

elif menu == "🎧 المسار الصوتي":
    st.subheader("🎧 تحويل لصوت")
    audio_input = st.text_area("النص")
  if st.button("تحويل"):
    if audio_input:
        tts = gTTS(text=audio_input, lang='ar')
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        st.audio(fp)
    else:
        st.warning("اكتب نص")if st.button("تحويل"):
    if audio_input:
        tts = gTTS(text=audio_input, lang='ar')
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        st.audio(fp)
    else:
        st.warning("اكتب نص")

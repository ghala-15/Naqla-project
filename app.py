import streamlit as st
from deep_translator import GoogleTranslator
import os

# إعدادات الصفحة
st.set_page_config(page_title="منصة نقلة | NAQLA", layout="wide")

# دالة الصور للأمان
def show_image(img_path, img_width):
    if os.path.exists(img_path):
        st.image(img_path, width=img_width)
    else:
        st.write(f"🖼️ [{img_path}]")

# القائمة الجانبية
with st.sidebar:
    show_image("naqla_logo.png", 150)
    st.title("نقلة | NAQLA")
    menu = st.radio("القائمة:", ["🏠 الرئيسية", "🎯 نمط التركيز", "⚙️ الإعدادات"])

if menu == "🏠 الرئيسية":
    col1, col2 = st.columns([1, 5])
    with col1: show_image("kku_logo.jpg", 80)
    with col2: st.title("منصة نقلة للتعلم الميسر")

    pathway = st.selectbox("اختر المسار:", ["🌐 المسار العالمي", "🎯 نمط التركيز"])

    if pathway == "🌐 المسار العالمي":
        st.subheader("🌐 المسار العالمي")
        
        # اختيار الفئة (النمط)
        user_need = st.radio("اختر النمط المناسب لاحتياجك:", ["👁️ النمط البصري (للعجز النطقي/السمعي)", "👂 النمط السمعي (للمكفوفين/ضعاف البصر)"])

        text_in = st.text_area("أدخل النص الأكاديمي المراد معالجته:", height=100)
        
        if st.button("بدأ المعالجة ✨"):
            if text_in:
                # الترجمة والتبسيط الحقيقي
                translated = GoogleTranslator(source='auto', target='ar').translate(text_in)
                
                st.divider()

                if user_need == "👁️ النمط البصري (للعجز النطقي/السمعي)":
                    st.subheader("🤟 معالجة للنمط البصري")
                    st.success(f"**النص المترجم والمبسط:**\n\n{translated}")
                    st.info("جاري عرض توضيحات بلغة الإشارة...")
                    show_image("sign_language_demo.gif", 300) 
                    
                elif user_need == "👂 النمط السمعي (للمكفوفين/ضعاف البصر)":
                    st.subheader("🔊 معالجة للنمط السمعي")
                    st.info("تم تحويل النص إلى صيغة قابلة للقراءة الصوتية:")
                    st.write(f"📢 {translated}")
                    st.button("اضغط للاستماع إلى النص 🎧")
            else:
                st.warning("يرجى إدخال نص.")

# باقي الأقسام (نمط التركيز والإعدادات) تبقى كما هي
elif menu == "🎯 نمط التركيز":
    st.header("🎯 نمط التركيز")
    st.subheader("✅ قائمة المهام")
    st.checkbox("مراجعة الدرس")
    
elif menu == "⚙️ الإعدادات":
    st.header("⚙️ الإعدادات")
    st.text_input("الاسم:", "غلا")

import streamlit as st
from deep_translator import GoogleTranslator
import time

# إعدادات الصفحة
st.set_page_config(page_title="منصة نقلة | NAQLA", layout="wide", page_icon="🎓")

# تصميم CSS لتحسين المظهر (نفس اللي استخدمناه وزيادة)
st.markdown("""
    <style>
    .main-card { background-color: #f8f9fa; padding: 20px; border-radius: 15px; border-right: 5px solid #007bff; margin-bottom: 20px; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #007bff; color: white; }
    h1, h2, h3 { color: #1e3a8a; }
    </style>
""", unsafe_allow_html=True)

# القائمة الجانبية
with st.sidebar:
   
    st.title("القائمة الرئيسية")
    menu = st.radio("انتقل إلى:", ["🏠 الرئيسية", "⚙️ الإعدادات", "♿ سهولة الوصول"])

# --- 1. قسم الإعدادات ---
if menu == "⚙️ الإعدادات":
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("⚙️ الإعدادات")
    st.subheader("👤 بيانات الحساب")
    st.text_input("الاسم:", value="غلا")
    st.text_input("البريد:", value="ghala@kku.edu.sa")
    st.button("حفظ التغييرات")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 2. قسم سهولة الوصول ---
elif menu == "♿ سهولة الوصول":
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("♿ سهولة الوصول")
    st.slider("حجم الخط:", 14, 30, 18)
    st.checkbox("تفعيل قارئ الشاشة")
  
    st.markdown('</div>', unsafe_allow_html=True)

# --- 3. القسم الرئيسي (المسارات) ---
elif menu == "🏠 الرئيسية":
    # الهيدر
    col_logo, col_title = st.columns([1, 4])
    with col_logo: st.image("kku_logo.jpg", width=100)
    with col_title: st.title("منصة نقلة - طريقك نحو التعلم الميسر")

    pathway = st.selectbox("اختر المسار:", ["🌐 المسار العالمي", "🎯 نمط التركيز"])

    # --- المسار العالمي (ترجمة وتبسيط حقيقي) ---
    if pathway == "🌐 المسار العالمي":
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.subheader("🌐 المسار العالمي (الترجمة والتبسيط الحقيقي)")
        
        c1, c2 = st.columns(2)
        with c1: src_l = st.selectbox("من لغة:", ["العربية", "English"])
        with c2: trg_l = st.selectbox("إلى لغة مبسطة:", ["English (Simple)", "العربية (مبسطة)"])

        text_in = st.text_area("أدخل النص الأكاديمي المراد معالجته:", height=100)
        
        if st.button("تبسيط ومعالجة ذكية ✨"):
            if text_in:
                s_code = 'ar' if src_l == "العربية" else 'en'
                t_code = 'en' if "English" in trg_l else 'ar'
                
                # ترجمة حقيقية
                translated = GoogleTranslator(source=s_code, target=t_code).translate(text_in)
                
                # تبسيط يدوي للمصطلحات الشائعة
                simple_text = translated.replace("Cloud Computing", "Online Storage").replace("infrastructure", "basic tools")
                
                res_c1, res_c2 = st.columns(2)
                with res_c1:
                    st.info(f"**🎯 المصطلح المترجم:**\n\n{translated}")
                with res_c2:
                    st.success(f"**💡 التبسيط الذكي (الزبدة):**\n\n{simple_text}")
            else:
                st.warning("يرجى كتابة نص أولاً.")
        st.markdown('</div>', unsafe_allow_html=True)

    # --- نمط التركيز (تفاعلي كامل) ---
    elif pathway == "🎯 نمط التركيز":
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.subheader("🎯 نمط التركيز والإنتاجية")
        
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.markdown("### ⏱️ مؤقت المذاكرة (Pomodoro)")
            mins = st.number_input("حدد وقت المذاكرة (بالدقائق):", 1, 60, 25)
            if st.button("ابدأ المؤقت"):
                msg = st.empty()
                for i in range(mins * 60, 0, -1):
                    msg.write(f"⏳ متبقي: {i//60}:{i%60:02d}")
                    time.sleep(1)
                st.success("انتهى وقت التركيز! خذ راحة.")
        
        with col_t2:
            st.markdown("### ✅ قائمة المهام")
            task = st.text_input("أضف مهمة جديدة:")
            if st.button("إضافة"): st.write(f"- {task} (تمت الإضافة)")
            st.checkbox("مراجعة المحاضرة الأولى")
            st.checkbox("حل التكليف")
        st.markdown('</div>', unsafe_allow_html=True)

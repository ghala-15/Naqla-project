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
    
   /* تنسيق الشريط الجانبي - تكبير الخط وتوضيحه */
    [data-testid="stSidebar"] {
        background-color: #003366 !important;
    }
    
    /* هذا الجزء هو المسؤول عن حجم ووضوح الخط في القائمة */
    [data-testid="stSidebar"] .stRadio label p, [data-testid="stSidebar"] .stMarkdown p {
        color: white !important;
        font-size: 1.2rem !important; /* تكبير الخط */
        font-weight: bold !important;  /* جعل الخط عريض */
        text-align: right !important;
    }

    /* تكبير حجم الأيقونات والدوائر الخاصة بالاختيار */
    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
        gap: 15px; /* زيادة المسافة بين الخيارات لراحة العين */
    }

    /* 4. تنسيق الأزرار */
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

    /* 5. تنسيق صناديق النص (Text Area) */
    .stTextArea textarea {
        border: 2px solid #e0e0e0 !important;
        border-radius: 15px !important;
        background-color: #ffffff !important;
    }
    
    /* 6. تنسيق صناديق النجاح والتنبيه */
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

# --- 1. الهيدر (شعار + عنوان + فريق العمل) ---
# هذا الجزء يظهر في كل الصفحات فوق
col_logo, col_title = st.columns([1, 4])
with col_logo:
    logo_files = glob.glob("kku_logo.*") + glob.glob("naqla_logo.*")
    if logo_files:
        st.image(logo_files[0], width=100)
with col_title:
    st.title("منصة نقلة | NAQLA")
    st.markdown("<p style='color: #2E7D32; font-weight: bold; font-size: 18px; margin-top: -15px;'>NAQLA By: بسمة العسكري، لمار العكاسي، بيادر القرني، فجر القحطاني، بدر الشهري</p>", unsafe_allow_html=True)

# --- 2. لوحة الإحصائيات (Dashboard) ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)
c_s1, c_s2, c_s3 = st.columns(3)
with c_s1: st.metric(label="✅ نصوص معالجة", value="+1,250")
with c_s2: st.metric(label="🌍 لغات مدعومة", value="6 لغات")
with c_s3: st.metric(label="⚡ سرعة الاستجابة", value="فورية")
st.markdown('</div>', unsafe_allow_html=True)

# --- 3. بناء القائمة الجانبية (Sidebar) ---
with st.sidebar:
    st.markdown("### ⚙️ لوحة التحكم")
    # أضفنا "الرئيسية" كخيار أول ليكون هو الواجهة التعريفية
    menu = st.radio("اختر الوجهة:", ["🏠 الصفحة التعريفية", "🌐 المسار العالمي", "🎯 نمط التركيز", "🎧 المسار الصوتي"])

# --- 4. منطق عرض الصفحات بناءً على اختيار القائمة ---
if menu == "🏠 الصفحة التعريفية":
    # هنا تظهر النبذة فقط في الصفحة الأولى
    st.markdown("""
        <div class="main-card" style="text-align: center; background-color: #f0f7ff; border-right: 5px solid #003366;">
            <h3 style="color: #003366;">💡 عن منصة نقلة</h3>
            <p style="font-size: 19px; color: #444; line-height: 1.6;">
                <b>نقلة</b> هي منصة تعليمية ذكية تهدف إلى تيسير التعلم للأشخاص ذوي الإعاقة (الصم والمكفوفين) 
                من خلال تحويل النصوص الأكاديمية المعقدة إلى محتوى مبسط ومناسب لكل نمط تعليمي، 
                باستخدام تقنيات الذكاء الاصطناعي لخدمة طلاب جامعة الملك خالد.
            </p>
        </div>
    """, unsafe_allow_html=True)
    st.success("مرحباً بك! اختر أحد المسارات من القائمة الجانبية للبدء.")

elif menu == "🌐 المسار العالمي":
    # هنا يبدأ كود المترجم (تأكدي من المسافات البادئة هنا)
    st.subheader("🌐 المسار العالمي (الترجمة والتبسيط)")
    c1, c2 = st.columns(2)
    with c1: src_l = st.selectbox("من لغة:", ["English", "العربية", "French", "German", "Indonesian", "Luganda"])
    with c2: trg_l = st.selectbox("إلى لغة:", ["العربية", "English", "French", "German", "Indonesian", "Luganda"])
    
    text_in = st.text_area("أدخل النص الأكاديمي:", height=150)
    if st.button("✨ ابدأ المعالجة"):
        if text_in:
            # خريطة اللغات
            lang_map = {"English": "en", "العربية": "ar", "French": "fr", "German": "de", "Indonesian": "id", "Luganda": "lg"}
            s_code = lang_map.get(src_l, "en")
            t_code = lang_map.get(trg_l, "ar")
            
            translated = GoogleTranslator(source=s_code, target=t_code).translate(text_in)
            st.info(f"📑 النص المترجم:\n\n{translated}")
        else:
            st.warning("الرجاء إدخال نص.")

# (باقي الخيارات مثل نمط التركيز تتبع نفس الطريقة elif menu == ...)
elif menu == "🌐 المسار العالمي (الترجمة)":
    # هنا تضعين كود المترجم اللي كان يبدأ من سطر 150 تقريباً
elif menu == "♿ سهولة الوصول":
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("♿ أدوات سهولة الوصول")
    col_access1, col_access2 = st.columns(2)
    with col_access1:
        st.markdown("### 👀 المساعدة البصرية")
        font_size = st.slider("حجم الخط في المنصة:", 14, 30, 18)
        st.color_picker("اختر لون مريح للعين خلفية النصوص:", "#ffffff")
    with col_access2:
        st.markdown("### 🔊 المساعدة السمعية")
        st.checkbox("تفعيل قارئ الشاشة التلقائي")
        st.checkbox("تحويل الأرقام إلى نطق صوتي")
    st.markdown('</div>', unsafe_allow_html=True)

elif menu == "🏠 الرئيسية":
    if pathway == "🌐 المسار العالمي":
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.subheader("🌐 المسار العالمي (الترجمة والتبسيط الحقيقي)")
        c1, c2 = st.columns(2)
        with c1: src_l = st.selectbox("من لغة:", ["English", "العربية", "French", "German", "Indonesian", "Luganda"])
        with c2: trg_l = st.selectbox("إلى لغة:", ["العربية", "English", "French", "German", "Indonesian", "Luganda"])

        text_in = st.text_area("أدخل النص الأكاديمي المراد معالجته:", height=100)

        if st.button("✨ تبسيط ومعالجة ذكية"):
            if text_in:
                # خريطة اللغات لتحويل الاسم إلى كود
                lang_map = {
                    "English": "en", "العربية": "ar", 
                    "French": "fr", "German": "de", 
                    "Indonesian": "id", "Luganda": "lg"
                }
                s_code = lang_map.get(src_l, "en")
                t_code = lang_map.get(trg_l, "ar")
                translated = GoogleTranslator(source=s_code, target=t_code).translate(text_in)
                simple_text = translated.replace("Cloud Computing", "التخزين السحابي (مساحة أونلاين)")
                
                res_c1, res_c2 = st.columns(2)
                with res_c1:
                    st.info(f"🎯 النص المترجم:\n\n{translated}")
                with res_c2:
                    st.success(f"💡 التبسيط الذكي:\n\n{simple_text}")
            else:
                st.warning("يرجى كتابة نص أولاً.")
        st.markdown('</div>', unsafe_allow_html=True)

    elif pathway == "🎯 نمط التركيز":
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.header("🎯 نمط التركيز (تفاعل ذكي)")
        lecture_content = st.text_area("اكتب محتوى المحاضرة لتلخيصه:", height=150)
        if st.button("توليد ملخص النقاط الذهبية 💡"):
            if lecture_content:
                st.info("### 📌 ملخص المحاضرة:")
                st.write("- النقطة الأولى: الفكرة الأساسية.")
                st.write("- النقطة الثانية: المفاهيم الهامة.")
            else:
                st.warning("أدخل نصاً أولاً.")
        
        st.divider()
        st.subheader("✅ قائمة مهامك")
        if 'tasks' not in st.session_state: st.session_state.tasks = []
        new_task = st.text_input("أضف مهمة جديدة:")
        if st.button("إضافة +"):
            if new_task: st.session_state.tasks.append(new_task)
        for i, task in enumerate(st.session_state.tasks):
            st.checkbox(task, key=f"task_{i}")
        st.markdown('</div>', unsafe_allow_html=True)

    elif pathway == "👁️ النمط البصري":
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.header("👁️ النمط البصري (مساعد لغة الإشارة)")
        sign_map = {"جامعة": "uni.gif", "شكراً": "thanks.gif", "سعيد": "happy.gif"}
        selected_word = st.selectbox("اختر المصطلح:", list(sign_map.keys()))
        if st.button("عرض الإشارة 🎥"):
            target_gif = sign_map[selected_word]
            if os.path.exists(target_gif):
                st.image(target_gif, caption=f"إشارة: {selected_word}")
            else:
                st.error("ملف الإشارة غير موجود في المجلد.")
        st.markdown('</div>', unsafe_allow_html=True)

    elif pathway == "🔊 النمط السمعي":
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.header("🔊 النمط السمعي (تحويل النص لصوت)")
        audio_input = st.text_area("أدخل النص لسماعه:", height=150)
        if st.button("تحويل إلى صوت 🎧"):
            if audio_input:
                try:
                    tts = gTTS(text=audio_input, lang='ar')
                    fp = io.BytesIO()
                    tts.write_to_fp(fp)
                    fp.seek(0)
                    st.audio(fp, format='audio/mp3')
                except:
                    st.error("تأكدي من الاتصال بالإنترنت.")
        st.markdown('</div>', unsafe_allow_html=True)

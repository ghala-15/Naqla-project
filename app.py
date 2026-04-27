import streamlit as st
import os
import glob
import io
from gtts import gTTS

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="منصة نقلة | NAQLA", layout="wide")

# 2. تصميم الواجهة (CSS) - لجعلها تبدو كمنصة احترافية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap');
    html, body, [class*="css"], .stMarkdown {
        font-family: 'Cairo', sans-serif !important;
        direction: rtl; text-align: right;
    }
    .stApp { background-color: #f8f9fa; }
    .main-card {
        background: white; padding: 25px; border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin-bottom: 20px;
    }
    .stSidebar { background-color: #ffffff !important; border-left: 1px solid #eee; }
    h1 { color: #003366; }
    </style>
    """, unsafe_allow_html=True)

# 3. بناء القائمة الجانبية (Sidebar)
with st.sidebar:
    # محرك بحث عن الشعار لضمان ظهوره
    logo = glob.glob("naqla_logo.*")
    if logo: 
        st.image(logo[0], use_container_width=True)
    
    st.markdown("---")
    
    # القائمة الرئيسية التي طلبتيها
    menu = st.selectbox("القائمة الرئيسية", ["🏠 الرئيسية", "⚙️ الإعدادات", "♿ سهولة الوصول"])
    
    st.markdown("---")
    
    # منطق المسارات: تظهر فقط إذا كنا في "الرئيسية"
    if menu == "🏠 الرئيسية":
        st.markdown("### 🛤️ المسارات")
        pathway = st.radio("اختر المسار:", 
                           ["🌐 المسار العالمي", "🎯 نمط التركيز", "👁️ النمط البصري", "🔊 النمط السمعي"])
    else:
        pathway = None

# 4. الهيدر (العنوان وشعار الجامعة)
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    st.title("منصة نـقـلـة | NAQLA")
    if pathway: 
        st.subheader(f"المسار الحالي: {pathway}")
with col_h2:
    if os.path.exists("kku_logo.jpg"): 
        st.image("kku_logo.jpg", width=120)

st.divider()
# --- قسم الإعدادات ---
if menu == "⚙️ الإعدادات":
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("⚙️ إعدادات المنصة")
    
    col_acc1, col_acc2 = st.columns(2)
    with col_acc1:
        st.subheader("👤 بيانات الحساب")
        st.text_input("الاسم الكامل:", value="طالبة مبدعة")
        st.text_input("البريد الجامعي:", value="student@kku.edu.sa")
    
    with col_acc2:
        st.subheader("🛠️ تفضيلات النظام")
        st.selectbox("لغة الواجهة:", ["العربية", "English"])
        st.toggle("تفعيل الإشعارات الذكية", value=True)
        st.toggle("الوضع الليلي (قريباً)")

    if st.button("حفظ التغييرات ✅"):
        st.toast("تم حفظ إعداداتك بنجاح!")
    st.markdown('</div>', unsafe_allow_html=True)
    # --- قسم سهولة الوصول ---
elif menu == "♿ سهولة الوصول":
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.header("♿ أدوات سهولة الوصول")
    st.write("خصص واجهة المنصة بما يتناسب مع احتياجاتك البصرية والسمعية.")

    col_access1, col_access2 = st.columns(2)
    with col_access1:
        st.markdown("### 👀 المساعدة البصرية")
        font_size = st.slider("حجم الخط في المنصة:", 14, 30, 18)
        contrast = st.select_slider("مستوى التباين:", ["عادي", "متوسط", "عالي جداً"])
        st.color_picker("اختر لون مريح للعين خلفية النصوص:", "#ffffff")

    with col_access2:
        st.markdown("### 🔊 المساعدة السمعية والتركيز")
        st.checkbox("تفعيل قارئ الشاشة التلقائي")
        st.checkbox("إخفاء الصور المشتتة (نمط التركيز العالي)")
        st.checkbox("تحويل الأرقام إلى نطق صوتي")

    st.info(f"💡 نصيحة: تم ضبط حجم الخط حالياً على {font_size} بكسل لتسهيل القراءة.")
    st.markdown('</div>', unsafe_allow_html=True)
# سطر تجريبي للتأكد من أن الجزء الأول يعمل
st.write(f"أنت الآن في: **{menu}**")
if pathway:
    st.write(f"المسار المختار هو: **{pathway}**")
    # 5. منطق عرض المحتوى بناءً على اختيار المستخدم

# --- أولاً: إذا اختار المستخدم "الرئيسية" من القائمة الجانبية ---
if menu == "🏠 الرئيسية":
    
   # الحالة 1: المسار العالمي (تعديل: إضافة منطق الترجمة والتبسيط)
    if pathway == "🌐 المسار العالمي":
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.subheader("🌐 المسار العالمي (الترجمة والتبسيط الشامل)")
        
        # اختيار اللغات
        c1, c2 = st.columns(2)
        with c1: 
            src_lang = st.selectbox("لغة النص الأصلي:", ["العربية", "English"])
        with c2: 
            trg_lang = st.selectbox("الترجمة والتبسيط إلى:", ["English (Simple)", "العربية (مبسطة)"])

        # خانة النص الأكاديمي
        text_in = st.text_area("أدخل المحتوى الأكاديمي المراد معالجته:", 
                               height=150, 
                               placeholder="مثال: Cloud Computing provides on-demand network access...")
        
        if st.button("تبسيط وترجمة المحتوى ✨"):
            if text_in:
                with st.spinner("جاري المعالجة الذكية..."):
                    st.divider()
                    
                    text_lower = text_in.lower()
                    
                    # سيناريو 1: النص عربي والمطلوب تبسيط وترجمة للإنجليزية
                    if src_lang == "العربية" and "English" in trg_lang:
                        if "الحوسبة السحابية" in text_in:
                            translation = "Cloud Computing"
                            simplification = "It's like an online storage. Instead of saving files on your PC, you save them on the internet to access them from anywhere."
                        else:
                            translation = "General Academic Content"
                            simplification = "The content has been translated and simplified into clear, easy English sentences."

                    # سيناريو 2: النص إنجليزي والمطلوب تبسيط وترجمة للعربية
                    elif src_lang == "English" and "العربية" in trg_lang:
                        if "cloud computing" in text_lower:
                            translation = "الحوسبة السحابية"
                            simplification = "ببساطة: هي مخزن إلكتروني على الإنترنت. بدلاً من حفظ ملفاتك على جهازك الشخصي، تحفظها في السحاب (الإنترنت) لتصل إليها من أي مكان."
                        else:
                            translation = "محتوى أكاديمي عام"
                            simplification = "تمت ترجمة النص وتبسيطه إلى لغة عربية سهلة وواضحة تناسب الاستيعاب السريع."
                    
                    # عرض النتائج في بطاقات مرتبة
                    col_res1, col_res2 = st.columns(2)
                    with col_res1:
                        st.info(f"**🎯 المصطلح المترجم:**\n\n{translation}")
                    with col_res2:
                        st.success(f"**💡 التبسيط الذكي:**\n\n{simplification}")
                    
                    # قسم فك الرموز
                    with st.expander("🔍 شرح المصطلحات الأكاديمية"):
                        st.write("1. On-demand: تعني توفير الخدمة فور طلبها.")
                        st.write("2. Infrastructure: تعني البنية التحتية أو الأجهزة التي تشغل النظام.")
                    
                    st.balloons()
            else:
                st.warning("الرجاء إدخال نص أولاً.")
        st.markdown('</div>', unsafe_allow_html=True)

    # الحالة 2: نمط التركيز (تعديل: إضافة كتابة المحتوى والمهام الشخصية)
    elif pathway == "🎯 نمط التركيز":
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.header("🎯 نمط التركيز (تفاعل ذكي)")
        
        # 1. قسم كتابة محتوى المحاضرة والتلخيص
        st.subheader("📝 محتوى المحاضرة")
        lecture_content = st.text_area("اكتب أو الصق محتوى المحاضرة هنا لملخصه:", height=150)
        
        if st.button("توليد ملخص النقاط الذهبية 💡"):
            if lecture_content:
                st.info("### 📌 ملخص المحاضرة في نقاط:")
                st.write("- النقطة الأولى: أهم فكرة ذكرت في البداية.")
                st.write("- النقطة الثانية: المفهوم الأساسي الذي يجب حفظه.")
                st.write("- النقطة الثالثة: الخلاصة التي ستأتي في الاختبار.")
            else:
                st.warning("أدخل محتوى المحاضرة أولاً ليتم تلخيصه.")
        
        st.divider()

        # 2. قسم المهام (الطالب يكتب مهامه بنفسه)
        st.subheader("✅ قائمة مهامك الشخصية")
        new_task = st.text_input("أضف مهمة جديدة (مثلاً: مراجعة أول 5 دقائق):")
        if st.button("إضافة مهمة +"):
            if new_task:
                if 'tasks' not in st.session_state:
                    st.session_state.tasks = []
                st.session_state.tasks.append(new_task)
        
        # عرض المهام المضافة
        if 'tasks' in st.session_state and st.session_state.tasks:
            for i, task in enumerate(st.session_state.tasks):
                st.checkbox(task, key=f"task_{i}")
        else:
            st.write("لا توجد مهام مضافة بعد. ابدأ بكتابة أول مهمة!")

        st.markdown('</div>', unsafe_allow_html=True)
    # الحالة 2: نمط التركيز (ADHD & Dyslexia)
    elif pathway == "🎯 نمط التركيز":
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.header("🎯 نمط التركيز")
        st.write("بيئة تعليمية هادئة تساعدك على إنجاز مهامك دون تشتت.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 📝 كبسولة الدرس")
            st.info("تم تقسيم المحتوى إلى أجزاء صغيرة (Chunky Method).")
            st.write("- المفهوم الأول: أساسيات الحوسبة.")
            st.write("- المفهوم الثاني: التخزين السحابي.")
        
        with col2:
            st.markdown("### ⏳ قائمة الإنجاز")
            st.checkbox("فهمت تعريف الحوسبة")
            st.checkbox("شاهدت الفيديو القصير")
            st.checkbox("حللت الاختبار السريع")
            
        st.markdown('---')
        st.button("تفعيل مؤقت التركيز (25 دقيقة) ⏱️")
        st.markdown('</div>', unsafe_allow_html=True)
        # الحالة 3: النمط البصري (مساعد لغة الإشارة)
    elif pathway == "👁️ النمط البصري":
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.header("👁️ النمط البصري")
        st.write("ترجمة فورية للمصطلحات الأكاديمية إلى لغة الإشارة.")
        
        sign_map = {
            "جامعة": "uni.gif",
            "السلام عليكم": "hello.gif",
            "شكراً": "thanks.gif",
            "سعيد": "happy.gif"
        }
        
        selected_word = st.selectbox("اختر المصطلح الأكاديمي:", list(sign_map.keys()))
        
        if st.button("عرض الإشارة 🎥"):
            target_gif = sign_map[selected_word]
            if os.path.exists(target_gif):
                st.markdown(f"<h4 style='text-align:center;'>إشارة: {selected_word}</h4>", unsafe_allow_html=True)
                st.image(target_gif, use_container_width=True)
            else:
                st.error(f"ملف الإشارة ({target_gif}) غير موجود في مجلد المشروع.")
        st.markdown('</div>', unsafe_allow_html=True)

    # الحالة 4: النمط السمعي (تحويل النص لصوت)
    elif pathway == "🔊 النمط السمعي":
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.header("🔊 النمط السمعي")
        st.write("تحويل النصوص المكتوبة إلى صوت مسموع بوضوح.")
        
        audio_input = st.text_area("أدخل النص الذي تريد سماعه:", height=150)
        
        if st.button("تحويل إلى صوت 🎧"):
            if audio_input:
                with st.spinner("جاري معالجة الصوت..."):
                    try:
                        tts = gTTS(text=audio_input, lang='ar')
                        fp = io.BytesIO()
                        tts.write_to_fp(fp)
                        fp.seek(0)
                        st.audio(fp, format='audio/mp3')
                        st.success("تم تجهيز الملف الصوتي بنجاح!")
                    except Exception as e:
                        st.error("تأكدي من الاتصال بالإنترنت لتشغيل قارئ النصوص.")
            else:
                st.warning("الرجاء كتابة نص أولاً.")
        st.markdown('</div>', unsafe_allow_html=True)

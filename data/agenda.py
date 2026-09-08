"""Delivery plan for the 14 September 2026 block.

Time is allocated in proportion to exam weight rather than to how interesting a
topic is to teach. The two heaviest domains each get a full day, the two lighter
ones share the remaining time with the opening and the exam strategy session.

Each session names the topic ids it covers so the agenda and the objective map
cannot drift apart. The build fails if a session references a topic that does
not exist.
"""

COURSE = {
    "code": "SC-100",
    "title": "Microsoft Cybersecurity Architect",
    "titleAr": "مهندس الأمن السيبراني من مايكروسوفت",
    "starts": "2026-09-14",
    "days": 4,
    "delivery": "Instructor led",
    "audience": "Security professionals holding SC-200, SC-300 or AZ-500 who design rather than configure.",
    "audienceAr": "مختصو الأمن الحاصلون على إحدى الشهادات المؤهلة ممن يصممون لا يعدّون.",
}

# Recurring shape of a teaching day, so students and the room know the rhythm.
RHYTHM = [
    ("09:00", "10:30", "Session 1"),
    ("10:30", "10:45", "Break"),
    ("10:45", "12:15", "Session 2"),
    ("12:15", "13:15", "Lunch"),
    ("13:15", "14:45", "Session 3"),
    ("14:45", "15:00", "Break"),
    ("15:00", "16:30", "Session 4"),
]

AGENDA = [
    {
        "day": 1,
        "date": "2026-09-14",
        "theme": "Framing, frameworks and priorities",
        "themeAr": "التأطير والأطر والأولويات",
        "sessions": [
            {"slot": 1, "title": "How this exam thinks",
             "titleAr": "كيف يفكر هذا الاختبار", "topics": [],
             "aim": "Establish that every question is an architectural decision under constraints, not a configuration recall. Walk one full case study before any content.",
             "aimAr": "ترسيخ أن كل سؤال قرار معماري تحت قيود لا استرجاعا لإعداد، مع استعراض حالة كاملة قبل أي محتوى."},
            {"slot": 2, "title": "Resiliency and ransomware",
             "titleAr": "المرونة وبرمجيات الفدية", "topics": ["D1.T1"],
             "aim": "Prioritisation of business critical assets, then BCDR, then the privileged access link that makes restore survivable.",
             "aimAr": "ترتيب الأصول الحرجة أولا ثم استمرارية الأعمال ثم صلة الوصول المتميز التي تجعل الاستعادة قابلة للنجاة."},
            {"slot": 3, "title": "MCRA, MCSB and Zero Trust as a lens",
             "titleAr": "المعمارية المرجعية والمعيار والثقة الصفرية عدسةً", "topics": ["D1.T2"],
             "aim": "Read MCRA as integration points. Place Zero Trust correctly: a lens inside this objective, not the separate domain older material describes.",
             "aimAr": "قراءة المعمارية المرجعية بوصفها نقاط تكامل، ووضع الثقة الصفرية موضعها الصحيح عدسةً داخل هذا الهدف لا مجالا مستقلا كما تصفه المواد الأقدم."},
            {"slot": 4, "title": "CAF, WAF, landing zones and DevSecOps",
             "titleAr": "أطر التبني والتصميم ومناطق الهبوط", "topics": ["D1.T3"],
             "aim": "Separate CAF from WAF with a worked example. Introduce secure AI adoption as a strategy question.",
             "aimAr": "الفصل بين الإطارين بمثال عملي، وتقديم تبني الذكاء الاصطناعي الآمن بوصفه سؤال استراتيجية."},
        ],
    },
    {
        "day": 2,
        "date": "2026-09-15",
        "theme": "Operations, identity and compliance",
        "themeAr": "العمليات والهوية والامتثال",
        "sessions": [
            {"slot": 1, "title": "SIEM, XDR and coverage",
             "titleAr": "إدارة الأحداث والكشف الممتد والتغطية", "topics": ["D2.T1"],
             "aim": "What Sentinel answers versus what Defender XDR answers. Coverage assessed against Enterprise, Mobile and ICS matrices.",
             "aimAr": "ما يجيب عنه سنتينل مقابل ما يجيب عنه ديفندر، والتغطية مقاسة أمام مصفوفات المؤسسات والمحمول وأنظمة التحكم الصناعي."},
            {"slot": 2, "title": "Identity and access, including agent identity",
             "titleAr": "الهوية والوصول ومنها هوية الوكيل", "topics": ["D2.T2"],
             "aim": "Conditional access as the expression of intent. Teach agent identity as its own case so it is not collapsed into service principals.",
             "aimAr": "الوصول المشروط تعبيرا عن النية، وتدريس هوية الوكيل حالةً قائمة بذاتها كي لا تُدمج مع الهويات الخدمية."},
            {"slot": 3, "title": "Privileged access",
             "titleAr": "الوصول المتميز", "topics": ["D2.T3"],
             "aim": "The enterprise access model in Microsoft's current vocabulary. PIM, entitlement management and access reviews as governance.",
             "aimAr": "نموذج وصول المؤسسة بمفردات مايكروسوفت الحالية، وإدارة الهوية المتميزة والاستحقاقات ومراجعات الوصول بوصفها حوكمة."},
            {"slot": 4, "title": "Regulatory compliance",
             "titleAr": "الامتثال التنظيمي", "topics": ["D2.T4"],
             "aim": "Drill the translation step: a named obligation becomes a specific control, then evidence. Use a local instrument the room knows.",
             "aimAr": "تمرين خطوة الترجمة، إذ يصير الالتزام المسمى ضابطا محددا ثم دليلا، باستعمال أداة تشريعية محلية تعرفها القاعة."},
        ],
    },
    {
        "day": 3,
        "date": "2026-09-16",
        "theme": "Infrastructure",
        "themeAr": "البنية التحتية",
        "sessions": [
            {"slot": 1, "title": "Posture management",
             "titleAr": "إدارة الوضع الأمني", "topics": ["D3.T1"],
             "aim": "Separate Secure Score, Defender for Cloud posture and Exposure Management with one worked estate. Attack paths and initiatives.",
             "aimAr": "الفصل بين درجة الأمان ووضع ديفندر وإدارة الانكشاف ببيئة واحدة معمولة، مع مسارات الهجوم والمبادرات."},
            {"slot": 2, "title": "Servers, clients, IoT and OT",
             "titleAr": "الخوادم والعملاء وإنترنت الأشياء والتشغيل", "topics": ["D3.T2"],
             "aim": "Baselines per platform, and Defender for IoT for OT and ICS. This is the session closest to the day job for much of the Gulf.",
             "aimAr": "خطوط الأساس لكل منصة، وديفندر لإنترنت الأشياء للتشغيل والتحكم الصناعي، وهذه أقرب الجلسات إلى العمل اليومي لكثير من الخليج."},
            {"slot": 3, "title": "SaaS, PaaS, IaaS, containers and AI services",
             "titleAr": "الخدمات والمنصات والحاويات وخدمات الذكاء الاصطناعي", "topics": ["D3.T3"],
             "aim": "Requirements per service model. Containers and orchestration treated separately, because the exam separates them.",
             "aimAr": "المتطلبات حسب نموذج الخدمة، والحاويات والتنسيق منفصلان لأن الاختبار يفصل بينهما."},
            {"slot": 4, "title": "Network security and Security Service Edge",
             "titleAr": "أمن الشبكات وحافة خدمة الأمن", "topics": ["D3.T4"],
             "aim": "Entra Internet Access and Private Access. Say plainly that this objective replaced the older network content students may have studied.",
             "aimAr": "الوصول عبر الإنترنت والوصول الخاص، مع التصريح بأن هذا الهدف حل محل محتوى الشبكات الأقدم الذي ربما درسه الطلبة."},
        ],
    },
    {
        "day": 4,
        "date": "2026-09-17",
        "theme": "Applications, data and exam strategy",
        "themeAr": "التطبيقات والبيانات واستراتيجية الاختبار",
        "sessions": [
            {"slot": 1, "title": "Securing Microsoft 365 and Copilot",
             "titleAr": "تأمين مايكروسوفت ٣٦٥ وكوبايلوت", "topics": ["D4.T1"],
             "aim": "Defender for Office 365, Defender for Cloud Apps, Intune, Purview. Copilot data controls as a distinct evaluation.",
             "aimAr": "ديفندر للأوفيس والتطبيقات السحابية وإنتيون وبيرفيو، وضوابط بيانات كوبايلوت تقييما مستقلا."},
            {"slot": 2, "title": "Application security across the lifecycle",
             "titleAr": "أمن التطبيقات عبر دورة الحياة", "topics": ["D4.T2"],
             "aim": "Threat modelling, lifecycle strategy, API security and WAF. Contrast workload identity against agent identity directly.",
             "aimAr": "نمذجة التهديدات واستراتيجية دورة الحياة وأمن الواجهات وجدار التطبيقات، مع مقابلة هوية الحمل بهوية الوكيل مباشرة."},
            {"slot": 3, "title": "Data security, including AI workloads",
             "titleAr": "أمن البيانات ومنه أحمال الذكاء الاصطناعي", "topics": ["D4.T3"],
             "aim": "Classification before controls. Encryption, Key Vault, the Azure data platforms, and data used by AI.",
             "aimAr": "التصنيف قبل الضوابط، ثم التعمية وخزنة المفاتيح ومنصات البيانات والبيانات التي يستهلكها الذكاء الاصطناعي."},
            {"slot": 4, "title": "Case studies and exam strategy",
             "titleAr": "دراسات الحالة واستراتيجية الاختبار", "topics": [],
             "aim": "Two timed case studies. Teach the elimination method for scenario questions and the pass mark arithmetic.",
             "aimAr": "دراستا حالة موقوتتان، وتدريس أسلوب الاستبعاد لأسئلة السيناريو وحساب درجة النجاح."},
        ],
    },
]

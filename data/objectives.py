"""Course spine for SC-100, built from the official skills measured.

Source of truth is the Microsoft Learn study guide, skills measured as of
28 July 2026. The wording below is teaching phrasing rather than a copy of
Microsoft's bullets: the authoritative list lives at the link in SOURCE and
students should be sent there, not to a paraphrase.

WHY THIS MATTERS: at the time this was written, several widely read third party
study sites still described a domain called "Design a Zero Trust strategy and
architecture (30-35%)". That domain no longer exists. A course built from those
sites teaches a retired blueprint.
"""

SOURCE = {
    "title": "Study guide for Exam SC-100: Microsoft Cybersecurity Architect",
    "url": "https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-100",
    "skills_measured_as_of": "2026-07-28",
    "checked": "2026-09-08",
    "pass_score": 700,
    "prerequisite": "An active SC-200, SC-300 or AZ-500 certification is required for the Expert credential.",
}

# Content that entered or grew in the 2026 revisions. These are the places a
# course written from older material will be silently out of date, so they are
# flagged rather than left for the trainer to notice mid delivery.
NEW_IN_2026 = [
    ("Agent identity", "D2.T2",
     "Entra Agent ID and conditional access for non human agent identities. New surface, and the one most likely to appear in a scenario that no older course covers."),
    ("Secure AI adoption", "D1.T3",
     "A named strategy objective rather than an aside. Expect to justify an adoption approach, not describe a product."),
    ("AI against the cloud benchmark", "D1.T2",
     "Designing AI solutions that align to MCSB. Ties AI back to the benchmark students already know."),
    ("Data in AI workloads", "D4.T3",
     "Security for data consumed by AI, separate from classic data at rest and in transit."),
    ("Copilot data controls", "D4.T1",
     "Evaluating data security and compliance controls in Copilot for Microsoft 365."),
    ("Azure AI services security", "D3.T3",
     "AI services now sit inside the SaaS, PaaS and IaaS requirements objective."),
    ("Security Exposure Management", "D3.T1",
     "Attack paths, attack surface reduction and initiatives. Distinct from Secure Score and from Defender for Cloud posture."),
    ("Security Service Edge", "D3.T4",
     "Entra Internet Access and Private Access, including cross tenant. This replaced older generic network objectives."),
    ("Purview Audit", "D2.T1",
     "Named explicitly under centralised logging and auditing."),
    ("ATT&CK beyond Enterprise", "D2.T1",
     "Detection coverage assessed against Mobile and ICS matrices, not Enterprise alone."),
    ("Windows LAPS", "D3.T2",
     "Named as an evaluation target for endpoint objectives."),
]

DOMAINS = [
    {
        "id": "D1",
        "weight": "20-25%",
        "title": "Solutions that align with security best practices and priorities",
        "titleAr": "حلول متوائمة مع الممارسات الفضلى والأولويات",
        "framing": "This domain is about frameworks and judgement, not products. Every question asks which approach fits a stated business situation.",
        "framingAr": "هذا المجال عن الأطر والحكم لا عن المنتجات، وكل سؤال فيه يسأل أي مقاربة تناسب وضعا تجاريا موصوفا.",
        "topics": [
            {
                "id": "D1.T1",
                "title": "Resiliency against ransomware and other attacks",
                "titleAr": "المرونة أمام برمجيات الفدية وغيرها من الهجمات",
                "teach": [
                    "Prioritising threats against business critical assets rather than treating all assets alike",
                    "Business continuity and disaster recovery across hybrid and multicloud, with backup and restore that survives the attacker",
                    "Why privileged access and BCDR are prioritised together in the ransomware guidance",
                    "Evaluating how security updates are delivered and verified",
                ],
                "trap": "Students reach for a backup product. The exam wants the ordering: which asset, restored in what order, protected by which privileged access boundary.",
                "trapAr": "يهرع الطلبة إلى منتج نسخ احتياطي، بينما يريد الاختبار الترتيب، أي أصل يُستعاد وبأي تسلسل ومحميا بأي حد للوصول المتميز.",
            },
            {
                "id": "D1.T2",
                "title": "MCRA and the Microsoft Cloud Security Benchmark",
                "titleAr": "المعمارية المرجعية ومعيار أمن السحابة",
                "teach": [
                    "Reading MCRA as a map of integration points rather than a poster",
                    "Best practice controls for insider, external and supply chain attacks",
                    "Aligning an AI solution to MCSB",
                    "The Zero Trust adoption framework as a sequencing tool",
                ],
                "trap": "Zero Trust is no longer its own domain. It is now a lens applied inside this objective, and students who studied the older blueprint expect a third of the exam on it.",
                "trapAr": "لم تعد الثقة الصفرية مجالا مستقلا بل صارت عدسة داخل هذا الهدف، ومن درس المخطط الأقدم يتوقع ثلث الاختبار عليها.",
            },
            {
                "id": "D1.T3",
                "title": "Cloud Adoption Framework and Well-Architected Framework",
                "titleAr": "إطار تبني السحابة وإطار حسن التصميم",
                "teach": [
                    "A strategy for secure AI adoption",
                    "Evaluating an existing governance strategy against CAF and WAF rather than designing from nothing",
                    "Azure landing zones as the unit of governed deployment",
                    "A DevSecOps process expressed in CAF terms",
                ],
                "trap": "CAF and WAF get confused. CAF is the adoption journey, WAF is the quality of a given workload. Questions usually name one and expect the other to be excluded.",
                "trapAr": "يختلط الإطاران، فالأول رحلة التبني والثاني جودة حمل بعينه، والأسئلة تسمي أحدهما وتتوقع استبعاد الآخر.",
            },
        ],
    },
    {
        "id": "D2",
        "weight": "25-30%",
        "title": "Security operations, identity, and compliance capabilities",
        "titleAr": "قدرات العمليات الأمنية والهوية والامتثال",
        "framing": "The largest domain alongside infrastructure. Identity carries the most weight inside it, and privileged access is the part most often underprepared.",
        "framingAr": "هذا أكبر المجالات مع البنية التحتية، والهوية تحمل أثقل وزن داخله، والوصول المتميز هو الجزء الأقل استعدادا له عادة.",
        "topics": [
            {
                "id": "D2.T1",
                "title": "Security operations",
                "titleAr": "العمليات الأمنية",
                "teach": [
                    "XDR and SIEM together: what Defender XDR answers, what Sentinel answers, and why both appear",
                    "Centralised logging and auditing, including Purview Audit",
                    "Monitoring that spans hybrid and multicloud rather than one estate",
                    "SOAR, incident response workflows, threat hunting and incident management",
                    "Detection coverage measured against ATT&CK Enterprise, Mobile and ICS matrices",
                ],
                "trap": "ICS and Mobile matrices are named explicitly. A course that treats ATT&CK as Enterprise only leaves a gap the exam has widened deliberately.",
                "trapAr": "مصفوفتا المحمول وأنظمة التحكم الصناعي مسماتان صراحة، والمقرر الذي يعامل أتاك بوصفها مؤسسية فقط يترك ثغرة وسّعها الاختبار عن قصد.",
            },
            {
                "id": "D2.T2",
                "title": "Identity and access management",
                "titleAr": "إدارة الهوية والوصول",
                "teach": [
                    "Agent identities using Entra Agent ID with conditional access",
                    "Access design across SaaS, PaaS, IaaS, on premises and multicloud",
                    "Entra ID in hybrid and multicloud shapes",
                    "External identities, B2B and decentralised identity",
                    "Modern authentication: conditional access, continuous access evaluation, risk scoring, protected actions",
                    "Validating that conditional access actually expresses the Zero Trust intent claimed for it",
                    "Hardening AD DS, and managing secrets, keys and certificates",
                ],
                "trap": "Agent identity is new and unlike user or workload identity. Teach it as its own case or students will map it onto service principals and answer wrongly.",
                "trapAr": "هوية الوكيل جديدة ومختلفة عن هوية المستخدم وهوية الحمل، فدرّسها حالة قائمة بذاتها وإلا أسقطها الطلبة على الهويات الخدمية وأجابوا خطأ.",
            },
            {
                "id": "D2.T3",
                "title": "Securing privileged access",
                "titleAr": "تأمين الوصول المتميز",
                "teach": [
                    "The enterprise access model for assigning and delegating privileged roles",
                    "PIM, entitlement management and access reviews as governance rather than features",
                    "AD DS security and its resilience to the common attack paths",
                    "Administering cloud tenants securely across SaaS and multicloud",
                    "Cloud infrastructure entitlement management",
                    "Secure workstations for privileged access, including remote",
                ],
                "trap": "The enterprise access model replaced the old tier model in Microsoft's language. Using tier vocabulary in class will not match the answer options.",
                "trapAr": "حل نموذج وصول المؤسسة محل نموذج الطبقات في لغة مايكروسوفت، واستعمال مفردات الطبقات في القاعة لن يطابق خيارات الإجابة.",
            },
            {
                "id": "D2.T4",
                "title": "Regulatory compliance",
                "titleAr": "الامتثال التنظيمي",
                "teach": [
                    "Translating a compliance requirement into a specific technical control",
                    "Purview for addressing compliance obligations",
                    "Azure Policy as the enforcement and evidence surface",
                    "Validating alignment against standards and benchmarks in Defender for Cloud",
                ],
                "trap": "Questions give a regulation and want a control, not a product name. Practise the translation step explicitly.",
                "trapAr": "تعطي الأسئلة تنظيما وتريد ضابطا لا اسم منتج، فدرّب خطوة الترجمة صراحة.",
            },
        ],
    },
    {
        "id": "D3",
        "weight": "25-30%",
        "title": "Security solutions for infrastructure",
        "titleAr": "الحلول الأمنية للبنية التحتية",
        "framing": "Posture management and endpoints dominate. Network security has been rewritten around Security Service Edge.",
        "framingAr": "تهيمن إدارة الوضع الأمني والنقاط الطرفية على هذا المجال، وقد أعيدت كتابة أمن الشبكات حول حافة خدمة الأمن.",
        "topics": [
            {
                "id": "D3.T1",
                "title": "Posture management across hybrid and multicloud",
                "titleAr": "إدارة الوضع الأمني عبر البيئات الهجينة والمتعددة",
                "teach": [
                    "Defender for Cloud posture, including MCSB",
                    "Secure Score, and what it does and does not measure",
                    "Integrated posture across hybrid and multicloud",
                    "Choosing among the cloud workload protection plans",
                    "Azure Arc as the mechanism for reaching non Azure estate",
                    "Defender External Attack Surface Management",
                    "Security Exposure Management: attack paths, attack surface reduction, insights and initiatives",
                ],
                "trap": "Secure Score, Defender for Cloud posture and Exposure Management are three different things that students merge into one. Separate them early with a worked example.",
                "trapAr": "درجة الأمان ووضع ديفندر وإدارة الانكشاف ثلاثة أشياء مختلفة يدمجها الطلبة في واحد، ففرّق بينها مبكرا بمثال معمول.",
            },
            {
                "id": "D3.T2",
                "title": "Server and client endpoints",
                "titleAr": "الخوادم والنقاط الطرفية للعملاء",
                "teach": [
                    "Requirements for servers across multiple platforms and operating systems",
                    "Mobile devices and clients: endpoint protection, hardening, configuration",
                    "IoT devices and embedded systems",
                    "OT and ICS through Defender for IoT",
                    "Security baselines for both server and client",
                    "Windows LAPS as an evaluation target",
                ],
                "trap": "OT and ICS appear here and again in the ATT&CK objective. Worth teaching once properly and cross referencing, since Gulf students frequently work in sectors where this is the real job.",
                "trapAr": "يظهر التشغيل والتحكم الصناعي هنا ومرة أخرى في هدف أتاك، ويحسن تدريسه مرة على وجهه مع الإحالة، فهو العمل الفعلي لكثير من طلبة الخليج.",
            },
            {
                "id": "D3.T3",
                "title": "SaaS, PaaS and IaaS requirements",
                "titleAr": "متطلبات خدمات البرمجيات والمنصات والبنية",
                "teach": [
                    "Baselines per service model",
                    "IoT workloads and web workloads",
                    "Containers and container orchestration as separate requirements",
                    "Azure AI services security",
                ],
                "trap": "Containers and orchestration are listed separately on purpose. Expect a question where the answer sits at the orchestration layer, not the image.",
                "trapAr": "الحاويات والتنسيق مدرجان منفصلين عن قصد، فتوقع سؤالا تقع إجابته في طبقة التنسيق لا في الصورة.",
            },
            {
                "id": "D3.T4",
                "title": "Network security and Security Service Edge",
                "titleAr": "أمن الشبكات وحافة خدمة الأمن",
                "teach": [
                    "Evaluating a network design against stated security requirements",
                    "Entra Internet Access as a secure web gateway",
                    "Entra Internet Access for Microsoft services, including cross tenant",
                    "Entra Private Access",
                ],
                "trap": "This objective is now largely SSE. Courses built on older material spend the time on NSGs and firewalls and miss what is actually assessed.",
                "trapAr": "صار هذا الهدف في معظمه عن حافة خدمة الأمن، والمقررات المبنية على مواد أقدم تنفق الوقت على مجموعات أمن الشبكة والجدران وتفوّت ما يُقاس فعلا.",
            },
        ],
    },
    {
        "id": "D4",
        "weight": "20-25%",
        "title": "Security solutions for applications and data",
        "titleAr": "الحلول الأمنية للتطبيقات والبيانات",
        "framing": "Microsoft 365, application lifecycle and data protection. AI now appears on both the data and the productivity side.",
        "framingAr": "مايكروسوفت ٣٦٥ ودورة حياة التطبيق وحماية البيانات، ويظهر الذكاء الاصطناعي الآن في جانبي البيانات والإنتاجية.",
        "topics": [
            {
                "id": "D4.T1",
                "title": "Securing Microsoft 365",
                "titleAr": "تأمين مايكروسوفت ٣٦٥",
                "teach": [
                    "Posture for productivity and collaboration measured by Secure Score",
                    "Defender for Office 365 and Defender for Cloud Apps",
                    "Intune for device management",
                    "Purview for securing data inside Microsoft 365",
                    "Data security and compliance controls in Copilot for Microsoft 365",
                ],
                "trap": "Copilot controls are new. Students assume existing Purview labelling covers it and stop there.",
                "trapAr": "ضوابط كوبايلوت جديدة، ويفترض الطلبة أن وسم بيرفيو القائم يغطيها فيتوقفون عندها.",
            },
            {
                "id": "D4.T2",
                "title": "Securing applications",
                "titleAr": "تأمين التطبيقات",
                "teach": [
                    "Assessing the posture of an existing application portfolio",
                    "Threat modelling business critical applications",
                    "A full lifecycle application security strategy",
                    "Standards and practices for the development process itself",
                    "Mapping technologies onto application security requirements",
                    "Workload identities for authenticating to Azure resources",
                    "API management and security",
                    "Azure Web Application Firewall",
                ],
                "trap": "Workload identity and agent identity are now both examinable and are not the same thing. Contrast them side by side.",
                "trapAr": "هوية الحمل وهوية الوكيل كلتاهما قابلة للاختبار الآن وليستا الشيء نفسه، فقابل بينهما جنبا إلى جنب.",
            },
            {
                "id": "D4.T3",
                "title": "Securing organisational data",
                "titleAr": "تأمين بيانات المؤسسة",
                "teach": [
                    "Data discovery and classification",
                    "Prioritising which data threats to mitigate first",
                    "Encryption at rest and in transit, Key Vault, infrastructure encryption",
                    "Security for data used in AI workloads",
                    "Azure SQL, Synapse Analytics and Cosmos DB",
                    "Azure Storage, with Defender for Storage and Defender for Databases",
                ],
                "trap": "Discovery and classification come before controls. Questions that lead with an encryption option are often testing whether you classify first.",
                "trapAr": "الاكتشاف والتصنيف يسبقان الضوابط، والأسئلة التي تبدأ بخيار تعمية تختبر غالبا هل تصنّف أولا.",
            },
        ],
    },
]

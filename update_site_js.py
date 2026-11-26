import os

ROOT_DIR = r"C:\Users\HP\Downloads\awtar-united\awtar-united"
PUBLIC_DIR = os.path.join(ROOT_DIR, "public")
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
PUBLIC_ASSETS = os.path.join(PUBLIC_DIR, "assets")

site_js_content = """/* AWTAR UNITED - LUXURY BILINGUAL & INTERACTIVE ENGINE */

// Translation Dictionary
const I18N = {
  en: {
    // Splash
    splash_text: "Awtar United Catering & Hospitality",

    // Navigation
    nav_home: "Home",
    nav_about: "About Us",
    nav_services: "Services",
    nav_menus: "Menus",
    nav_gallery: "Gallery",
    nav_events: "Events & Projects",
    nav_contact: "Contact",
    nav_quote: "Get a Quote",
    lang_btn: "العربية",

    // Home Hero Slider
    hero_badge: "Premier Hospitality in Riyadh",
    hero_title_1: "Refined Taste, Unforgettable Moments",
    hero_desc_1: "Luxury catering and royal hospitality for corporate summits, VIP celebrations and mega projects across the Kingdom.",
    btn_quote: "Request a Quote",
    btn_services: "Explore Services",
    btn_menus: "View Menus",
    btn_gallery: "View Gallery",

    // Stats Bar
    stat_years_num: "5+",
    stat_years_label: "Years of Excellence",
    stat_clients_num: "500+",
    stat_clients_label: "Prestigious Clients",
    stat_events_num: "5,000+",
    stat_events_label: "Flawlessly Catered Events",
    stat_team_num: "100%",
    stat_team_label: "Saudi & International Standards",

    // Home Services Section
    services_kicker: "Culinary & Hospitality Solutions",
    services_title: "Exceptional Services Tailored for You",
    services_subtitle: "From high-profile executive gatherings to mega-scale public events, we deliver hospitality with unmatched grace.",
    service_1_title: "Mega Project Catering",
    service_1_desc: "End-to-end catering operations for mega-projects, staff meal programs, food villages, and large-scale festival logistics.",
    service_2_title: "Corporate & Summit Catering",
    service_2_desc: "Flawless dining experiences for board meetings, conferences, business symposiums, and government assemblies.",
    service_3_title: "Royal Buffets & VIP Receptions",
    service_3_desc: "Standard, premium, and VIP multi-course banquet arrangements with live cooking stations and exquisite presentation.",
    service_4_title: "Coffee Break & Executive Refreshments",
    service_4_desc: "Artisanal specialty coffee, freshly baked French pastries, savory canapés, and bespoke mocktails for business intervals.",
    service_5_title: "Finger Food & Cocktail Canapés",
    service_5_desc: "Delicate gourmet finger foods, mini bites, and handcrafted appetizers designed for dynamic networking receptions.",
    service_6_title: "VIP Hospitality & Protocol Staff",
    service_6_desc: "Highly trained silver-service waitstaff, receptionists, hostesses, and event coordination specialists.",

    // Video Section
    video_kicker: "In Action",
    video_title: "Witness Our Craft & Precision",
    video_subtitle: "Step behind the scenes and experience the artistry, preparation, and grandeur of Awtar United.",
    video_1_title: "Culinary Excellence & Preparation",
    video_1_desc: "Watch our expert culinary team prepare lavish spreads using fresh, premium ingredients.",
    video_2_title: "Live Event & Banquet Hospitality",
    video_2_desc: "Live banquet setups, welcoming royal guests, and delivering impeccable service.",

    // Partners Section
    partners_kicker: "Honored Collaborations",
    partners_title: "Our Prestigious Partners & Clients",
    partners_subtitle: "Proud to collaborate with Saudi Arabia's most esteemed ministries, sovereign institutions, and corporate giants.",

    // About Page Distinct Elements
    about_hero_title: "Hospitality Rooted in Passion & Precision",
    about_hero_desc: "Discover the story, heritage, and culinary leadership behind Riyadh's foremost catering service.",
    about_story_kicker: "Our Heritage",
    about_story_title: "5+ Years of Defining Saudi Hospitality",
    about_story_text1: "Awtar United was founded on a simple yet profound conviction: hospitality should never be routine. An event's food and service define the memories guests carry home. Every detail—from the temperature of a hot dish to the courteous smile of a server—must convey genuine care.",
    about_story_text2: "Today, we stand proud as trusted catering partners to the Kingdom's largest ministries, international defense exhibitions, entertainment festivals, and corporate leaders.",
    timeline_kicker: "Key Milestones",
    timeline_title: "Our Journey of Excellence",
    t_year_1: "2019",
    t_desc_1: "Founded in Riyadh with a vision to revolutionize event catering through authentic Saudi care.",
    t_year_2: "2021",
    t_desc_2: "Awarded ongoing executive catering operations for prestigious government ministries and defence sectors.",
    t_year_3: "2023",
    t_desc_3: "Expanded to mega-project operations, festival catering, and VIP protocol for Riyadh Season and MDLBEAST.",
    t_year_4: "2026",
    t_desc_4: "Leading full-scale catering and hospitality partner aligned with Saudi Vision 2030 standards.",
    mission_title: "Our Mission",
    mission_desc: "To deliver culinary artistry and genuine hospitality that honors our clients' reputation.",
    vision_title: "Our Vision",
    vision_desc: "To be the leading Saudi hospitality enterprise recognized across the Gulf.",
    values_title: "Our Values",
    values_desc: "Authentic Saudi generosity, uncompromising food safety, and immaculate presentation.",
    quality_title: "Commitment to Quality",
    quality_desc: "Rigorous food safety certifications, daily fresh sourcing, and precision temperature logistics.",

    // Services Page Distinct Elements
    services_hero_title: "Comprehensive Hospitality Solutions",
    services_hero_desc: "Tailored catering solutions engineered for royal summits, corporate banquets, and high-volume operations.",
    workflow_kicker: "Our Process",
    workflow_title: "From Consultation to Flawless Service",
    step_1_title: "1. Consultation & Vision",
    step_1_desc: "We analyze your event scale, guest profile, and aesthetic preferences.",
    step_2_title: "2. Tasting & Menu Design",
    step_2_desc: "Curated multi-course menus crafted by executive chefs with tasting sessions.",
    step_3_title: "3. Precision Logistics",
    step_3_desc: "Equipped mobile kitchens, temperature-controlled transit, and seamless setup.",
    step_4_title: "4. Flawless Execution",
    step_4_desc: "Impeccable table service, live cooking, and attentive guest care until the final hour.",

    // Menus Page Distinct Elements
    menus_hero_title: "Curated Culinary Collections",
    menus_hero_desc: "Explore authentic Saudi banquets, international gourmet buffets, artisan coffee breaks, and exquisite desserts.",
    menu_cat_1: "Coffee Break VIP 1",
    menu_cat_2: "Coffee Break VIP 2",
    menu_cat_3: "International Buffet 1",
    menu_cat_4: "Executive Royal Buffet 2",
    menu_cat_5: "VIP Grand Banquet",
    menu_cat_6: "Gourmet Finger Food",
    menu_cat_7: "Plated VIP Menus",
    menu_cat_8: "Artisanal Desserts & Sweets",
    menu_cat_9: "Beverages & Specialty Mocktails",

    // Gallery Page
    gallery_hero_title: "Visual Feast & Portfolio",
    gallery_hero_desc: "A photographic journey through our signature buffets, corporate banquets, VIP hospitality, and exquisite food styling.",
    filter_all: "All Photographs",
    filter_buffet: "Buffets & Banquets",
    filter_projects: "Mega Projects & Corporate",
    filter_coffee: "Coffee Break & Sweets",
    filter_hospitality: "VIP Hospitality & Protocol",

    // Events Page
    events_hero_title: "Major Events & Project Portfolio",
    events_hero_desc: "Highlighting memorable operations and mega-scale events managed with supreme professionalism by Awtar United.",
    event_mod_title: "Ministry of Defence",
    event_mod_desc: "High-efficiency management of daily and monthly executive catering and operations with comprehensive logistical coordination.",
    event_mdl_title: "MDLBEAST Soundstorm",
    event_mdl_desc: "Massive logistical and catering support for world-class artists, VIP lounges, and tens of thousands of event participants.",
    event_balad_title: "Balad Beast Jeddah",
    event_balad_desc: "Delivering exceptional hospitality, specialized food stations, and round-the-clock service in historic settings.",

    // Contact Page
    contact_hero_title: "Let's Plan Your Next Event",
    contact_hero_desc: "Get in touch with our event planners today. We are available to consult, customize, and deliver excellence.",
    contact_info_title: "Direct Inquiries",
    contact_phone: "Phone / Support",
    contact_email: "Email Address",
    contact_address: "Location & Service Area",
    contact_address_val: "Riyadh, Kingdom of Saudi Arabia",
    contact_hours: "Business Hours",
    contact_hours_val: "Saturday – Thursday, 9:00 AM – 9:00 PM. Friday closed.",

    // Quote Page
    quote_hero_title: "Request a Customized Quotation",
    quote_hero_desc: "Provide your event specifications and our banquet managers will formulate a detailed bespoke proposal within hours.",
    form_fullname: "Full Name",
    form_company: "Company / Organization",
    form_email: "Email Address",
    form_phone: "Phone Number",
    form_event_type: "Event Type",
    form_event_date: "Event Date",
    form_location: "Event Location in Riyadh",
    form_guests: "Estimated Number of Guests",
    form_budget: "Estimated Budget (Optional)",
    form_services_needed: "Required Services",
    form_menu_pref: "Menu & Dietary Preferences",
    form_notes: "Additional Notes or Special Requirements",
    form_submit_quote: "Submit Quotation Request",
    form_submit_msg: "Send Message",
    form_whatsapp_cta: "Chat Directly on WhatsApp",

    // Footer
    footer_about: "Awtar United brings together culinary excellence and authentic Saudi hospitality for corporate events, private celebrations, and mega projects in Riyadh.",
    footer_quick_links: "Quick Navigation",
    footer_services_title: "Services",
    footer_contact_title: "Get in Touch",
    footer_copyright: "© 2026 Awtar United Catering Services. All Rights Reserved. Riyadh, Saudi Arabia.",
    whatsapp_tooltip: "Chat on WhatsApp"
  },

  ar: {
    // Splash
    splash_text: "أوتار المتحدة للضيافة والإعاشة",

    // Navigation
    nav_home: "الرئيسية",
    nav_about: "من نحن",
    nav_services: "خدماتنا",
    nav_menus: "قوائم الطعام",
    nav_gallery: "معرض الصور",
    nav_events: "المشاريع والفعاليات",
    nav_contact: "تواصل معنا",
    nav_quote: "طلب تسعيرة",
    lang_btn: "English",

    // Home Hero Slider
    hero_badge: "الضيافة والإعاشة الفاخرة في الرياض",
    hero_title_1: "مذاق رفيع.. ولحظات لا تُنسى",
    hero_desc_1: "خدمات تموين وإعاشة ملكية وراقية للمؤتمرات الكبرى، الفعاليات الخاصة، والمشاريع الاستراتيجية في كافة أنحاء المملكة.",
    btn_quote: "طلب عرض سعر",
    btn_services: "استكشف خدماتنا",
    btn_menus: "تصفح القوائم",
    btn_gallery: "معرض الصور",

    // Stats Bar
    stat_years_num: "+5",
    stat_years_label: "سنوات من التميز",
    stat_clients_num: "+500",
    stat_clients_label: "عميل من النخبة",
    stat_events_num: "+5,000",
    stat_events_label: "فعالية تم تنفيذها بنجاح",
    stat_team_num: "100%",
    stat_team_label: "معايير سعودية وعالمية",

    // Home Services Section
    services_kicker: "حلول الضيافة والإعاشة",
    services_title: "خدمات استثنائية مصممة خصيصاً لمناسبتك",
    services_subtitle: "من الاجتماعات التنفيذية الرفيعة وحتى الفعاليات والمشاريع المليونية، نقدم ضيافة تعكس رقيكم وأصالتكم.",
    service_1_title: "تموين المشاريع والفعاليات الكبرى",
    service_1_desc: "حلول إعاشة متكاملة للمشاريع الضخمة، المهرجانات، قرى الفعاليات، وبرامج إعاشة الموظفين والفرق الميدانية.",
    service_2_title: "إعاشة الشركات والمؤتمرات",
    service_2_desc: "تجارب طعام وضيافة راقية لاجتماعات مجالس الإدارة، قمم الأعمال، والملتقيات الحكومية والدولية.",
    service_3_title: "البوفيهات الملكية وحفلات VIP",
    service_3_desc: "بوفيهات عالمية ومحلية استثنائية مع محطات طهي مباشر وأواني فاخرة تلبي أذواق كبار الشخصيات.",
    service_4_title: "كوفي بريك واستراحات القهوة",
    service_4_desc: "قهوة مختصة، مخبوزات فرنسية طازجة، مقبلات خفيفة، ومشروبات باردة منعشة لفترات الاستراحة في المؤتمرات.",
    service_5_title: "المقبلات الراقية وفينجر فود",
    service_5_desc: "كانابيه وأطباق صغيرة مبتكرة تُقدّم بأناقة فائقة لتناسب حفلات الاستقبال واللقاءات التفاعلية.",
    service_6_title: "خدمات الضيافة وبروتوكول VIP",
    service_6_desc: "طواقم ضيافة ومضيفين مدربين بأعلى المعايير الدبلوماسية لتقديم خدمة تليق بمقام ضيوفكم الكرام.",

    // Video Section
    video_kicker: "في الميدان",
    video_title: "شاهد دقة وإتقان فريق أوتار المتحدة",
    video_subtitle: "جولة خلف الكواليس لتتعرف على شغف التحضير وفخامة التقديم في فعالياتنا ومطابخنا المركزية.",
    video_1_title: "إبداع الطهي وتحضير الولائم",
    video_1_desc: "شاهد فريق الطهاة المحترفين أثناء تجهيز أشهى الأطباق الطازجة بأعلى معايير سلامة الغذاء.",
    video_2_title: "الضيافة الميدانية واستقبال الضيوف",
    video_2_desc: "لقطات حية من تنظيم وتنسيق البوفيهات الفاخرة وتقديم تجربة ضيافة ملكية لا تُنسى.",

    // Partners Section
    partners_kicker: "شركاء النجاح",
    partners_title: "شركاؤنا وعملاؤنا من النخبة",
    partners_subtitle: "نفخر بالتعاون المستمر مع نخبة الوزارات، الهيئات الحكومية المرموقة، وكبرى الشركات في المملكة العربية السعودية.",

    // About Page Distinct Elements
    about_hero_title: "ضيافة سعودية نابعة من الشغف والاهتمام",
    about_hero_desc: "تعرف على قصة أوتار المتحدة، قيمنا الأصيلة، والفريق المتفاني خلف أرقى مناسبات العاصمة الرياض.",
    about_story_kicker: "أصالتنا ومسيرتنا",
    about_story_title: "أكثر من 5 سنوات في قيادة الإعاشة والضيافة في الرياض",
    about_story_text1: "بدأنا أوتار المتحدة لأننا رأينا مناسبات كثيرة كان الطعام فيها موجوداً فقط دون روح أو عناية بالتفاصيل. فقررنا أن نكون مختلفين؛ كل طبق نقدمه وكل فعالية نخدمها نتعامل معها كأنها مناسبة عائلتنا الخاصة بكل حفاوة وكرم.",
    about_story_text2: "واليوم، نحن الخيار الموثوق لإعاشة كبرى الجهات والوزارات والمعارض الدفاعية الدولية والفعاليات الجماهيرية الكبرى. نمتلك مطابخ مركزية متطورة وأسطول نقل مجهز يضمن أعلى درجات الطزاجة والجودة.",
    timeline_kicker: "محطات مضيئة",
    timeline_title: "مسيرة النجاح والتوسع",
    t_year_1: "2019",
    t_desc_1: "انطلاق أوتار المتحدة في الرياض برؤية تهدف للارتقاء بخدمات التموين والضيافة السعودية.",
    t_year_2: "2021",
    t_desc_2: "الفوز بعقود إعاشة كبرى للجهات الحكومية والقطاعات الدفاعية بأعلى المعايير التنظيمية.",
    t_year_3: "2023",
    t_desc_3: "التوسع في تموين مهرجانات موسم الرياض، فعاليات مدل بيست، وقرى المشاريع الاستراتيجية.",
    t_year_4: "2026",
    t_desc_4: "الريادة في تقديم أرقى حلول الضيافة والإعاشة المتوافقة مع مستهدفات رؤية السعودية 2030.",
    mission_title: "رسالتنا",
    mission_desc: "تقديم فنون طهي راقية وضيافة تعتز بالهوية وتليق بمكانة عملائنا الكرام.",
    vision_title: "رؤيتنا",
    vision_desc: "أن نكون الشركة السعودية الرائدة والأولى في قطاع الإعاشة والضيافة في منطقة الخليج.",
    values_title: "قيمنا",
    values_desc: "الكرم السعودي الأصيل، الجودة الصارمة، جماليات التقديم، والاحترام التام لكل ضيف.",
    quality_title: "التزامنا بالجودة",
    quality_desc: "شهادات سلامة الغذاء العالمية، توريد يومي للمكونات الطازجة، وضبط حراري دقيق.",

    // Services Page Distinct Elements
    services_hero_title: "حلول متكاملة في التموين والإعاشة الفاخرة",
    services_hero_desc: "خدمات مصممة هندسياً للقمم الملكية، مؤتمرات الشركات، ومشاريع الإعاشة المليونية.",
    workflow_kicker: "منهجية العمل",
    workflow_title: "من التخطيط والاستشارة إلى التنفيذ الميداني",
    step_1_title: "1. الاستشارة وتحديد الاحتياج",
    step_1_desc: "دراسة نوع الفعالية، فئات الضيوف، والطابع العام المطلوب للمائدة والخدمة.",
    step_2_title: "2. تصميم القائمة وتجربة التذوق",
    step_2_desc: "إعداد مقترحات طهي مبتكرة من قبل طهاتنا المعتمدين مع جلسة تذوق خاصة.",
    step_3_title: "3. الجاهزية اللوجستية الدقيقة",
    step_3_desc: "نقل آمن بدرجات حرارة مضبوطة وتجهيز كامل للمعدات وأطقم الضيافة قبل الفعالية.",
    step_4_title: "4. التنفيذ والخدمة الملكية",
    step_4_desc: "خدمة راقية بابتسامة احترافية وإشراف ميداني مستمر حتى مغادرة آخر ضيف.",

    // Menus Page Distinct Elements
    menus_hero_title: "قوائم طعام وتشكيلات طهي مبتكرة",
    menus_hero_desc: "استكشف خياراتنا المتنوعة من قوائم استراحات القهوة، البوفيهات الشرقية والغربية، والولائم السعودية الفاخرة.",
    menu_cat_1: "كوفي بريك VIP الأول",
    menu_cat_2: "كوفي بريك VIP الثاني",
    menu_cat_3: "بوفيه عالمي فاخر 1",
    menu_cat_4: "بوفيه تنفيذي ملكي 2",
    menu_cat_5: "وليمة كبار الشخصيات VIP",
    menu_cat_6: "أصناف فينجر فود الراقية",
    menu_cat_7: "قوائم الضيافة المسكوبة في الصحون",
    menu_cat_8: "تشكيلة الحلويات الشرقية والغربية",
    menu_cat_9: "المشروبات المنعشة والموكتيلات",

    // Gallery Page
    gallery_hero_title: "معرض الصور والأعمال",
    gallery_hero_desc: "جولة بصرية توثق لمساتنا في تنسيق الموائد، تقديم الأطباق، والخدمة الراقية في كبرى فعاليات الرياض.",
    filter_all: "جميع الصور",
    filter_buffet: "بوفيهات وولائم",
    filter_projects: "المشاريع الكبرى والشركات",
    filter_coffee: "كوفي بريك وحلويات",
    filter_hospitality: "ضيافة كبار الشخصيات",

    // Events Page
    events_hero_title: "سجل الفعاليات والمشاريع الكبرى",
    events_hero_desc: "محطات مضيئة ومشاريع وطنية كبرى تشرفنا بتنفيذ خدمات الإعاشة والضيافة لها بأعلى معايير الإتقان.",
    event_mod_title: "وزارة الدفاع",
    event_mod_desc: "إدارة عمليات الإعاشة اليومية والشهرية بكفاءة عالية وتنظيم دقيق يلبي أعلى متطلبات العمليات الرسمية.",
    event_mdl_title: "مدل بيست ساوندستورم",
    event_mdl_desc: "دعم لوجستي وغذائي ضخم لكبار الضيوف والفنانين وعشرات الآلاف من زوار المهرجان الموسيقي الأكبر.",
    event_balad_title: "بلد بيست جدة التاريخية",
    event_balad_desc: "تقديم تجربة ضيافة تراثية عصرية متكاملة ومحطات طعام مجهزة على مدار الساعة في قلب جدة التاريخية.",

    // Contact Page
    contact_hero_title: "تواصل مع مستشاري الفعاليات",
    contact_hero_desc: "يسعدنا الرد على استفساراتكم ومشاركتكم التخطيط لمناسبتكم القادمة في مدينة الرياض والمناطق المجاورة.",
    contact_info_title: "معلومات التواصل المباشر",
    contact_phone: "الهاتف / خدمة العملاء",
    contact_email: "البريد الإلكتروني",
    contact_address: "الموقع ونطاق الخدمة",
    contact_address_val: "الرياض، المملكة العربية السعودية",
    contact_hours: "أوقات العمل الرسمية",
    contact_hours_val: "السبت – الخميس: 9:00 صباحاً – 9:00 مساءً (الجمعة مغلق)",

    // Quote Page
    quote_hero_title: "طلب عرض سعر مخصص لمناسبتك",
    quote_hero_desc: "يرجى تعبئة تفاصيل الفعالية وسيقوم مديرو الضيافة بإعداد مقترح مالي وفني مفصل خلال ساعات معدودة.",
    form_fullname: "الاسم الكامل",
    form_company: "اسم الشركة / الجهة (اختياري)",
    form_email: "البريد الإلكتروني",
    form_phone: "رقم الجوال",
    form_event_type: "نوع الفعالية",
    form_event_date: "تاريخ الفعالية",
    form_location: "مكان الفعالية في الرياض",
    form_guests: "العدد التقريبي للضيوف",
    form_budget: "الميزانية المتوقعة (اختياري)",
    form_services_needed: "الخدمات المطلوبة",
    form_menu_pref: "تفضيلات قائمة الطعام والحميات",
    form_notes: "ملاحظات إضافية أو متطلبات خاصة",
    form_submit_quote: "إرسال طلب التسعيرة",
    form_submit_msg: "إرسال الرسالة",
    form_whatsapp_cta: "تواصل مباشرة عبر واتساب",

    // Footer
    footer_about: "تجمع أوتار المتحدة بين أرقى فنون الطهي وكرم الضيافة السعودية الأصيلة لإثراء المناسبات الخاصة، فعاليات الشركات، والمشاريع الكبرى في الرياض.",
    footer_quick_links: "روابط سريعة",
    footer_services_title: "أبرز الخدمات",
    footer_contact_title: "تواصل معنا",
    footer_copyright: "© 2026 أوتار المتحدة لخدمات الإعاشة والضيافة. جميع الحقوق محفوظة. الرياض، المملكة العربية السعودية.",
    whatsapp_tooltip: "تواصل عبر واتساب"
  }
};

let currentLang = localStorage.getItem('awtar_language') || 'en';

function applyLanguage(lang) {
  currentLang = lang;
  localStorage.setItem('awtar_language', lang);
  
  const isRtl = lang === 'ar';
  document.documentElement.lang = lang;
  document.documentElement.dir = isRtl ? 'rtl' : 'ltr';
  document.body.classList.toggle('rtl', isRtl);

  const langToggleBtn = document.getElementById('lang-toggle-btn');
  if (langToggleBtn) {
    langToggleBtn.querySelector('.lang-label').textContent = lang === 'en' ? 'العربية' : 'English';
  }

  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (I18N[lang] && I18N[lang][key]) {
      el.textContent = I18N[lang][key];
    }
  });

  document.querySelectorAll('[data-i18n-ph]').forEach(el => {
    const key = el.getAttribute('data-i18n-ph');
    if (I18N[lang] && I18N[lang][key]) {
      el.placeholder = I18N[lang][key];
    }
  });

  document.querySelectorAll('.partner-card').forEach(card => {
    const span = card.querySelector('span');
    if (span) {
      span.textContent = isRtl ? (card.dataset.nameAr || span.textContent) : (card.dataset.nameEn || span.textContent);
    }
  });
}

// Splash hide helper
function hideSplash() {
  const splash = document.getElementById('site-splash-loader');
  if (splash) {
    splash.classList.add('hidden');
    setTimeout(() => {
      splash.style.display = 'none';
    }, 600);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  applyLanguage(currentLang);

  const langBtn = document.getElementById('lang-toggle-btn');
  if (langBtn) {
    langBtn.addEventListener('click', () => {
      const nextLang = currentLang === 'en' ? 'ar' : 'en';
      applyLanguage(nextLang);
    });
  }

  const navToggle = document.getElementById('nav-toggle-btn');
  const navMenu = document.getElementById('nav-menu');
  if (navToggle && navMenu) {
    navToggle.addEventListener('click', () => {
      navMenu.classList.toggle('active');
    });
  }

  // Hero Slider
  const slider = document.querySelector('.hero-slider-section');
  if (slider) {
    const slides = slider.querySelectorAll('.slide');
    const dotsContainer = slider.querySelector('.slider-dots');
    const prevBtn = slider.querySelector('.slider-prev');
    const nextBtn = slider.querySelector('.slider-next');
    let currentIndex = 0;
    let autoInterval;

    if (slides.length > 1) {
      if (dotsContainer) {
        dotsContainer.innerHTML = '';
        slides.forEach((_, idx) => {
          const dot = document.createElement('button');
          dot.className = `slider-dot ${idx === 0 ? 'active' : ''}`;
          dot.setAttribute('aria-label', `Go to slide ${idx + 1}`);
          dot.addEventListener('click', () => goToSlide(idx));
          dotsContainer.appendChild(dot);
        });
      }

      function updateSlide(newIndex) {
        slides[currentIndex].classList.remove('active');
        const dots = dotsContainer ? dotsContainer.querySelectorAll('.slider-dot') : [];
        if (dots[currentIndex]) dots[currentIndex].classList.remove('active');

        currentIndex = (newIndex + slides.length) % slides.length;

        slides[currentIndex].classList.add('active');
        if (dots[currentIndex]) dots[currentIndex].classList.add('active');
      }

      function goToSlide(idx) {
        updateSlide(idx);
        restartAutoplay();
      }

      if (prevBtn) {
        prevBtn.addEventListener('click', () => {
          updateSlide(currentIndex - 1);
          restartAutoplay();
        });
      }
      if (nextBtn) {
        nextBtn.addEventListener('click', () => {
          updateSlide(currentIndex + 1);
          restartAutoplay();
        });
      }

      function startAutoplay() {
        autoInterval = setInterval(() => {
          updateSlide(currentIndex + 1);
        }, 5500);
      }

      function restartAutoplay() {
        clearInterval(autoInterval);
        startAutoplay();
      }

      slider.addEventListener('mouseenter', () => clearInterval(autoInterval));
      slider.addEventListener('mouseleave', () => startAutoplay());

      startAutoplay();
    }
  }

  // Gallery Filter
  const filterBtns = document.querySelectorAll('.filter-btn');
  const galleryItems = document.querySelectorAll('.gallery-item');
  if (filterBtns.length > 0) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const filter = btn.dataset.filter;

        galleryItems.forEach(item => {
          if (filter === 'all' || item.dataset.category === filter) {
            item.style.display = 'block';
          } else {
            item.style.display = 'none';
          }
        });
      });
    });
  }

  // Gallery Lightbox
  const lightbox = document.getElementById('gallery-lightbox');
  if (lightbox) {
    galleryItems.forEach(item => {
      item.addEventListener('click', () => {
        const img = item.querySelector('img');
        const modalImg = lightbox.querySelector('img');
        if (img && modalImg) {
          modalImg.src = img.src;
          modalImg.alt = img.alt;
          if (typeof lightbox.showModal === 'function') {
            lightbox.showModal();
          }
        }
      });
    });
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) lightbox.close();
    });
  }

  // Form handling
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const alert = document.getElementById('contact-alert');
      if (alert) {
        alert.style.display = 'block';
        alert.scrollIntoView({ behavior: 'smooth' });
      }
      contactForm.reset();
    });
  }

  const quoteForm = document.getElementById('quote-form');
  if (quoteForm) {
    const params = new URLSearchParams(window.location.search);
    const serviceParam = params.get('service');
    if (serviceParam) {
      document.querySelectorAll('input[name="services"]').forEach(cb => {
        if (cb.value.toLowerCase().includes(serviceParam.toLowerCase())) {
          cb.checked = true;
        }
      });
    }

    quoteForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const ref = 'AWT-' + Math.floor(100000 + Math.random() * 900000);
      const alert = document.getElementById('quote-alert');
      const refSpan = document.getElementById('quote-ref-code');
      if (refSpan) refSpan.textContent = ref;
      if (alert) {
        alert.style.display = 'block';
        alert.scrollIntoView({ behavior: 'smooth' });
      }

      const name = quoteForm.querySelector('[name="name"]')?.value || '';
      const phone = quoteForm.querySelector('[name="phone"]')?.value || '';
      const guests = quoteForm.querySelector('[name="guests"]')?.value || '';
      const eventType = quoteForm.querySelector('[name="event_type"]')?.value || '';
      const text = `Hello Awtar United, I would like to request a quotation (Ref: ${ref}). Name: ${name}, Phone: ${phone}, Event: ${eventType}, Guests: ${guests}.`;
      
      const waBtn = document.getElementById('quote-whatsapp-submit');
      if (waBtn) {
        waBtn.href = `https://wa.me/966545264145?text=${encodeURIComponent(text)}`;
        waBtn.style.display = 'inline-flex';
      }
      quoteForm.reset();
    });
  }
});

// Splash dismiss on load or fallback
window.addEventListener('load', hideSplash);
setTimeout(hideSplash, 1200);
"""

with open(os.path.join(ASSETS_DIR, "site.js"), "w", encoding="utf-8") as f:
    f.write(site_js_content)
with open(os.path.join(PUBLIC_ASSETS, "site.js"), "w", encoding="utf-8") as f:
    f.write(site_js_content)

print("Updated site.js with splash loader handling!")

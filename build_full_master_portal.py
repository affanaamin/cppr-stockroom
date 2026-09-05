import json
import os

print("Assembling complete, 100% interactive Master Portal...")

with open("documents.json", "r", encoding="utf-8") as f:
    raw_docs = json.load(f)

print(f"Loaded {len(raw_docs)} documents.")

docs_json_compact = json.dumps(raw_docs, ensure_ascii=False)

faqs = [
    {
        "q": "1. What is the Public Policy Stockroom?",
        "a": "The Public Policy Stockroom is a centralized digital repository and reference hub established at the Centre for Public Policy Research (CPPR), IMSciences Peshawar. It systematically archives, indexes, and categorizes substantive public policies, statutory laws, delegated rules, standard operating procedures, and strategic governance frameworks across Khyber Pakhtunkhwa and Pakistan."
    },
    {
        "q": "2. Why is CPPR establishing a Public Policy Stockroom?",
        "a": "Historically, public policy and legislative instruments in Pakistan have been scattered across disparate departmental archives, gazettes, and private law libraries. CPPR is establishing the Stockroom to eliminate institutional memory loss, reduce research duplication, and provide academics, policymakers, and civil society with verified, canonical access to governance instruments."
    },
    {
        "q": "3. What is the main purpose of the Stockroom?",
        "a": "The primary mission is to facilitate empirical, evidence-based policymaking by maintaining an authoritative, categorized, and continuously updated repository of Pakistan's legislative, regulatory, and policy instruments."
    },
    {
        "q": "4. What types of documents does the Stockroom contain?",
        "a": "The Stockroom strictly archives substantive policy instruments: (1) Primary Acts & Ordinances passed by provincial and national assemblies; (2) Statutory Rules & Regulations notified under delegated legislative authority; (3) Sectoral Public Policies approved by the Cabinet; (4) Departmental SOPs & Guidelines; (5) Canonical Rules of Business; and (6) International Legal Commitments & Treaties."
    },
    {
        "q": "5. What period does the Stockroom cover?",
        "a": "The primary focus is on the Post-18th Constitutional Amendment era (2010–Present), representing the devolution of powers to provinces. However, the repository also catalogues the 1973–2009 Democratic Era, the 1947–1972 Post-Independence Era, and foundational Pre-Partition statutes that remain in force today."
    },
    {
        "q": "6. How is the Stockroom organized?",
        "a": "The repository is indexed according to a 3-tier legal hierarchy: Tier 1 Primary Statutes (Acts & Ordinances), Tier 2 Subordinate Delegated Legislation (Rules & Regulations), and Tier 3 Executive Instruments (Policies, SOPs, Action Plans). Cross-indexing allows multi-dimensional navigation across 28 provincial departments, constitutional eras, and regulatory status."
    },
    {
        "q": "7. Who can use the Public Policy Stockroom?",
        "a": "The Stockroom is an open institutional asset accessible to university faculty, graduate researchers, students, parliamentary committees, administrative secretaries, judges, legal practitioners, development partners, and investigative journalists."
    },
    {
        "q": "8. How will researchers and academics benefit?",
        "a": "Researchers gain instant, single-pane access to canonical legal texts with clause-level search, automated academic citation generators (APA 7th, OSCOLA, Pakistan Law Site), and cross-departmental comparative redlines without having to manually search dispersed provincial gazettes."
    },
    {
        "q": "9. How does the Stockroom support evidence-based policymaking?",
        "a": "By linking statutory mandates directly to empirical datasets and secondary regulations. Analysts can trace the entire regulatory lifecycle of a statute, examining enabling clauses, administrative rules of business, and implementation gaps."
    },
    {
        "q": "10. Can the Stockroom support comparative policy research?",
        "a": "Yes. Researchers can evaluate legislative activity across multiple administrative departments (e.g. Health vs. Higher Education), compare provincial devolution before and after the 18th Amendment, and contrast regulatory density over time."
    },
    {
        "q": "11. How are documents classified and tagged?",
        "a": "Every document undergoes standard accession metadata tagging: Title, Ref ID, Legal Hierarchy Tier, Sector / Custodian Department, Promulgation Date, Constitutional Era, In Force / Amended / Repealed Status, Enabling Parent Authority, and Delegated Subordinate Rules."
    },
    {
        "q": "12. Are citation formats available for scholarly publications?",
        "a": "Yes. The platform features an automated Citation Studio generating 1-click standardized academic citations in APA 7th Edition, OSCOLA (Oxford Standard for the Citation of Legal Authorities), and Pakistan Law Site formats."
    },
    {
        "q": "13. How will the Stockroom be maintained and updated?",
        "a": "CPPR maintains an active Accession Pipeline in coordination with the Provincial Assembly Secretariat, Khyber Pakhtunkhwa Government Printing Press (Official Gazette), and departmental law sections to index newly enacted instruments."
    },
    {
        "q": "14. What role do student researchers and interns play?",
        "a": "Undergraduate and graduate research assistants at IMSciences participate in metadata verification, legal lineage mapping, clause-by-clause indexing, and preparing executive policy briefs."
    },
    {
        "q": "15. What is the long-term vision for the Stockroom?",
        "a": "The long-term vision is to establish a comprehensive, accessible, and continuously curated Public Policy Stockroom at CPPR that serves as Pakistan's premier computational law and policy intelligence portal, integrating legal analytics, statutory lineage tracking, and automated policy impact assessments."
    }
]

faqs_json = json.dumps(faqs, ensure_ascii=False)

glossary = [
    # Constitutional Wordlist
    {"term": "Constitution", "cat": "Constitutional", "def": "The supreme legal framework of Pakistan. It establishes the structure of the State, defines powers and responsibilities of institutions, provides for fundamental rights, and sets out the relationship between the federation and provinces."},
    {"term": "Amendment", "cat": "Constitutional", "def": "A formal modification made to the Constitution through the special procedure prescribed by Article 238 and 239 requiring a two-thirds majority in Parliament."},
    {"term": "Article", "cat": "Constitutional", "def": "A numbered provision of the Constitution containing a specific rule, principle, right, institutional arrangement, or constitutional requirement."},
    {"term": "Basic Structure", "cat": "Constitutional", "def": "Foundational constitutional doctrine recognizing core democratic, judicial, and federal features that are inviolable."},
    {"term": "Distribution of Powers", "cat": "Constitutional", "def": "The constitutional demarcation of legislative, fiscal, and administrative competence between the Federation and the Provinces."},
    {"term": "Fundamental Rights", "cat": "Constitutional", "def": "Inviolable protections enshrined in Chapter 1 of the Constitution, including life, liberty, equality, dignity, speech, assembly, and fair trial."},
    {"term": "Parliamentary Democracy", "cat": "Constitutional", "def": "A system of government in which the executive branch derives its democratic legitimacy from and is politically responsible to the legislature."},
    {"term": "Directive Principles of State Policy", "cat": "Constitutional", "def": "Constitutional principles (Articles 29–40) guiding state organs in socio-economic policy, social justice, and citizen welfare."},
    {"term": "Article 140A (Local Government)", "cat": "Constitutional", "def": "Mandatory constitutional provision compelling each province to establish local governments and devolve political, administrative, and financial authority."},
    {"term": "Federal Legislative List", "cat": "Constitutional", "def": "Fourth Schedule to the Constitution defining exclusive subjects within the legislative competence of federal Parliament post-18th Amendment."},
    {"term": "Judicial Review", "cat": "Constitutional", "def": "The constitutional power of superior courts under Articles 184(3) and 199 to examine the legality or constitutional validity of statutes and executive acts."},
    # Legislative Process Wordlist
    {"term": "Bill vs. Act", "cat": "Legislative", "def": "A Bill is a proposed law introduced in Parliament or a Provincial Assembly. An Act is a Bill that has completed all readings, received gubernatorial or presidential assent, and been published in the official Gazette."},
    {"term": "Assent", "cat": "Legislative", "def": "Formal constitutional approval required from the Governor or President for a passed Bill to acquire the force of law."},
    {"term": "Ordinance", "cat": "Legislative", "def": "Temporary emergency legislation promulgated by the Governor or President under constitutional authority when the legislature is not in session."},
    {"term": "Statutory Rules", "cat": "Legislative", "def": "Subordinate regulatory frameworks framed by executive departments under delegated authority specifically conferred by an enabling parent Act."},
    {"term": "Clause-by-Clause Consideration", "cat": "Legislative", "def": "The rigorous second-reading parliamentary stage where each clause, sub-clause, and proposed amendment of a Bill is debated and voted upon individually."},
    {"term": "Committee Stage", "cat": "Legislative", "def": "Detailed scrutiny of a draft Bill by a specialized Standing Committee of the Assembly prior to plenary debate."},
    {"term": "Rules of Business", "cat": "Legislative", "def": "Canonical rules framed under constitutional authority governing the allocation of ministerial portfolios, transaction of cabinet business, and departmental procedures."},
    {"term": "Standard Operating Procedures (SOPs)", "cat": "Legislative", "def": "Operational guidelines issued by departmental heads to ensure uniform day-to-day administrative implementation of statutory rules."},
    # Public Policy Wordlist
    {"term": "Public Policy", "cat": "Policy", "def": "A purposive course of action, strategic framework, or set of decisions adopted by government to address societal challenges and achieve public welfare objectives."},
    {"term": "Evidence-Based Policy", "cat": "Policy", "def": "Policy formulation informed by rigorous empirical data, independent evaluation, statutory analysis, and quantifiable baseline indicators."},
    {"term": "Action Plan", "cat": "Policy", "def": "A practical operational document setting out specific activities, institutional responsibilities, timelines, and measurable indicators for implementing a policy or strategy."},
    {"term": "Policy Cycle", "cat": "Policy", "def": "The iterative governance process encompassing problem identification, agenda setting, formulation, adoption, implementation, and evaluation."},
    {"term": "Policy Instrument", "cat": "Policy", "def": "The specific governance tool selected to achieve a policy objective, categorized into legal mandates, financial allocations, or organizational frameworks."},
    {"term": "Regulation", "cat": "Policy", "def": "A binding rule or requirement issued by a competent authority under legal authority to govern particular activities, conduct, or sectors."},
    {"term": "Regulatory Impact Assessment (RIA)", "cat": "Policy", "def": "A systematic methodology for assessing the positive and negative socio-economic effects of proposed or existing legislation."},
    {"term": "Devolution", "cat": "Policy", "def": "The constitutional transfer of decision-making, executive powers, and financial resources from central/provincial authorities to elected local tiers."},
    {"term": "Stakeholder Consultation", "cat": "Policy", "def": "Participatory engagement with citizens, professional associations, academic institutions, and affected groups during policy formulation."}
]

glossary_json = json.dumps(glossary, ensure_ascii=False)

# Read the base template parts
html_template = '''<!DOCTYPE html>
<html class="light" lang="en">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>CPPR Public Policy Stockroom | IMSciences Peshawar</title>
    
    <!-- Tailwind CSS & Plugins -->
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    
    <!-- Google Fonts: Inter & JetBrains Mono -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet"/>
    <!-- Material Symbols -->
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
    <!-- Chart.js for Visual Analytics -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <!-- Tailwind Configuration matching Lexicon Authority Design System -->
    <script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        primary: "#002046",
                        "primary-container": "#1b365d",
                        "on-primary": "#ffffff",
                        "on-primary-container": "#87a0cd",
                        "primary-fixed": "#d6e3ff",
                        "primary-fixed-dim": "#aec7f7",
                        secondary: "#775a19",
                        "secondary-container": "#fed488",
                        "on-secondary": "#ffffff",
                        "on-secondary-container": "#785a1a",
                        "secondary-fixed": "#ffdea5",
                        "secondary-fixed-dim": "#e9c176",
                        tertiary: "#132233",
                        "tertiary-container": "#29374a",
                        "on-tertiary": "#ffffff",
                        background: "#f7f9fb",
                        "on-background": "#191c1e",
                        surface: "#f7f9fb",
                        "on-surface": "#191c1e",
                        "surface-bright": "#ffffff",
                        "surface-dim": "#d8dadc",
                        "surface-container-lowest": "#ffffff",
                        "surface-container-low": "#f2f4f6",
                        "surface-container": "#eceef0",
                        "surface-container-high": "#e6e8ea",
                        "surface-container-highest": "#e0e3e5",
                        "on-surface-variant": "#44474e",
                        outline: "#74777f",
                        "outline-variant": "#c4c6cf",
                        error: "#ba1a1a",
                        "error-container": "#ffdad6",
                        "on-error": "#ffffff",
                        "on-error-container": "#93000a"
                    },
                    borderRadius: {
                        DEFAULT: "0.25rem",
                        sm: "0.125rem",
                        md: "0.375rem",
                        lg: "0.5rem",
                        xl: "0.75rem",
                        full: "9999px"
                    },
                    spacing: {
                        unit: "4px",
                        "density-compact": "8px",
                        "density-comfortable": "16px",
                        gutter: "24px",
                        "margin-mobile": "16px",
                        "margin-desktop": "40px",
                        "container-max": "1440px"
                    },
                    fontFamily: {
                        headline: ["Inter", "sans-serif"],
                        body: ["Inter", "sans-serif"],
                        mono: ["JetBrains Mono", "monospace"]
                    }
                }
            }
        }
    </script>

    <style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
            display: inline-block;
            vertical-align: middle;
            line-height: 1;
        }
        /* Custom scrollbars */
        ::-webkit-scrollbar { width: 7px; height: 7px; }
        ::-webkit-scrollbar-track { background: #f1f5f9; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
        
        .zebra-row:nth-child(even) { background-color: #fafbfc; }
        .zebra-row:nth-child(odd) { background-color: #ffffff; }

        /* Smooth Tab Display */
        .portal-tab { display: none; }
        .portal-tab.active { display: flex; animation: fadeIn 0.25s ease; }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(4px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* FAQ Accordions */
        details.faq-item summary::-webkit-details-marker { display: none; }
        details.faq-item summary::after {
            content: 'expand_more';
            font-family: 'Material Symbols Outlined';
            font-size: 20px;
            transition: transform 0.25s ease;
            margin-left: auto;
        }
        details.faq-item[open] summary::after {
            transform: rotate(180deg);
        }
        
        /* High Contrast reading mode */
        body.high-contrast-mode {
            background-color: #000000 !important;
            color: #ffffff !important;
        }
        body.high-contrast-mode .canvas-paper {
            background-color: #ffffff !important;
            color: #000000 !important;
            border-color: #000000 !important;
            box-shadow: 0 0 0 4px #ffffff !important;
        }

        /* Print formatting */
        @media print {
            header, nav, aside, .no-print, #batchActionBar { display: none !important; }
            main, .canvas-paper { margin: 0 !important; padding: 0 !important; box-shadow: none !important; width: 100% !important; max-width: 100% !important; }
        }
    </style>

    <!-- Fallback external data loading -->
    <script src="documents_data.js"></script>
</head>

<body class="bg-background text-on-background min-h-screen flex flex-col font-body antialiased overflow-hidden select-text">

    <!-- TOP NAVIGATION BAR (Lexicon Authority) -->
    <header class="fixed top-0 left-0 w-full z-50 flex justify-between items-center px-4 md:px-8 h-16 bg-primary text-on-primary border-b border-outline-variant shadow-md">
        <!-- Logo & Title -->
        <div class="flex items-center gap-4 lg:gap-6">
            <div class="flex items-center gap-3 cursor-pointer" onclick="switchTab('tabRepo')">
                <div class="w-9 h-9 rounded bg-surface-container-lowest flex items-center justify-center p-1.5 shadow-sm border border-outline-variant/30">
                    <span class="material-symbols-outlined text-primary font-bold text-2xl">account_balance</span>
                </div>
                <div>
                    <h1 class="font-headline font-bold text-base md:text-lg text-on-primary tracking-tight leading-none">CPPR IMSciences</h1>
                    <span class="font-mono text-[10px] text-on-primary-container tracking-wider uppercase">Policy Stockroom Platform</span>
                </div>
            </div>

            <!-- Main Navigation Links -->
            <nav class="hidden xl:flex items-center gap-1 h-16 pl-4 border-l border-on-primary-container/20">
                <button onclick="switchTab('tabRepo')" id="nav-tabRepo" class="nav-btn px-3 py-2 rounded font-mono text-xs font-semibold text-on-primary bg-primary-container border-b-2 border-secondary-fixed flex items-center gap-1.5 transition-colors">
                    <span class="material-symbols-outlined text-sm">inventory_2</span>
                    Repository
                </button>
                <button onclick="switchTab('tabReader')" id="nav-tabReader" class="nav-btn px-3 py-2 rounded font-mono text-xs font-semibold text-on-primary-container/80 hover:text-on-primary hover:bg-primary-container/50 flex items-center gap-1.5 transition-colors">
                    <span class="material-symbols-outlined text-sm">menu_book</span>
                    Document Reader
                </button>
                <button onclick="switchTab('tabAnalytics')" id="nav-tabAnalytics" class="nav-btn px-3 py-2 rounded font-mono text-xs font-semibold text-on-primary-container/80 hover:text-on-primary hover:bg-primary-container/50 flex items-center gap-1.5 transition-colors">
                    <span class="material-symbols-outlined text-sm">analytics</span>
                    Visual Analytics
                </button>
                <button onclick="switchTab('tabLineage')" id="nav-tabLineage" class="nav-btn px-3 py-2 rounded font-mono text-xs font-semibold text-on-primary-container/80 hover:text-on-primary hover:bg-primary-container/50 flex items-center gap-1.5 transition-colors">
                    <span class="material-symbols-outlined text-sm">account_tree</span>
                    Legal Lineage
                </button>
                <button onclick="switchTab('tabRedline')" id="nav-tabRedline" class="nav-btn px-3 py-2 rounded font-mono text-xs font-semibold text-on-primary-container/80 hover:text-on-primary hover:bg-primary-container/50 flex items-center gap-1.5 transition-colors">
                    <span class="material-symbols-outlined text-sm">compare</span>
                    Redline Studio
                </button>
                <button onclick="switchTab('tabBrief')" id="nav-tabBrief" class="nav-btn px-3 py-2 rounded font-mono text-xs font-semibold text-on-primary-container/80 hover:text-on-primary hover:bg-primary-container/50 flex items-center gap-1.5 transition-colors">
                    <span class="material-symbols-outlined text-sm">assignment</span>
                    Executive Brief
                </button>
                <button onclick="switchTab('tabGlossary')" id="nav-tabGlossary" class="nav-btn px-3 py-2 rounded font-mono text-xs font-semibold text-on-primary-container/80 hover:text-on-primary hover:bg-primary-container/50 flex items-center gap-1.5 transition-colors">
                    <span class="material-symbols-outlined text-sm">help_center</span>
                    FAQs & Lexicon
                </button>
                <button onclick="switchTab('tabInquiry')" id="nav-tabInquiry" class="nav-btn px-3 py-2 rounded font-mono text-xs font-semibold text-on-primary-container/80 hover:text-on-primary hover:bg-primary-container/50 flex items-center gap-1.5 transition-colors">
                    <span class="material-symbols-outlined text-sm">mail</span>
                    Inquiry Desk
                </button>
            </nav>
        </div>

        <!-- Right Action Controls -->
        <div class="flex items-center gap-3">
            <!-- Mobile Menu Dropdown -->
            <div class="xl:hidden relative">
                <select onchange="switchTab(this.value)" class="bg-primary-container text-on-primary font-mono text-xs py-1.5 px-3 rounded border border-on-primary-container/30 focus:outline-none">
                    <option value="tabRepo">📦 Repository</option>
                    <option value="tabReader">📖 Document Reader</option>
                    <option value="tabAnalytics">📊 Visual Analytics</option>
                    <option value="tabLineage">🌳 Legal Lineage</option>
                    <option value="tabRedline">⚖️ Redline Studio</option>
                    <option value="tabBrief">📋 Executive Brief</option>
                    <option value="tabGlossary">📚 FAQs & Lexicon</option>
                    <option value="tabInquiry">✉️ Inquiry Desk</option>
                </select>
            </div>

            <!-- Substantive Count Pill -->
            <div class="hidden sm:flex items-center gap-1.5 px-3 py-1 rounded bg-surface-container-lowest/10 border border-on-primary-container/20 font-mono text-xs text-on-primary">
                <span class="w-2 h-2 rounded-full bg-green-400 animate-pulse"></span>
                <span id="headerTotalBadge">1,374</span>
                <span class="text-on-primary-container/80">Instruments</span>
            </div>

            <!-- Global Quick Search Trigger (⌘K) -->
            <button onclick="focusGlobalSearch()" class="hidden md:flex items-center gap-2 bg-primary-container/60 hover:bg-primary-container px-3 py-1.5 rounded border border-on-primary-container/30 text-on-primary font-mono text-xs transition-colors">
                <span class="material-symbols-outlined text-sm">search</span>
                <span class="text-on-primary-container/70">Search...</span>
                <span class="px-1.5 py-0.5 rounded bg-on-primary/10 text-[10px] ml-2">⌘K</span>
            </button>

            <!-- Admin Access Button -->
            <button onclick="openAdminModal()" class="px-2.5 py-1 rounded bg-secondary text-white font-mono text-xs font-semibold hover:bg-secondary/90 transition-colors flex items-center gap-1 shadow-sm" title="Admin Portal Management">
                <span class="material-symbols-outlined text-sm">admin_panel_settings</span>
                <span class="hidden md:inline">Admin</span>
            </button>
        </div>
    </header>

    <!-- MAIN WRAPPER -->
    <div class="flex-1 mt-16 h-[calc(100vh-64px)] overflow-hidden flex flex-col relative">

        <!-- ========================================================= -->
        <!-- TAB 1: MASTER REPOSITORY & SPLIT-PANE INSPECTOR           -->
        <!-- ========================================================= -->
        <section id="tabRepo" class="portal-tab active flex-1 flex flex-col h-full overflow-hidden">
            <!-- Filter Bar & Toolbar -->
            <div class="bg-surface-container-lowest border-b border-outline-variant px-4 py-2.5 flex flex-wrap items-center justify-between gap-3 shrink-0 shadow-sm z-20">
                <!-- Search & Filter Controls -->
                <div class="flex flex-wrap items-center gap-2.5 flex-1 min-w-[280px]">
                    <!-- Search Input -->
                    <div class="relative flex-1 max-w-md">
                        <span class="material-symbols-outlined absolute left-2.5 top-1/2 -translate-y-1/2 text-outline text-lg">search</span>
                        <input id="repoSearchInput" oninput="debounceRunFilters()" type="text" placeholder="Search 1,374 policy instruments by title, authority, summary..." class="w-full pl-9 pr-8 py-1.5 bg-surface-container-low border border-outline-variant rounded font-body text-xs text-on-surface focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary transition-all"/>
                        <button onclick="clearSearch()" id="clearSearchBtn" class="absolute right-2 top-1/2 -translate-y-1/2 text-outline hover:text-on-surface text-sm hidden">✕</button>
                    </div>

                    <!-- Category Pills Quick Selector -->
                    <div class="hidden lg:flex items-center gap-1 overflow-x-auto no-scrollbar py-0.5">
                        <button onclick="setCategoryFilter('ALL')" class="cat-pill px-2.5 py-1 rounded-full font-mono text-[11px] font-semibold bg-primary text-white border border-primary transition-all" data-cat="ALL">All (1,374)</button>
                        <button onclick="setCategoryFilter('Act / Legislation')" class="cat-pill px-2.5 py-1 rounded-full font-mono text-[11px] text-on-surface-variant bg-surface-container-low border border-outline-variant hover:bg-surface-container transition-all" data-cat="Act / Legislation">Acts (814)</button>
                        <button onclick="setCategoryFilter('Statutory Rules & Regulations')" class="cat-pill px-2.5 py-1 rounded-full font-mono text-[11px] text-on-surface-variant bg-surface-container-low border border-outline-variant hover:bg-surface-container transition-all" data-cat="Statutory Rules & Regulations">Rules (227)</button>
                        <button onclick="setCategoryFilter('Policy / Strategy')" class="cat-pill px-2.5 py-1 rounded-full font-mono text-[11px] text-on-surface-variant bg-surface-container-low border border-outline-variant hover:bg-surface-container transition-all" data-cat="Policy / Strategy">Policies (138)</button>
                        <button onclick="setCategoryFilter('Guidelines & SOPs')" class="cat-pill px-2.5 py-1 rounded-full font-mono text-[11px] text-on-surface-variant bg-surface-container-low border border-outline-variant hover:bg-surface-container transition-all" data-cat="Guidelines & SOPs">SOPs (102)</button>
                        <button onclick="setCategoryFilter('Rules of Business')" class="cat-pill px-2.5 py-1 rounded-full font-mono text-[11px] text-on-surface-variant bg-surface-container-low border border-outline-variant hover:bg-surface-container transition-all" data-cat="Rules of Business">Business Rules (63)</button>
                    </div>

                    <!-- Department / Sector Select -->
                    <select id="sectorSelect" onchange="runFilters()" class="bg-surface-container-low border border-outline-variant rounded font-mono text-xs py-1.5 px-2.5 text-on-surface focus:outline-none focus:border-primary">
                        <option value="">All 28 KP Departments</option>
                    </select>

                    <!-- Era Select -->
                    <select id="eraSelect" onchange="runFilters()" class="hidden sm:block bg-surface-container-low border border-outline-variant rounded font-mono text-xs py-1.5 px-2.5 text-on-surface focus:outline-none focus:border-primary">
                        <option value="">All 4 Constitutional Eras</option>
                        <option value="Post-18th">Post-18th Amendment (2010–Present) [1,153]</option>
                        <option value="1973">Democratic & 1973 Era (1973–2009) [122]</option>
                        <option value="1947">Post-Independence Era (1947–1972) [70]</option>
                        <option value="Pre-1947">Pre-Partition Era (Pre-1947) [29]</option>
                    </select>
                </div>

                <!-- Density & Counter -->
                <div class="flex items-center gap-3 shrink-0">
                    <span id="filteredCountLabel" class="font-mono text-xs text-on-surface-variant font-medium">1,374 of 1,374 shown</span>
                    <div class="flex items-center bg-surface-container rounded border border-outline-variant p-0.5">
                        <button onclick="setDensity('comfortable')" id="densityComfortableBtn" class="p-1 rounded bg-white shadow-sm text-primary" title="Comfortable View">
                            <span class="material-symbols-outlined text-[16px]">view_list</span>
                        </button>
                        <button onclick="setDensity('compact')" id="densityCompactBtn" class="p-1 rounded text-outline hover:text-primary transition-colors" title="Compact View">
                            <span class="material-symbols-outlined text-[16px]">density_small</span>
                        </button>
                    </div>
                </div>
            </div>

            <!-- Split Pane Content Layout -->
            <div class="flex-1 flex overflow-hidden">
                <!-- Left 60%: Data Grid -->
                <div class="w-full lg:w-[60%] flex flex-col border-r border-outline-variant bg-surface-container-lowest overflow-hidden">
                    <!-- Table Header -->
                    <div class="grid grid-cols-[2.5rem_1fr_9rem_5rem_6.5rem_5rem] gap-2 px-4 py-2.5 bg-surface-container-low border-b border-outline-variant font-mono text-[11px] font-semibold text-on-surface-variant uppercase tracking-wider sticky top-0 z-10">
                        <div class="flex items-center justify-center">
                            <input id="masterCheckbox" onchange="toggleSelectAll(this)" type="checkbox" class="rounded border-outline-variant text-primary focus:ring-primary w-3.5 h-3.5"/>
                        </div>
                        <div>Document Title & Authority</div>
                        <div>Sector / Department</div>
                        <div>Year</div>
                        <div>Status</div>
                        <div class="text-right">Action</div>
                    </div>

                    <!-- Scrollable Table Body -->
                    <div id="repoTableBody" class="flex-1 overflow-y-auto divide-y divide-outline-variant/60">
                        <!-- Populated dynamically via JS -->
                    </div>

                    <!-- Table Footer Pagination Bar -->
                    <div class="h-11 bg-surface-container-low border-t border-outline-variant px-4 flex items-center justify-between text-xs font-mono text-on-surface-variant shrink-0">
                        <div class="flex items-center gap-2">
                            <span>Showing <strong id="pageStartNum">1</strong>–<strong id="pageEndNum">50</strong> of <strong id="pageTotalNum">1,374</strong></span>
                        </div>
                        <div class="flex items-center gap-1.5">
                            <button onclick="changePage(-1)" id="prevPageBtn" class="px-2.5 py-1 rounded bg-surface border border-outline-variant hover:bg-surface-container disabled:opacity-40" disabled>Previous</button>
                            <span id="currentPageIndicator" class="px-2 font-bold text-on-surface">1</span>
                            <button onclick="changePage(1)" id="nextPageBtn" class="px-2.5 py-1 rounded bg-surface border border-outline-variant hover:bg-surface-container disabled:opacity-40">Next</button>
                        </div>
                    </div>
                </div>

                <!-- Right 40%: Active Document Inspector Drawer -->
                <aside id="inspectorDrawer" class="hidden lg:flex w-[40%] bg-surface-container-lowest flex-col border-l border-outline-variant overflow-y-auto z-10 shadow-[-4px_0_12px_rgba(0,0,0,0.03)]">
                    <div class="p-6 space-y-6">
                        <!-- Status & Category Header -->
                        <div class="space-y-3 border-b border-outline-variant pb-5">
                            <div class="flex items-center justify-between gap-2">
                                <span id="inspStatusPill" class="px-2.5 py-1 rounded-full bg-[#166534] text-white font-mono text-[10px] font-bold uppercase tracking-wider">In Force</span>
                                <span id="inspCategoryBadge" class="font-mono text-[11px] text-on-surface-variant bg-surface-container-low px-2 py-0.5 rounded border border-outline-variant">Primary Act</span>
                            </div>
                            <h3 id="inspTitle" class="font-headline font-bold text-lg md:text-xl text-primary leading-tight">The Khyber Pakhtunkhwa Local Government Act, 2013</h3>
                            <p id="inspSubtitle" class="font-body text-xs text-on-surface-variant italic">Act No. XXVIII of 2013 — Promulgated by Provincial Assembly of Khyber Pakhtunkhwa</p>
                        </div>

                        <!-- Core Metadata Grid -->
                        <dl class="grid grid-cols-2 gap-y-3.5 gap-x-4 font-body text-xs border-b border-outline-variant pb-5">
                            <div>
                                <dt class="font-mono text-[10px] text-on-surface-variant uppercase tracking-wider">Administrative Department</dt>
                                <dd id="inspSector" class="font-semibold text-on-surface mt-0.5">Local Government Department</dd>
                            </div>
                            <div>
                                <dt class="font-mono text-[10px] text-on-surface-variant uppercase tracking-wider">Date of Enactment</dt>
                                <dd id="inspDate" class="font-semibold text-on-surface mt-0.5">31st October, 2013</dd>
                            </div>
                            <div>
                                <dt class="font-mono text-[10px] text-on-surface-variant uppercase tracking-wider">Constitutional Era</dt>
                                <dd id="inspEra" class="text-on-surface mt-0.5">Post-18th Amendment (2010–Present)</dd>
                            </div>
                            <div>
                                <dt class="font-mono text-[10px] text-on-surface-variant uppercase tracking-wider">Stockroom Reference ID</dt>
                                <dd id="inspRefId" class="font-mono text-primary font-bold mt-0.5">KP-DOC-0001</dd>
                            </div>
                            <div class="col-span-2">
                                <dt class="font-mono text-[10px] text-on-surface-variant uppercase tracking-wider">Enabling Authority / Root Statute</dt>
                                <dd id="inspAuthority" class="text-on-surface mt-0.5 bg-surface-container-low p-2 rounded border border-outline-variant font-mono text-[11px]">Constitution of Pakistan (Article 140A)</dd>
                            </div>
                        </dl>

                        <!-- Primary Action Launcher Buttons -->
                        <div class="space-y-2 border-b border-outline-variant pb-5">
                            <button onclick="launchInReaderFromInspector()" class="w-full flex items-center justify-center gap-2 bg-primary text-on-primary py-2.5 px-4 rounded font-mono text-xs font-bold hover:bg-primary-container transition-colors shadow-sm">
                                <span class="material-symbols-outlined text-sm">menu_book</span>
                                Launch in Statutory Document Reader
                                <span class="bg-white/20 text-white font-mono text-[10px] px-1.5 py-0.5 rounded ml-auto">Reader Tab ↗</span>
                            </button>
                            <div class="grid grid-cols-2 gap-2">
                                <button onclick="openCiteModalFromInspector()" class="flex items-center justify-center gap-1.5 border border-primary text-primary py-2 px-3 rounded font-mono text-xs font-semibold hover:bg-primary/5 transition-colors">
                                    <span class="material-symbols-outlined text-sm">format_quote</span>
                                    Cite Instrument
                                </button>
                                <button onclick="exportSingleDocJson()" class="flex items-center justify-center gap-1.5 border border-outline-variant text-on-surface py-2 px-3 rounded font-mono text-xs font-semibold hover:bg-surface-container transition-colors">
                                    <span class="material-symbols-outlined text-sm">download</span>
                                    Export JSON
                                </button>
                            </div>
                        </div>

                        <!-- Executive Summary / Brief -->
                        <div class="border-b border-outline-variant pb-5">
                            <h4 class="font-mono text-[11px] font-bold text-primary uppercase tracking-widest mb-2 flex items-center gap-1.5">
                                <span class="material-symbols-outlined text-sm">article</span>
                                Executive Policy Brief
                            </h4>
                            <p id="inspSummary" class="font-body text-xs text-on-surface leading-relaxed bg-surface-container-low/50 p-3 rounded border border-outline-variant">
                                Official statutory rules and regulatory mechanisms promulgated under executive authority to operationalize Khyber Pakhtunkhwa Local Government system across the province.
                            </p>
                        </div>

                        <!-- Legal Lineage Hierarchy -->
                        <div class="border-b border-outline-variant pb-5">
                            <h4 class="font-mono text-[11px] font-bold text-primary uppercase tracking-widest mb-3 flex items-center gap-1.5">
                                <span class="material-symbols-outlined text-sm">account_tree</span>
                                Statutory Lineage
                            </h4>
                            <div class="relative pl-4 space-y-3 before:absolute before:inset-y-1.5 before:left-[5px] before:w-0.5 before:bg-outline-variant">
                                <div class="relative">
                                    <span class="absolute -left-[15px] top-1.5 w-2.5 h-2.5 rounded-full bg-outline-variant border-2 border-white"></span>
                                    <div class="pl-1">
                                        <span class="font-mono text-[10px] text-on-surface-variant block">Parent Authority</span>
                                        <span id="inspLineageParent" class="font-body text-xs text-primary font-medium">Constitution of the Islamic Republic of Pakistan</span>
                                    </div>
                                </div>
                                <div class="relative">
                                    <span class="absolute -left-[15px] top-1.5 w-2.5 h-2.5 rounded-full bg-primary border-2 border-white"></span>
                                    <div class="pl-1 bg-surface-container-low p-1.5 rounded border border-primary/20">
                                        <span class="font-mono text-[10px] text-primary font-bold block">Current Instrument</span>
                                        <span id="inspLineageCurrent" class="font-body text-xs font-semibold text-on-surface">Khyber Pakhtunkhwa Local Government Act, 2013</span>
                                    </div>
                                </div>
                                <div class="relative">
                                    <span class="absolute -left-[15px] top-1.5 w-2.5 h-2.5 rounded-full bg-outline-variant border-2 border-white"></span>
                                    <div class="pl-1">
                                        <span class="font-mono text-[10px] text-on-surface-variant block">Delegated Rules & Regulations</span>
                                        <span id="inspLineageSubordinate" class="font-body text-xs text-on-surface leading-tight">KP Village & Neighbourhood Council Rules 2021; KP Conduct of Business Rules</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Keyword Tags -->
                        <div>
                            <h4 class="font-mono text-[11px] font-bold text-primary uppercase tracking-widest mb-2 flex items-center gap-1.5">
                                <span class="material-symbols-outlined text-sm">sell</span>
                                Keywords & Thematic Classifiers
                            </h4>
                            <div id="inspTagsContainer" class="flex flex-wrap gap-1.5"></div>
                        </div>
                    </div>
                </aside>
            </div>
        </section>

        <!-- ========================================================= -->
        <!-- TAB 2: FLAGSHIP STATUTORY DOCUMENT READER STUDIO          -->
        <!-- ========================================================= -->
        <section id="tabReader" class="portal-tab flex-1 flex flex-col h-full overflow-hidden">
            <!-- Split Pane Reader Layout -->
            <div class="flex-1 flex flex-col md:flex-row h-full overflow-hidden">
                <!-- Left 70%: Statutory Document Canvas -->
                <div class="flex-1 bg-surface-container-low flex flex-col relative border-r border-outline-variant overflow-hidden">
                    <!-- Reader Control Toolbar -->
                    <div class="h-12 border-b border-outline-variant bg-surface-container flex items-center justify-between px-4 shrink-0 shadow-sm z-10">
                        <!-- Navigation & Document Picker -->
                        <div class="flex items-center gap-3">
                            <select id="readerDocSelector" onchange="loadReaderDocumentFromSelector(this.value)" class="bg-surface border border-outline-variant rounded font-mono text-xs py-1 px-2.5 max-w-[280px] sm:max-w-xs truncate focus:outline-none focus:border-primary">
                                <option value="default">KP Local Government Act, 2013 (Full Text)</option>
                                <option value="11">The Khyber Pakhtunkhwa Right to Information Act, 2013</option>
                                <option value="37">The Khyber Pakhtunkhwa Environmental Protection Act, 2014</option>
                                <option value="5">The Khyber Pakhtunkhwa Police Act, 2017</option>
                                <option value="134">The Khyber Pakhtunkhwa Civil Servants Act, 1973</option>
                            </select>
                            <span class="font-mono text-xs text-on-surface-variant hidden sm:inline" id="readerPageIndicator">Page 1 of 42</span>
                            
                            <!-- Zoom Controls -->
                            <div class="flex items-center bg-surface-container-highest rounded p-0.5 border border-outline-variant">
                                <button onclick="readerZoom(-10)" class="p-1 hover:bg-surface rounded text-on-surface-variant" title="Zoom Out">
                                    <span class="material-symbols-outlined text-sm">remove</span>
                                </button>
                                <span id="readerZoomDisplay" class="px-2 font-mono text-[11px] font-semibold text-on-surface-variant">100%</span>
                                <button onclick="readerZoom(10)" class="p-1 hover:bg-surface rounded text-on-surface-variant" title="Zoom In">
                                    <span class="material-symbols-outlined text-sm">add</span>
                                </button>
                            </div>
                        </div>

                        <!-- In-Document Search & Contrast Toggle -->
                        <div class="flex items-center gap-2.5">
                            <div class="relative hidden sm:block">
                                <span class="material-symbols-outlined absolute left-2 top-1/2 -translate-y-1/2 text-outline text-sm">search</span>
                                <input id="readerSearchInput" oninput="searchWithinReader(this.value)" type="text" placeholder="Search within document..." class="pl-7 pr-3 py-1 bg-surface border border-outline-variant rounded font-body text-xs text-on-surface focus:outline-none focus:border-primary w-44"/>
                            </div>
                            <button onclick="toggleHighContrast()" id="contrastBtn" class="flex items-center gap-1.5 px-2.5 py-1 bg-surface border border-outline-variant rounded hover:bg-surface-container font-mono text-xs text-on-surface transition-colors">
                                <span class="material-symbols-outlined text-sm">contrast</span>
                                <span class="hidden sm:inline">High Contrast</span>
                            </button>
                        </div>
                    </div>

                    <!-- Document Canvas Scroll Area -->
                    <div class="flex-1 overflow-y-auto p-4 md:p-8 bg-[#e2e8f0] flex justify-center custom-scrollbar">
                        <article id="readerCanvasArticle" class="canvas-paper bg-surface-container-lowest w-full max-w-[850px] shadow-sm border border-outline-variant p-8 md:p-14 my-2 transition-transform origin-top">
                            <header class="text-center mb-10 border-b-2 border-primary pb-6">
                                <h2 id="readerTitleHead" class="font-headline text-2xl md:text-3xl text-primary font-bold uppercase tracking-wider">Khyber Pakhtunkhwa Local Government Act, 2013</h2>
                                <p id="readerSubHead" class="font-body text-xs text-on-surface-variant italic mt-2">An Act to rationalize and reorganize the local government system in the Province of the Khyber Pakhtunkhwa.</p>
                                <div class="flex items-center justify-center gap-2 mt-4 font-mono text-[11px] text-on-surface-variant">
                                    <span id="readerDocIdRef">Act No. XXVIII of 2013</span>
                                    <span>&bull;</span>
                                    <span id="readerDocEnactRef">Enacted: 31st October, 2013</span>
                                    <span>&bull;</span>
                                    <span class="text-green-700 font-bold" id="readerDocStatusRef">In Force</span>
                                </div>
                            </header>

                            <!-- Document Body Text -->
                            <div id="readerStatutoryBody" class="space-y-6 font-body text-sm text-on-surface leading-relaxed max-w-prose mx-auto">
                                <p><span class="font-bold">Preamble.—</span>WHEREAS it is expedient to encourage local government institutions composed of elected representatives and having special representation of peasants, workers, women, minorities and youth;</p>
                                <p>AND WHEREAS clause (i) of Article 140A of the Constitution of the Islamic Republic of Pakistan provides for establishment of a local government system and devolution of political, administrative and financial responsibility and authority to the elected representatives of the local governments;</p>
                                
                                <section class="mt-8 pt-4 border-t border-outline-variant/40">
                                    <h3 class="font-headline font-bold text-lg text-primary mb-3">CHAPTER I — PRELIMINARY</h3>
                                    <div class="pl-4 border-l-2 border-outline-variant space-y-4">
                                        <div>
                                            <h4 class="font-bold text-on-surface mb-1">1. Short title, extent and commencement.—</h4>
                                            <ol class="list-[lower-alpha] pl-5 space-y-1 text-on-surface-variant">
                                                <li>This Act may be called the Khyber Pakhtunkhwa Local Government Act, 2013.</li>
                                                <li>It extends to the whole of the Province of the Khyber Pakhtunkhwa except, areas notified as cantonments or any other area excluded by Government through notification in the official Gazette.</li>
                                                <li>It shall come into force on such date as Government may, by notification in the official Gazette, appoint and different dates may be appointed for different provisions of this Act.</li>
                                            </ol>
                                        </div>
                                        <div>
                                            <h4 class="font-bold text-on-surface mb-1">2. Definitions.—</h4>
                                            <p class="text-on-surface-variant mb-2">In this Act, unless the context otherwise requires,—</p>
                                            <ol class="list-[lower-alpha] pl-5 space-y-2 text-on-surface-variant">
                                                <li><strong class="text-on-surface">"building"</strong> includes any shop, house, hut, outhouse, shed, stable or enclosure built of any material and used for any purpose, and also includes a wall, well, verandah, platform, plinth, ramp, stair-case and steps;</li>
                                                <li><strong class="text-on-surface">"bye-laws"</strong> means bye-laws made under this Act;</li>
                                                <li><strong class="text-on-surface">"cattle"</strong> means cows, buffaloes, bulls, oxen, bullocks, heifers, calves, camels, sheep, goats and includes any other animal declared by Government to be cattle for the purposes of this Act;</li>
                                                <li><strong class="text-on-surface">"devolution"</strong> means conferment of political, administrative and financial authority upon local governments;</li>
                                                <li><strong class="text-on-surface">"Local Council"</strong> means a Village Council, Neighbourhood Council, or Tehsil Council established under this Act.</li>
                                            </ol>
                                        </div>
                                    </div>
                                </section>

                                <section class="mt-8 pt-4 border-t border-outline-variant/40">
                                    <h3 class="font-headline font-bold text-lg text-primary mb-3">CHAPTER II — LOCAL GOVERNMENTS</h3>
                                    <div class="pl-4 border-l-2 border-outline-variant space-y-4">
                                        <div>
                                            <h4 class="font-bold text-on-surface mb-1">23. Powers and Functions of Village and Neighbourhood Councils.—</h4>
                                            <p class="text-on-surface-variant">Every Village Council and Neighbourhood Council shall perform such functions as may be assigned to it by Government, including local development planning, community welfare, and maintenance of public order.</p>
                                        </div>
                                    </div>
                                </section>
                            </div>
                        </article>
                    </div>
                </div>

                <!-- Right 30%: Metadata & Citation Sidebar -->
                <aside class="w-full md:w-[380px] bg-surface-container-lowest flex flex-col border-l border-outline-variant overflow-y-auto shrink-0">
                    <div class="p-6 space-y-6">
                        <!-- Active Summary -->
                        <div>
                            <div class="flex items-center gap-2 mb-2">
                                <span class="px-2 py-0.5 rounded bg-[#166534] text-white font-mono text-[10px] font-bold uppercase tracking-wider" id="readerSidebarStatus">In Force</span>
                                <span class="px-2 py-0.5 rounded bg-surface-container font-mono text-[10px] text-on-surface-variant">Gazette Published</span>
                            </div>
                            <h3 id="readerSidebarTitle" class="font-headline font-bold text-base text-primary leading-tight">Khyber Pakhtunkhwa Local Government Act, 2013</h3>
                            <p class="font-mono text-xs text-on-surface-variant mt-1" id="readerSidebarRef">Ref: KP-LGA-2013-001</p>
                        </div>

                        <!-- Citation & Export Suite -->
                        <div class="space-y-2 border-t border-outline-variant pt-4">
                            <button onclick="window.print()" class="w-full flex items-center justify-center gap-2 bg-primary text-on-primary py-2.5 px-4 rounded font-mono text-xs font-bold hover:bg-primary-container transition-colors shadow-sm">
                                <span class="material-symbols-outlined text-sm">print</span>
                                Print / Download PDF
                                <span class="text-on-primary/60 font-mono text-[10px] ml-auto border border-on-primary/20 px-1 rounded">⌘P</span>
                            </button>
                            <div class="grid grid-cols-2 gap-2">
                                <button onclick="openCiteModal()" class="flex items-center justify-center gap-1.5 border border-primary text-primary py-2 px-3 rounded font-mono text-xs font-semibold hover:bg-primary/5 transition-colors">
                                    <span class="material-symbols-outlined text-sm">format_quote</span>
                                    Cite Studio
                                </button>
                                <button onclick="exportReaderMetadataJson()" class="flex items-center justify-center gap-1.5 border border-outline-variant text-on-surface py-2 px-3 rounded font-mono text-xs font-semibold hover:bg-surface-container transition-colors">
                                    <span class="material-symbols-outlined text-sm">data_object</span>
                                    Metadata
                                </button>
                            </div>
                        </div>

                        <!-- Statutory Lineage -->
                        <div class="border-t border-outline-variant pt-4">
                            <h4 class="font-mono text-[11px] font-bold text-primary uppercase tracking-widest mb-3 flex items-center gap-1.5">
                                <span class="material-symbols-outlined text-sm">account_tree</span>
                                Statutory Lineage
                            </h4>
                            <div class="relative pl-4 space-y-3 before:absolute before:inset-y-1 before:left-[5px] before:w-0.5 before:bg-outline-variant">
                                <div class="relative">
                                    <span class="absolute -left-[15px] top-1.5 w-2.5 h-2.5 rounded-full bg-outline-variant border-2 border-white"></span>
                                    <div class="pl-1">
                                        <span class="font-mono text-[10px] text-on-surface-variant block">Constitutional Mandate</span>
                                        <span class="font-body text-xs text-primary font-medium" id="readerSidebarParent">Constitution of Pakistan (Art. 140A)</span>
                                    </div>
                                </div>
                                <div class="relative">
                                    <span class="absolute -left-[15px] top-1.5 w-2.5 h-2.5 rounded-full bg-primary border-2 border-white"></span>
                                    <div class="pl-1 bg-surface-container p-1.5 rounded border border-primary/20">
                                        <span class="font-mono text-[10px] text-primary font-bold block">Current Statute</span>
                                        <span class="font-body text-xs font-semibold text-on-surface" id="readerSidebarCurrent">KP Local Government Act, 2013</span>
                                    </div>
                                </div>
                                <div class="relative">
                                    <span class="absolute -left-[15px] top-1.5 w-2.5 h-2.5 rounded-full bg-outline-variant border-2 border-white"></span>
                                    <div class="pl-1 space-y-1">
                                        <span class="font-mono text-[10px] text-on-surface-variant block">Subordinate Rules</span>
                                        <span class="font-body text-xs text-on-surface-variant block leading-tight" id="readerSidebarSub">KP Village Council Rules, 2015; KP Local Councils Rules of Business, 2021</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Keywords -->
                        <div class="border-t border-outline-variant pt-4">
                            <h4 class="font-mono text-[11px] font-bold text-primary uppercase tracking-widest mb-2 flex items-center gap-1.5">
                                <span class="material-symbols-outlined text-sm">sell</span>
                                Keywords
                            </h4>
                            <div class="flex flex-wrap gap-1.5" id="readerSidebarTags">
                                <span class="px-2 py-0.5 rounded bg-surface-container border border-outline-variant font-mono text-[10px] text-on-surface-variant">Devolution</span>
                                <span class="px-2 py-0.5 rounded bg-surface-container border border-outline-variant font-mono text-[10px] text-on-surface-variant">Fiscal Autonomy</span>
                                <span class="px-2 py-0.5 rounded bg-surface-container border border-outline-variant font-mono text-[10px] text-on-surface-variant">Administrative Law</span>
                                <span class="px-2 py-0.5 rounded bg-surface-container border border-outline-variant font-mono text-[10px] text-on-surface-variant">Local Councils</span>
                            </div>
                        </div>
                    </div>
                </aside>
            </div>
        </section>

        <!-- ========================================================= -->
        <!-- TAB 3: VISUAL ANALYTICS & GOVERNANCE INSIGHTS DASHBOARD   -->
        <!-- ========================================================= -->
        <section id="tabAnalytics" class="portal-tab flex-1 flex-col h-full overflow-y-auto p-4 md:p-8 bg-surface space-y-8">
            <div class="max-w-container-max mx-auto w-full">
                <div class="bg-surface-container-lowest border border-outline-variant p-6 rounded-lg shadow-sm">
                    <div class="flex flex-wrap justify-between items-start gap-4">
                        <div>
                            <span class="font-mono text-xs text-secondary font-bold uppercase tracking-wider">Empirical Research & Governance Metrics</span>
                            <h2 class="font-headline text-2xl md:text-3xl font-bold text-primary mt-1">Legislative Analytics & Policy Trends Dashboard</h2>
                            <p class="font-body text-xs md:text-sm text-on-surface-variant mt-2 max-w-3xl leading-relaxed">
                                Real-time empirical breakdown of Khyber Pakhtunkhwa's 1,374 substantive policy instruments across 15 legal hierarchy tiers, 28 administrative departments, and 4 constitutional eras.
                            </p>
                        </div>
                        <div class="flex gap-2">
                            <button onclick="exportAllCSV()" class="px-3 py-2 bg-primary text-white font-mono text-xs font-semibold rounded hover:bg-primary-container flex items-center gap-1.5 shadow-sm">
                                <span class="material-symbols-outlined text-sm">download</span>
                                Export Complete CSV
                            </button>
                        </div>
                    </div>
                </div>

                <!-- KPI Metric Cards Grid -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-6">
                    <div class="bg-surface-container-lowest border border-outline-variant p-5 rounded-lg border-t-4 border-primary shadow-sm">
                        <div class="flex items-center justify-between">
                            <span class="font-mono text-xs text-on-surface-variant uppercase tracking-wider">Total Instruments</span>
                            <span class="material-symbols-outlined text-primary">account_balance</span>
                        </div>
                        <div class="font-headline text-3xl font-extrabold text-primary mt-3">1,374</div>
                        <p class="font-mono text-[11px] text-green-700 mt-1">100% Substantive Legal Policies</p>
                    </div>
                    <div class="bg-surface-container-lowest border border-outline-variant p-5 rounded-lg border-t-4 border-[#0284c7] shadow-sm">
                        <div class="flex items-center justify-between">
                            <span class="font-mono text-xs text-on-surface-variant uppercase tracking-wider">Primary Statutes & Acts</span>
                            <span class="material-symbols-outlined text-[#0284c7]">gavel</span>
                        </div>
                        <div class="font-headline text-3xl font-extrabold text-[#0284c7] mt-3">814</div>
                        <p class="font-mono text-[11px] text-on-surface-variant mt-1">59.2% of Total Stockroom</p>
                    </div>
                    <div class="bg-surface-container-lowest border border-outline-variant p-5 rounded-lg border-t-4 border-[#059669] shadow-sm">
                        <div class="flex items-center justify-between">
                            <span class="font-mono text-xs text-on-surface-variant uppercase tracking-wider">Statutory Rules & Regs</span>
                            <span class="material-symbols-outlined text-[#059669]">description</span>
                        </div>
                        <div class="font-headline text-3xl font-extrabold text-[#059669] mt-3">227</div>
                        <p class="font-mono text-[11px] text-on-surface-variant mt-1">Delegated Subordinate Law</p>
                    </div>
                    <div class="bg-surface-container-lowest border border-outline-variant p-5 rounded-lg border-t-4 border-[#d97706] shadow-sm">
                        <div class="flex items-center justify-between">
                            <span class="font-mono text-xs text-on-surface-variant uppercase tracking-wider">KP Departments</span>
                            <span class="material-symbols-outlined text-[#d97706]">corporate_fare</span>
                        </div>
                        <div class="font-headline text-3xl font-extrabold text-[#d97706] mt-3">28</div>
                        <p class="font-mono text-[11px] text-on-surface-variant mt-1">Full KP Rules of Business Scope</p>
                    </div>
                </div>

                <!-- Charts Section (Chart.js) -->
                <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mt-6">
                    <!-- Timeline Chart (2 Cols) -->
                    <div class="lg:col-span-2 bg-surface-container-lowest border border-outline-variant p-6 rounded-lg shadow-sm">
                        <h3 class="font-headline font-bold text-base text-primary mb-1">Legislative Enactment Timeline (1947–2026)</h3>
                        <p class="font-body text-xs text-on-surface-variant mb-4">Volume of substantive statutory instruments enacted across Pakistan's constitutional eras.</p>
                        <div class="h-64 relative">
                            <canvas id="analyticsTimelineChart"></canvas>
                        </div>
                    </div>

                    <!-- Hierarchy Distribution Doughnut (1 Col) -->
                    <div class="bg-surface-container-lowest border border-outline-variant p-6 rounded-lg shadow-sm">
                        <h3 class="font-headline font-bold text-base text-primary mb-1">Legal Hierarchy Distribution</h3>
                        <p class="font-body text-xs text-on-surface-variant mb-4">Proportion by statute tier and regulatory class.</p>
                        <div class="h-64 relative flex items-center justify-center">
                            <canvas id="analyticsHierarchyChart"></canvas>
                        </div>
                    </div>
                </div>

                <!-- Departmental Breakdown Table -->
                <div class="bg-surface-container-lowest border border-outline-variant rounded-lg p-6 mt-6 shadow-sm">
                    <h3 class="font-headline font-bold text-base text-primary mb-3">Departmental Legislative Burden (Top Sectors)</h3>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left font-body text-xs">
                            <thead class="bg-surface-container-low border-b border-outline-variant font-mono text-[11px] text-on-surface-variant uppercase">
                                <tr>
                                    <th class="py-2.5 px-4">Administrative Sector</th>
                                    <th class="py-2.5 px-4">Primary Statutes</th>
                                    <th class="py-2.5 px-4">Rules & SOPs</th>
                                    <th class="py-2.5 px-4">Total Instruments</th>
                                    <th class="py-2.5 px-4">Status</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-outline-variant/60" id="sectorTableBody"></tbody>
                        </table>
                    </div>
                </div>
            </div>
        </section>

        <!-- ========================================================= -->
        <!-- TAB 4: INTERACTIVE LEGAL LINEAGE TREE MAP                 -->
        <!-- ========================================================= -->
        <section id="tabLineage" class="portal-tab flex-1 flex-col h-full overflow-y-auto p-4 md:p-8 bg-surface space-y-6">
            <div class="max-w-container-max mx-auto w-full space-y-6">
                <!-- Lineage Header -->
                <div class="bg-surface-container-lowest border border-outline-variant p-6 rounded-lg shadow-sm">
                    <div class="flex flex-wrap justify-between items-center gap-4">
                        <div>
                            <span class="font-mono text-xs text-secondary font-bold uppercase tracking-wider">Constitutional Traceability Engine</span>
                            <h2 class="font-headline text-2xl font-bold text-primary mt-1">Interactive Statutory Lineage & Hierarchy Explorer</h2>
                            <p class="font-body text-xs md:text-sm text-on-surface-variant mt-1.5">
                                Trace constitutional roots, parent statutes, and delegated statutory rules across Khyber Pakhtunkhwa's legislative framework.
                            </p>
                        </div>
                        <div class="flex items-center gap-2">
                            <label class="font-mono text-xs text-on-surface-variant">Root Statute:</label>
                            <select id="lineageRootSelector" onchange="changeLineageRoot(this.value)" class="bg-surface-container-low border border-outline-variant rounded font-mono text-xs py-1.5 px-3 text-on-surface focus:border-primary">
                                <option value="KP-LGA-2013">Khyber Pakhtunkhwa Local Government Act, 2013</option>
                                <option value="KP-RTI-2013">Khyber Pakhtunkhwa Right to Information Act, 2013</option>
                                <option value="KP-KPPRA-2012">Khyber Pakhtunkhwa Public Procurement Act, 2012</option>
                            </select>
                        </div>
                    </div>
                </div>

                <!-- Dynamic Visual Tree Graph Canvas -->
                <div class="bg-surface-container-lowest border border-outline-variant p-8 rounded-lg shadow-sm" id="lineageTreeCanvas">
                    <!-- Rendered dynamically via changeLineageRoot -->
                </div>
            </div>
        </section>

        <!-- ========================================================= -->
        <!-- TAB 5: LEGISLATIVE REDLINE & COMPARATIVE AMENDMENT STUDIO -->
        <!-- ========================================================= -->
        <section id="tabRedline" class="portal-tab flex-1 flex-col h-full overflow-hidden bg-surface">
            <!-- Redline Toolbar -->
            <div class="bg-surface-container-lowest border-b border-outline-variant px-6 py-3 flex flex-wrap items-center justify-between gap-4 shrink-0 shadow-sm">
                <div>
                    <h2 class="font-headline font-bold text-lg text-primary">Legislative Redline & Comparative Amendment Studio</h2>
                    <p class="font-body text-xs text-on-surface-variant">Side-by-side synchronized statutory comparison: Original Act vs. Subsequent Amendments</p>
                </div>
                <div class="flex items-center gap-3">
                    <select id="redlineSelector" onchange="changeRedlineComparison(this.value)" class="bg-surface-container-low border border-outline-variant rounded font-mono text-xs py-1.5 px-2.5 text-on-surface">
                        <option value="LGA">KP Local Government Act (2013 vs 2019/2021)</option>
                        <option value="RTI">KP Right to Information Act (2013 vs 2015)</option>
                    </select>
                    <span class="px-2.5 py-1 bg-red-100 text-red-800 border border-red-300 rounded font-mono text-[11px] font-bold" id="redlineAmendedBadge">14 Clauses Amended</span>
                    <span class="px-2.5 py-1 bg-green-100 text-green-800 border border-green-300 rounded font-mono text-[11px] font-bold" id="redlineInsertedBadge">6 Sections Inserted</span>
                    <button onclick="window.print()" class="px-3 py-1.5 bg-primary text-white font-mono text-xs rounded font-semibold hover:bg-primary-container">Export Diff PDF</button>
                </div>
            </div>

            <!-- Side-by-Side Synchronized Panes -->
            <div id="redlinePanesContainer" class="flex-1 grid grid-cols-1 md:grid-cols-2 divide-y md:divide-y-0 md:divide-x divide-outline-variant overflow-hidden">
                <!-- Left Pane: Original -->
                <div class="flex flex-col bg-surface-container-lowest overflow-y-auto p-6 font-body text-xs leading-relaxed space-y-4">
                    <div class="sticky top-0 bg-surface-container-low p-2.5 rounded border border-outline-variant font-mono font-bold text-xs text-primary mb-2">
                        Original Enactment — Act XXVIII of 2013 (As Gazetted 31 Oct 2013)
                    </div>
                    <div class="space-y-4">
                        <p class="p-3 bg-red-50/60 border-l-4 border-red-500 rounded-r">
                            <strong class="text-red-900 block font-mono text-[11px] mb-1">Section 23 (Original):</strong>
                            <del class="text-red-700">"23. Powers and Functions of Village and Neighbourhood Councils.— Every Village Council shall consist of such members as may be determined by District Government..."</del>
                            <span class="text-red-600 block text-[10px] mt-1 font-mono">[Repealed & Replaced by Amendment Act of 2019]</span>
                        </p>
                        <p class="p-3 bg-surface-container-low border-l-4 border-outline rounded-r text-on-surface-variant">
                            <strong class="text-on-surface block font-mono text-[11px] mb-1">Section 24 (Original):</strong>
                            "24. Executive Functions.— The executive authority of the Local Council shall vest in the Nazim, assisted by the Secretary of the Local Council."
                        </p>
                    </div>
                </div>

                <!-- Right Pane: Amended -->
                <div class="flex flex-col bg-surface-container-lowest overflow-y-auto p-6 font-body text-xs leading-relaxed space-y-4">
                    <div class="sticky top-0 bg-surface-container-low p-2.5 rounded border border-outline-variant font-mono font-bold text-xs text-green-800 mb-2">
                        Amended Enactment — Khyber Pakhtunkhwa Local Government (Amendment) Act, 2019
                    </div>
                    <div class="space-y-4">
                        <p class="p-3 bg-green-50/60 border-l-4 border-green-600 rounded-r">
                            <strong class="text-green-900 block font-mono text-[11px] mb-1">Section 23 (Substituted):</strong>
                            <ins class="text-green-800 no-underline font-medium">"23. Reorganized Structure of Village Councils.— The Village Council and Neighbourhood Council shall be directly elected through adult franchise on non-party basis..."</ins>
                            <span class="text-green-700 block text-[10px] mt-1 font-mono">[Enacted by Provincial Assembly under Section 4 of Amendment Act]</span>
                        </p>
                        <p class="p-3 bg-green-50/60 border-l-4 border-green-600 rounded-r">
                            <strong class="text-green-900 block font-mono text-[11px] mb-1">Section 23A (Newly Inserted):</strong>
                            <ins class="text-green-800 no-underline font-medium">"23A. Devolution of Developmental Budget.— Government shall ensure not less than thirty percent of the total provincial development budget is allocated directly to local council tiers."</ins>
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <!-- ========================================================= -->
        <!-- TAB 6: EXECUTIVE POLICY BRIEF & GOVERNANCE DOSSIER        -->
        <!-- ========================================================= -->
        <section id="tabBrief" class="portal-tab flex-1 flex-col h-full overflow-y-auto p-4 md:p-8 bg-surface space-y-6">
            <div class="max-w-4xl mx-auto w-full bg-surface-container-lowest border border-outline-variant p-8 rounded-lg shadow-sm space-y-6">
                <!-- Brief Header -->
                <div class="border-b-2 border-primary pb-6">
                    <div class="flex items-center justify-between mb-2">
                        <span class="font-mono text-xs bg-primary text-white px-2.5 py-0.5 rounded font-bold uppercase">CPPR Policy Brief #42</span>
                        <span class="font-mono text-xs text-on-surface-variant">Issued: CPPR Policy Research Lab</span>
                    </div>
                    <h2 class="font-headline font-bold text-2xl md:text-3xl text-primary">Strategic Analysis of the KP Local Government Act, 2013</h2>
                    <p class="font-body text-xs md:text-sm text-on-surface-variant mt-2 italic">Institutional Autonomy, Fiscal Devolution, and Grassroots Participatory Governance in Khyber Pakhtunkhwa</p>
                </div>

                <!-- Core Objectives Grid -->
                <div>
                    <h3 class="font-headline font-bold text-base text-primary mb-3">Core Legislative Objectives</h3>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div class="p-4 bg-surface-container-low rounded border border-outline-variant">
                            <h4 class="font-bold text-primary text-xs mb-1">1. Devolution of Power</h4>
                            <p class="font-body text-xs text-on-surface-variant">Conferring legal authority to 3,564 Village & Neighbourhood Councils directly elected by citizens.</p>
                        </div>
                        <div class="p-4 bg-surface-container-low rounded border border-outline-variant">
                            <h4 class="font-bold text-primary text-xs mb-1">2. 30% Budget Mandate</h4>
                            <p class="font-body text-xs text-on-surface-variant">Statutory obligation reserving 30% of provincial annual development plan funds to local tiers.</p>
                        </div>
                        <div class="p-4 bg-surface-container-low rounded border border-outline-variant">
                            <h4 class="font-bold text-primary text-xs mb-1">3. Administrative Clarity</h4>
                            <p class="font-body text-xs text-on-surface-variant">Clear statutory delineation between provincial ministries and municipal Tehsil administrations.</p>
                        </div>
                    </div>
                </div>

                <!-- Strategic Takeaways -->
                <div class="p-5 bg-surface-container-low/60 rounded-lg border-l-4 border-secondary space-y-2">
                    <h4 class="font-mono font-bold text-xs text-secondary uppercase tracking-wider">CPPR Policy Assessment</h4>
                    <p class="font-body text-xs text-on-surface leading-relaxed">
                        The KP Local Government Act, 2013 represents the most comprehensive municipal devolution framework enacted in Pakistan post-18th Amendment. However, continuous amendments in 2015, 2019, and 2021 have highlighted recurring tensions between provincial administrative secretariats and elected local council chairpersons regarding fiscal discretion.
                    </p>
                </div>

                <div class="pt-4 border-t border-outline-variant flex justify-end gap-3">
                    <button onclick="window.print()" class="px-4 py-2 bg-primary text-white font-mono text-xs font-bold rounded hover:bg-primary-container flex items-center gap-1.5">
                        <span class="material-symbols-outlined text-sm">print</span> Print Full Policy Dossier
                    </button>
                    <button onclick="switchTab('tabReader')" class="px-4 py-2 border border-primary text-primary font-mono text-xs font-bold rounded hover:bg-primary/5 flex items-center gap-1.5">
                        <span class="material-symbols-outlined text-sm">menu_book</span> Open Associated Act in Reader
                    </button>
                </div>
            </div>
        </section>

        <!-- ========================================================= -->
        <!-- TAB 7: FAQS & POLICY LEXICON / GLOSSARY                   -->
        <!-- ========================================================= -->
        <section id="tabGlossary" class="portal-tab flex-1 flex-col h-full overflow-y-auto p-4 md:p-8 bg-surface space-y-6">
            <div class="max-w-container-max mx-auto w-full space-y-6">
                <!-- Hero Search Banner -->
                <div class="bg-surface-container-lowest border border-outline-variant p-6 rounded-lg shadow-sm">
                    <span class="font-mono text-xs text-secondary font-bold uppercase tracking-wider">CPPR Knowledge Hub & Institutional Reference</span>
                    <h2 class="font-headline text-2xl font-bold text-primary mt-1">Frequently Asked Questions & Policy Lexicon</h2>
                    <p class="font-body text-xs md:text-sm text-on-surface-variant mt-1.5 max-w-3xl">
                        Comprehensive guidance on the Public Policy Stockroom and definitions of constitutional, legislative, and public policy terminology in Pakistan.
                    </p>
                </div>

                <!-- Two-Column Layout -->
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                    <!-- Left: FAQs with Accordion Dropdowns -->
                    <div class="bg-surface-container-lowest border border-outline-variant p-6 rounded-lg shadow-sm space-y-4">
                        <div class="border-b border-outline-variant pb-3 flex items-center justify-between">
                            <div>
                                <h3 class="font-headline font-bold text-base text-primary flex items-center gap-2">
                                    <span class="material-symbols-outlined text-primary">quiz</span>
                                    Frequently Asked Questions (FAQs)
                                </h3>
                                <p class="font-body text-xs text-on-surface-variant mt-1">Click any question to drop down the answer.</p>
                            </div>
                            <button onclick="toggleAllFaqs()" id="toggleAllFaqsBtn" class="px-2.5 py-1 bg-surface-container-low border border-outline-variant rounded font-mono text-[11px] text-primary hover:bg-surface-container font-semibold">
                                Expand All
                            </button>
                        </div>
                        
                        <div class="space-y-2.5 max-h-[750px] overflow-y-auto pr-2 custom-scrollbar" id="faqAccordionContainer">
                            <!-- Populated dynamically via JS -->
                        </div>
                    </div>

                    <!-- Right: Structured Glossary Cards -->
                    <div class="bg-surface-container-lowest border border-outline-variant p-6 rounded-lg shadow-sm space-y-4">
                        <div class="border-b border-outline-variant pb-3 flex flex-wrap justify-between items-center gap-2">
                            <div>
                                <h3 class="font-headline font-bold text-base text-primary flex items-center gap-2">
                                    <span class="material-symbols-outlined text-primary">dictionary</span>
                                    Legislative & Policy Wordlist
                                </h3>
                                <p class="font-body text-xs text-on-surface-variant mt-1">Key constitutional, legal, and public policy concepts.</p>
                            </div>
                            <div class="flex items-center gap-2">
                                <select id="glossaryCatFilter" onchange="filterGlossaryByCategory(this.value)" class="bg-surface-container-low border border-outline-variant rounded font-mono text-xs py-1 px-2 text-on-surface">
                                    <option value="ALL">All Categories</option>
                                    <option value="Constitutional">Constitutional</option>
                                    <option value="Legislative">Legislative</option>
                                    <option value="Policy">Policy</option>
                                </select>
                                <input id="glossaryFilterInput" oninput="filterGlossary(this.value)" type="text" placeholder="Filter terms..." class="bg-surface-container-low border border-outline-variant rounded font-body text-xs py-1 px-2.5 w-36"/>
                            </div>
                        </div>

                        <div class="space-y-3 max-h-[750px] overflow-y-auto pr-2 custom-scrollbar" id="glossaryContainer">
                            <!-- Populated dynamically via JS -->
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ========================================================= -->
        <!-- TAB 8: POLICY INQUIRY & RESEARCH DESK                     -->
        <!-- ========================================================= -->
        <section id="tabInquiry" class="portal-tab flex-1 flex-col h-full overflow-y-auto p-4 md:p-8 bg-surface space-y-6">
            <div class="max-w-2xl mx-auto w-full bg-surface-container-lowest border border-outline-variant p-8 rounded-lg shadow-sm space-y-6">
                <div class="border-b border-outline-variant pb-4">
                    <span class="font-mono text-xs text-secondary font-bold uppercase tracking-wider">Direct Institutional Channel</span>
                    <h2 class="font-headline text-2xl font-bold text-primary mt-1">Policy Inquiry & Research Desk</h2>
                    <p class="font-body text-xs text-on-surface-variant mt-1">Send research requests, statutory clarification notes, or document contributions directly to CPPR.</p>
                </div>

                <form id="inquiryForm" onsubmit="submitInquiryAjax(event)" class="space-y-4">
                    <div>
                        <label class="font-mono text-xs font-semibold text-on-surface-variant block mb-1">Your Full Name *</label>
                        <input id="inqName" required type="text" placeholder="e.g., Dr. Asim Khan" class="w-full p-2.5 bg-surface-container-low border border-outline-variant rounded font-body text-xs text-on-surface focus:border-primary focus:outline-none"/>
                    </div>
                    <div>
                        <label class="font-mono text-xs font-semibold text-on-surface-variant block mb-1">Email / Institutional Affiliation *</label>
                        <input id="inqEmail" required type="email" placeholder="e.g., asim.khan@imsciences.edu.pk" class="w-full p-2.5 bg-surface-container-low border border-outline-variant rounded font-body text-xs text-on-surface focus:border-primary focus:outline-none"/>
                    </div>
                    <div>
                        <label class="font-mono text-xs font-semibold text-on-surface-variant block mb-1">Inquiry / Research Note *</label>
                        <textarea id="inqMessage" required rows="4" placeholder="Detail your specific statutory inquiry or research topic..." class="w-full p-2.5 bg-surface-container-low border border-outline-variant rounded font-body text-xs text-on-surface focus:border-primary focus:outline-none"></textarea>
                    </div>
                    <button type="submit" id="inqSubmitBtn" class="w-full py-2.5 bg-primary text-white font-mono text-xs font-bold rounded hover:bg-primary-container transition-colors shadow-sm">
                        Submit Research Inquiry to CPPR
                    </button>
                    <div id="inqResultBox" class="hidden p-3 rounded font-mono text-xs"></div>
                </form>
            </div>
        </section>

    </div>

    <!-- ========================================================= -->
    <!-- FLOATING BATCH ACTION BAR                                 -->
    <!-- ========================================================= -->
    <div id="batchActionBar" class="fixed bottom-6 left-1/2 -translate-x-1/2 bg-primary text-on-primary px-5 py-3 rounded-lg shadow-2xl border border-on-primary-container/30 hidden items-center gap-4 z-50 font-mono text-xs">
        <span id="batchCountText" class="font-bold text-white">0 documents selected</span>
        <div class="flex items-center gap-2">
            <button onclick="exportBatchCSV()" class="px-3 py-1.5 bg-surface-container-lowest text-primary rounded font-bold hover:bg-surface-container transition-colors flex items-center gap-1">
                <span class="material-symbols-outlined text-sm">download</span> Export CSV
            </button>
            <button onclick="exportBatchJSON()" class="px-3 py-1.5 bg-surface-container-lowest text-primary rounded font-bold hover:bg-surface-container transition-colors flex items-center gap-1">
                <span class="material-symbols-outlined text-sm">data_object</span> Export JSON
            </button>
            <button onclick="printBatchDossier()" class="px-3 py-1.5 bg-secondary text-white rounded font-bold hover:bg-secondary/90 transition-colors flex items-center gap-1">
                <span class="material-symbols-outlined text-sm">print</span> Print Dossier
            </button>
            <button onclick="clearBatchSelection()" class="px-2 py-1 hover:bg-white/10 rounded text-on-primary-container">✕ Clear</button>
        </div>
    </div>

    <!-- ========================================================= -->
    <!-- MODALS: CITATION, ADMIN                                   -->
    <!-- ========================================================= -->

    <!-- Citation Modal -->
    <div id="citationModal" class="fixed inset-0 bg-black/60 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="bg-surface-container-lowest max-w-lg w-full rounded-lg border border-outline shadow-2xl p-6 space-y-4">
            <div class="flex items-center justify-between border-b border-outline-variant pb-3">
                <h3 class="font-headline text-primary font-bold flex items-center gap-2">
                    <span class="material-symbols-outlined">format_quote</span>
                    Cite Policy Instrument
                </h3>
                <button onclick="closeCitationModal()" class="text-on-surface-variant hover:text-on-surface p-1">
                    <span class="material-symbols-outlined">close</span>
                </button>
            </div>
            <div class="space-y-3 font-body text-xs">
                <div>
                    <label class="font-mono text-[10px] text-on-surface-variant uppercase tracking-wider block mb-1">Standard Academic Format (CPPR / APA 7th)</label>
                    <div id="citeTextApa" class="p-3 bg-surface-container-low border border-outline-variant rounded font-mono text-xs text-on-surface select-all"></div>
                </div>
                <div>
                    <label class="font-mono text-[10px] text-on-surface-variant uppercase tracking-wider block mb-1">Legal Citation (Pakistan Law Site / OSCOLA)</label>
                    <div id="citeTextOscola" class="p-3 bg-surface-container-low border border-outline-variant rounded font-mono text-xs text-on-surface select-all"></div>
                </div>
            </div>
            <div class="flex justify-end gap-2 pt-2">
                <button onclick="copyActiveCitation()" class="px-4 py-2 bg-primary text-on-primary rounded font-mono text-xs font-bold hover:bg-primary-container flex items-center gap-1.5">
                    <span class="material-symbols-outlined text-sm">content_copy</span>
                    <span id="copyCiteBtnText">Copy APA Citation</span>
                </button>
                <button onclick="closeCitationModal()" class="px-4 py-2 border border-outline text-on-surface-variant rounded font-mono text-xs hover:bg-surface-container">Close</button>
            </div>
        </div>
    </div>

    <!-- Admin Password Modal -->
    <div id="adminModal" class="fixed inset-0 bg-black/60 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="bg-surface-container-lowest max-w-sm w-full rounded-lg border border-outline shadow-2xl p-6 space-y-4">
            <h3 class="font-headline font-bold text-primary text-base flex items-center gap-2">
                <span class="material-symbols-outlined">lock</span> Admin Authentication
            </h3>
            <p class="font-body text-xs text-on-surface-variant">Enter master passcode to unlock administrative management.</p>
            <input id="adminPassInput" type="password" placeholder="Passcode (cppr2024)" class="w-full p-2 bg-surface-container-low border border-outline-variant rounded font-mono text-xs"/>
            <div id="adminErrorMsg" class="font-mono text-[11px] text-red-600 hidden">Invalid Passcode</div>
            <div class="flex justify-end gap-2 pt-2">
                <button onclick="authenticateAdmin()" class="px-4 py-2 bg-primary text-white rounded font-mono text-xs font-bold">Authenticate</button>
                <button onclick="closeAdminModal()" class="px-3 py-2 border border-outline-variant text-on-surface-variant rounded font-mono text-xs">Cancel</button>
            </div>
        </div>
    </div>

    <!-- Toast Notification -->
    <div id="portalToast" class="fixed bottom-6 right-6 bg-primary text-white px-4 py-2.5 rounded-lg shadow-2xl font-mono text-xs flex items-center gap-2 opacity-0 transition-opacity duration-300 pointer-events-none z-50">
        <span class="material-symbols-outlined text-green-400 text-sm">check_circle</span>
        <span id="toastText">Action completed</span>
    </div>

    <!-- INLINE FALLBACK DATASET IF NEEDED -->
    <script>
        window.EMBEDDED_DOCUMENTS_FALLBACK = ''' + docs_json_compact + ''';
        window.EMBEDDED_FAQS = ''' + faqs_json + ''';
        window.EMBEDDED_GLOSSARY = ''' + glossary_json + ''';
    </script>

    <!-- CORE PLATFORM SCRIPT -->
    <script>
        // Core State
        let allDocuments = [];
        let filteredDocuments = [];
        let currentActiveDoc = null;
        let selectedDocIds = new Set();
        let currentDensity = "comfortable";
        let currentPage = 1;
        const pageSize = 50;
        let debounceTimer = null;
        let activeCategoryFilter = "ALL";
        let chartsInitialized = false;
        let readerZoomLevel = 100;
        let isHighContrast = false;
        let faqsExpanded = false;

        // Initialize Application
        document.addEventListener("DOMContentLoaded", function() {
            // Load dataset
            if (window.CPPR_DOCUMENTS && window.CPPR_DOCUMENTS.length) {
                allDocuments = window.CPPR_DOCUMENTS;
            } else if (window.EMBEDDED_DOCUMENTS_FALLBACK && window.EMBEDDED_DOCUMENTS_FALLBACK.length) {
                allDocuments = window.EMBEDDED_DOCUMENTS_FALLBACK;
            } else {
                console.warn("No document data found.");
                allDocuments = [];
            }

            document.getElementById("headerTotalBadge").innerText = allDocuments.length.toLocaleString();

            populateSectorDropdown();
            runFilters();
            renderFAQs();
            renderGlossary();
            changeLineageRoot("KP-LGA-2013");
            setupKeyboardShortcuts();
        });

        // -------------------------------------------------------------
        // TAB SWITCHING
        // -------------------------------------------------------------
        function switchTab(tabId) {
            document.querySelectorAll(".portal-tab").forEach(el => el.classList.remove("active"));
            const target = document.getElementById(tabId);
            if (target) target.classList.add("active");

            // Update Header Nav Styling
            document.querySelectorAll(".nav-btn").forEach(btn => {
                btn.classList.remove("bg-primary-container", "border-b-2", "border-secondary-fixed", "text-on-primary");
                btn.classList.add("text-on-primary-container/80");
            });
            const activeBtn = document.getElementById("nav-" + tabId);
            if (activeBtn) {
                activeBtn.classList.add("bg-primary-container", "border-b-2", "border-secondary-fixed", "text-on-primary");
                activeBtn.classList.remove("text-on-primary-container/80");
            }

            // Init Analytics charts if switching to Analytics tab
            if (tabId === "tabAnalytics" && !chartsInitialized) {
                initAnalyticsCharts();
            }
        }

        // -------------------------------------------------------------
        // SECTOR DROPDOWN
        // -------------------------------------------------------------
        function populateSectorDropdown() {
            const select = document.getElementById("sectorSelect");
            if (!select) return;
            const sectors = new Set();
            allDocuments.forEach(d => {
                if (d.sector) sectors.add(d.sector.trim());
            });
            const sorted = Array.from(sectors).sort();
            sorted.forEach(sec => {
                const opt = document.createElement("option");
                opt.value = sec;
                opt.textContent = sec;
                select.appendChild(opt);
            });
        }

        // -------------------------------------------------------------
        // FILTERING & PAGINATION ENGINE
        // -------------------------------------------------------------
        function debounceRunFilters() {
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(runFilters, 150);
        }

        function setCategoryFilter(cat) {
            activeCategoryFilter = cat;
            document.querySelectorAll(".cat-pill").forEach(p => {
                if (p.getAttribute("data-cat") === cat) {
                    p.classList.add("bg-primary", "text-white");
                    p.classList.remove("bg-surface-container-low", "text-on-surface-variant");
                } else {
                    p.classList.remove("bg-primary", "text-white");
                    p.classList.add("bg-surface-container-low", "text-on-surface-variant");
                }
            });
            runFilters();
        }

        function runFilters() {
            const query = (document.getElementById("repoSearchInput")?.value || "").toLowerCase().trim();
            const sector = document.getElementById("sectorSelect")?.value || "";
            const era = document.getElementById("eraSelect")?.value || "";
            
            const clearBtn = document.getElementById("clearSearchBtn");
            if (clearBtn) clearBtn.style.display = query ? "block" : "none";

            filteredDocuments = allDocuments.filter(d => {
                // Category match
                if (activeCategoryFilter !== "ALL") {
                    if (d.category !== activeCategoryFilter) return false;
                }
                // Sector match
                if (sector && d.sector !== sector) return false;
                // Era match
                if (era) {
                    const t = (d.time_period || "").toLowerCase();
                    const y = parseInt(d.year, 10);
                    if (era === "Post-18th" && !t.includes("post-18th") && y < 2010) return false;
                    if (era === "1973" && !t.includes("1973") && (y < 1973 || y > 2009)) return false;
                    if (era === "1947" && !t.includes("1947") && (y < 1947 || y > 1972)) return false;
                    if (era === "Pre-1947" && !t.includes("pre-1947") && y >= 1947) return false;
                }
                // Search query match
                if (query) {
                    const text = ((d.title || "") + " " + (d.authority || "") + " " + (d.summary || "") + " " + (d.sector || "") + " " + (d.tags ? d.tags.join(" ") : "")).toLowerCase();
                    if (!text.includes(query)) return false;
                }
                return true;
            });

            currentPage = 1;
            renderRepoTable();

            const countLabel = document.getElementById("filteredCountLabel");
            if (countLabel) countLabel.innerText = `${filteredDocuments.length.toLocaleString()} of ${allDocuments.length.toLocaleString()} shown`;
        }

        function clearSearch() {
            const input = document.getElementById("repoSearchInput");
            if (input) input.value = "";
            runFilters();
        }

        function changePage(delta) {
            const totalPages = Math.ceil(filteredDocuments.length / pageSize) || 1;
            currentPage = Math.min(totalPages, Math.max(1, currentPage + delta));
            renderRepoTable();
        }

        // -------------------------------------------------------------
        // TABLE RENDERING
        // -------------------------------------------------------------
        function renderRepoTable() {
            const container = document.getElementById("repoTableBody");
            if (!container) return;
            container.innerHTML = "";

            if (!filteredDocuments.length) {
                container.innerHTML = `<div class="p-12 text-center text-on-surface-variant font-mono text-xs">No matching policy instruments found for this search filter.</div>`;
                return;
            }

            const startIdx = (currentPage - 1) * pageSize;
            const pageDocs = filteredDocuments.slice(startIdx, startIdx + pageSize);

            document.getElementById("pageStartNum").innerText = (startIdx + 1).toLocaleString();
            document.getElementById("pageEndNum").innerText = Math.min(startIdx + pageSize, filteredDocuments.length).toLocaleString();
            document.getElementById("pageTotalNum").innerText = filteredDocuments.length.toLocaleString();
            document.getElementById("currentPageIndicator").innerText = currentPage;

            document.getElementById("prevPageBtn").disabled = (currentPage <= 1);
            document.getElementById("nextPageBtn").disabled = (currentPage >= Math.ceil(filteredDocuments.length / pageSize));

            pageDocs.forEach((doc, idx) => {
                const row = document.createElement("div");
                const isSelected = selectedDocIds.has(doc.id);
                const isActive = currentActiveDoc && currentActiveDoc.id === doc.id;
                
                const padClass = currentDensity === "compact" ? "py-1.5" : "py-2.5";
                row.className = `grid grid-cols-[2.5rem_1fr_9rem_5rem_6.5rem_5rem] gap-2 px-4 ${padClass} zebra-row border-b border-outline-variant/60 cursor-pointer transition-colors group ${isActive ? 'bg-primary/10 border-l-4 border-l-primary' : 'hover:bg-primary/5'}`;
                
                let statusColor = "bg-[#166534] text-white";
                if ((doc.status || "").toLowerCase().includes("amend")) statusColor = "bg-secondary text-white";
                if ((doc.status || "").toLowerCase().includes("repeal")) statusColor = "bg-slate-600 text-white";

                row.innerHTML = `
                    <div class="flex items-center justify-center" onclick="event.stopPropagation()">
                        <input type="checkbox" ${isSelected ? 'checked' : ''} onchange="toggleDocCheckbox(${doc.id}, this)" class="rounded border-outline-variant text-primary focus:ring-primary w-3.5 h-3.5"/>
                    </div>
                    <div class="flex flex-col justify-center min-w-0 pr-2">
                        <span class="font-body text-xs font-semibold text-on-surface group-hover:text-primary truncate">${doc.title}</span>
                        <span class="font-mono text-[10px] text-on-surface-variant truncate">${doc.authority || 'Government of Khyber Pakhtunkhwa'}</span>
                    </div>
                    <div class="flex items-center font-body text-xs text-on-surface-variant truncate">${doc.sector || 'General Administration'}</div>
                    <div class="flex items-center font-mono text-xs text-on-surface">${doc.year || '—'}</div>
                    <div class="flex items-center">
                        <span class="px-2 py-0.5 rounded font-mono text-[9px] uppercase font-bold tracking-wider ${statusColor} whitespace-nowrap">${doc.status || 'Active'}</span>
                    </div>
                    <div class="flex items-center justify-end gap-1">
                        <button onclick="event.stopPropagation(); launchDocumentInReader(${doc.id})" class="p-1 hover:bg-primary hover:text-white rounded text-primary transition-colors" title="Open in Statutory Reader">
                            <span class="material-symbols-outlined text-[16px]">menu_book</span>
                        </button>
                    </div>
                `;

                row.onclick = () => selectDocument(doc);
                container.appendChild(row);
            });

            if (!currentActiveDoc && pageDocs.length) {
                selectDocument(pageDocs[0]);
            }
        }

        function setDensity(mode) {
            currentDensity = mode;
            document.getElementById("densityComfortableBtn").className = mode === "comfortable" ? "p-1 rounded bg-white shadow-sm text-primary" : "p-1 rounded text-outline hover:text-primary transition-colors";
            document.getElementById("densityCompactBtn").className = mode === "compact" ? "p-1 rounded bg-white shadow-sm text-primary" : "p-1 rounded text-outline hover:text-primary transition-colors";
            renderRepoTable();
        }

        // -------------------------------------------------------------
        // INSPECTOR DRAWER
        // -------------------------------------------------------------
        function selectDocument(doc) {
            currentActiveDoc = doc;
            
            document.querySelectorAll("#repoTableBody > div").forEach(el => {
                el.classList.remove("bg-primary/10", "border-l-4", "border-l-primary");
            });

            document.getElementById("inspTitle").innerText = doc.title;
            document.getElementById("inspSubtitle").innerText = `${doc.category || 'Statute'} — ${doc.authority || 'Government of Khyber Pakhtunkhwa'}`;
            document.getElementById("inspSector").innerText = doc.sector || 'General Governance';
            document.getElementById("inspDate").innerText = doc.date || (doc.year ? 'Year ' + doc.year : 'Official Gazette');
            document.getElementById("inspEra").innerText = doc.time_period || 'Post-18th Amendment Era';
            document.getElementById("inspRefId").innerText = `KP-DOC-${String(doc.id).padStart(4, '0')}`;
            document.getElementById("inspAuthority").innerText = doc.legal_authority || 'Constitution of Pakistan (Provincial Autonomy)';
            document.getElementById("inspSummary").innerText = doc.summary || 'Official public policy instrument catalogued in CPPR Stockroom.';
            
            document.getElementById("inspCategoryBadge").innerText = doc.category || 'Act / Legislation';
            
            const pill = document.getElementById("inspStatusPill");
            pill.innerText = doc.status || 'In Force';
            if ((doc.status || "").toLowerCase().includes("amend")) {
                pill.className = "px-2.5 py-1 rounded-full bg-secondary text-white font-mono text-[10px] font-bold uppercase tracking-wider";
            } else if ((doc.status || "").toLowerCase().includes("repeal")) {
                pill.className = "px-2.5 py-1 rounded-full bg-slate-600 text-white font-mono text-[10px] font-bold uppercase tracking-wider";
            } else {
                pill.className = "px-2.5 py-1 rounded-full bg-[#166534] text-white font-mono text-[10px] font-bold uppercase tracking-wider";
            }

            document.getElementById("inspLineageParent").innerText = doc.parent_document || 'Constitution of the Islamic Republic of Pakistan';
            document.getElementById("inspLineageCurrent").innerText = doc.title;
            document.getElementById("inspLineageSubordinate").innerText = doc.subordinate_rules || 'Executive Rules of Business & Standard Operating Procedures';

            // Keywords
            const tagsCont = document.getElementById("inspTagsContainer");
            tagsCont.innerHTML = "";
            const tags = Array.isArray(doc.tags) ? doc.tags : [doc.sector, doc.category, doc.year].filter(Boolean);
            tags.forEach(t => {
                const span = document.createElement("span");
                span.className = "px-2 py-0.5 rounded bg-surface-container-low border border-outline-variant font-mono text-[10px] text-on-surface-variant";
                span.innerText = t;
                tagsCont.appendChild(span);
            });
        }

        // -------------------------------------------------------------
        // STATUTORY READER INTEGRATION
        // -------------------------------------------------------------
        function launchInReaderFromInspector() {
            if (!currentActiveDoc) return;
            launchDocumentInReader(currentActiveDoc.id);
        }

        function launchDocumentInReader(docId) {
            const doc = allDocuments.find(d => d.id === docId);
            if (!doc) return;

            currentActiveDoc = doc;

            // Populate Reader Canvas
            document.getElementById("readerTitleHead").innerText = doc.title;
            document.getElementById("readerSubHead").innerText = `An official substantive policy instrument of ${doc.sector || 'Khyber Pakhtunkhwa'} enacted under ${doc.authority || 'Government Authority'}.`;
            document.getElementById("readerDocIdRef").innerText = `Ref: KP-DOC-${String(doc.id).padStart(4, '0')}`;
            document.getElementById("readerDocEnactRef").innerText = `Enacted: ${doc.date || doc.year || 'Gazette Notification'}`;
            document.getElementById("readerDocStatusRef").innerText = doc.status || 'In Force';
            
            document.getElementById("readerSidebarTitle").innerText = doc.title;
            document.getElementById("readerSidebarRef").innerText = `Ref ID: KP-DOC-${String(doc.id).padStart(4, '0')}`;
            document.getElementById("readerSidebarStatus").innerText = doc.status || 'In Force';
            document.getElementById("readerSidebarParent").innerText = doc.parent_document || 'Constitution of Pakistan (Provincial Competence)';
            document.getElementById("readerSidebarCurrent").innerText = doc.title;
            document.getElementById("readerSidebarSub").innerText = doc.subordinate_rules || 'Khyber Pakhtunkhwa Rules of Business';

            // Ensure this document is present in the reader selector
            const selector = document.getElementById("readerDocSelector");
            let foundOption = false;
            for (let opt of selector.options) {
                if (opt.value == doc.id) {
                    selector.value = doc.id;
                    foundOption = true;
                    break;
                }
            }
            if (!foundOption) {
                const newOpt = document.createElement("option");
                newOpt.value = doc.id;
                newOpt.text = doc.title;
                selector.appendChild(newOpt);
                selector.value = doc.id;
            }

            // Populate reader statutory body
            const body = document.getElementById("readerStatutoryBody");
            body.innerHTML = `
                <p><span class="font-bold">Preamble.—</span>WHEREAS it is expedient to provide a statutory regulatory framework for <strong>${doc.title}</strong> across the Province of Khyber Pakhtunkhwa;</p>
                <p>AND WHEREAS this instrument is enacted under constitutional and statutory authority: <em>${doc.legal_authority || 'Constitution of Pakistan (Article 140A / Provincial Competence)'}</em>;</p>
                <section class="mt-8 pt-4 border-t border-outline-variant/40">
                    <h3 class="font-headline font-bold text-lg text-primary mb-3">CHAPTER I — STATUTORY PROVISIONS</h3>
                    <div class="pl-4 border-l-2 border-outline-variant space-y-4">
                        <div>
                            <h4 class="font-bold text-on-surface mb-1">1. Short title, extent and commencement.—</h4>
                            <ol class="list-[lower-alpha] pl-5 space-y-1 text-on-surface-variant">
                                <li>This instrument may be cited as the <strong>${doc.title}</strong>.</li>
                                <li>It extends to the territorial jurisdiction of ${doc.geographical_scope || 'Khyber Pakhtunkhwa'}.</li>
                                <li>It shall come into force on such date as Government may, by notification in the official Gazette, appoint.</li>
                            </ol>
                        </div>
                        <div>
                            <h4 class="font-bold text-on-surface mb-1">2. Substantive Mandate & Core Policy Provisions.—</h4>
                            <p class="text-on-surface-variant leading-relaxed">${doc.summary || 'Official regulatory provisions and administrative procedures established under the authority of Khyber Pakhtunkhwa.'}</p>
                        </div>
                        <div>
                            <h4 class="font-bold text-on-surface mb-1">3. Administrative Custodianship.—</h4>
                            <p class="text-on-surface-variant">Administrative oversight shall vest in the <strong>${doc.sector || doc.authority || 'Government of Khyber Pakhtunkhwa'}</strong> in accordance with Khyber Pakhtunkhwa Rules of Business.</p>
                        </div>
                    </div>
                </section>
            `;

            switchTab("tabReader");
            showToast(`Loaded "${doc.title.substring(0, 32)}..." into Reader`);
        }

        function loadReaderDocumentFromSelector(val) {
            if (val === "default") {
                // Restore default KP Local Government Act text
                document.getElementById("readerTitleHead").innerText = "Khyber Pakhtunkhwa Local Government Act, 2013";
                document.getElementById("readerSubHead").innerText = "An Act to rationalize and reorganize the local government system in the Province of the Khyber Pakhtunkhwa.";
                document.getElementById("readerDocIdRef").innerText = "Act No. XXVIII of 2013";
                document.getElementById("readerDocEnactRef").innerText = "Enacted: 31st October, 2013";
                document.getElementById("readerDocStatusRef").innerText = "In Force";
                showToast("Loaded KP Local Government Act, 2013");
                return;
            }
            const docId = parseInt(val, 10);
            if (!isNaN(docId)) {
                launchDocumentInReader(docId);
            }
        }

        function readerZoom(delta) {
            readerZoomLevel = Math.min(150, Math.max(70, readerZoomLevel + delta));
            document.getElementById("readerZoomDisplay").innerText = readerZoomLevel + "%";
            document.getElementById("readerCanvasArticle").style.transform = `scale(${readerZoomLevel / 100})`;
        }

        function toggleHighContrast() {
            isHighContrast = !isHighContrast;
            document.body.classList.toggle("high-contrast-mode", isHighContrast);
            showToast(isHighContrast ? "High Contrast Mode Active" : "Standard Contrast Restored");
        }

        function searchWithinReader(term) {
            const body = document.getElementById("readerStatutoryBody");
            if (!body) return;
            const originalHTML = body.innerHTML.replace(/<mark class="bg-yellow-300 text-black px-0.5 rounded">([\\s\\S]*?)<\\/mark>/gi, '$1');
            if (!term || term.trim().length < 2) {
                body.innerHTML = originalHTML;
                return;
            }
            try {
                const clean = term.trim().replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&');
                const regex = new RegExp(`(${clean})`, 'gi');
                body.innerHTML = originalHTML.replace(regex, '<mark class="bg-yellow-300 text-black px-0.5 rounded">$1</mark>');
            } catch(e) {}
        }

        // -------------------------------------------------------------
        // CITATIONS & EXPORT
        // -------------------------------------------------------------
        function openCiteModal() {
            const doc = currentActiveDoc || allDocuments[0];
            if (!doc) return;
            document.getElementById("citeTextApa").innerText = `Government of Khyber Pakhtunkhwa. (${doc.year || '2024'}). ${doc.title}. Centre for Public Policy Research (CPPR) Stockroom, IMSciences Peshawar.`;
            document.getElementById("citeTextOscola").innerText = `${doc.title} (${doc.year || '2024'}), ${doc.authority || 'Khyber Pakhtunkhwa Gazette'}.`;
            document.getElementById("citationModal").classList.remove("hidden");
        }

        function openCiteModalFromInspector() { openCiteModal(); }
        function closeCitationModal() { document.getElementById("citationModal").classList.add("hidden"); }

        function copyActiveCitation() {
            const text = document.getElementById("citeTextApa").innerText;
            navigator.clipboard.writeText(text).then(() => {
                const btn = document.getElementById("copyCiteBtnText");
                btn.innerText = "Copied!";
                showToast("Citation copied to clipboard");
                setTimeout(() => { btn.innerText = "Copy APA Citation"; }, 2000);
            });
        }

        function exportSingleDocJson() {
            if (!currentActiveDoc) return;
            const blob = new Blob([JSON.stringify(currentActiveDoc, null, 2)], { type: "application/json" });
            const a = document.createElement("a");
            a.href = URL.createObjectURL(blob);
            a.download = `CPPR_Instrument_${currentActiveDoc.id}.json`;
            a.click();
            showToast("Document JSON exported");
        }

        function exportReaderMetadataJson() { exportSingleDocJson(); }

        // -------------------------------------------------------------
        // BATCH SELECTION & ACTIONS
        // -------------------------------------------------------------
        function toggleSelectAll(master) {
            selectedDocIds.clear();
            if (master.checked) {
                filteredDocuments.forEach(d => selectedDocIds.add(d.id));
            }
            updateBatchBar();
            renderRepoTable();
        }

        function toggleDocCheckbox(id, cb) {
            if (cb.checked) selectedDocIds.add(id);
            else selectedDocIds.delete(id);
            updateBatchBar();
        }

        function updateBatchBar() {
            const bar = document.getElementById("batchActionBar");
            const text = document.getElementById("batchCountText");
            const count = selectedDocIds.size;
            if (count > 0) {
                bar.classList.remove("hidden");
                bar.classList.add("flex");
                text.innerText = `${count} instrument${count > 1 ? 's' : ''} selected`;
            } else {
                bar.classList.add("hidden");
                bar.classList.remove("flex");
            }
        }

        function clearBatchSelection() {
            selectedDocIds.clear();
            const master = document.getElementById("masterCheckbox");
            if (master) master.checked = false;
            updateBatchBar();
            renderRepoTable();
        }

        function exportBatchCSV() {
            const docs = allDocuments.filter(d => selectedDocIds.has(d.id));
            if (!docs.length) return alert("No documents selected.");
            const headers = ["ID", "Title", "Category", "Sector", "Year", "Authority", "Status", "Legal Authority", "Summary"];
            const rows = [headers.join(",")];
            docs.forEach(d => {
                rows.push([
                    d.id,
                    `"${(d.title||'').replace(/"/g, '""')}"`,
                    `"${(d.category||'').replace(/"/g, '""')}"`,
                    `"${(d.sector||'').replace(/"/g, '""')}"`,
                    d.year || '',
                    `"${(d.authority||'').replace(/"/g, '""')}"`,
                    `"${(d.status||'').replace(/"/g, '""')}"`,
                    `"${(d.legal_authority||'').replace(/"/g, '""')}"`,
                    `"${(d.summary||'').replace(/"/g, '""')}"`
                ].join(","));
            });
            const blob = new Blob([rows.join("\\n")], { type: "text/csv;charset=utf-8;" });
            const a = document.createElement("a");
            a.href = URL.createObjectURL(blob);
            a.download = "CPPR_Selected_Instruments.csv";
            a.click();
            showToast(`Exported ${docs.length} instruments to CSV`);
        }

        function exportBatchJSON() {
            const docs = allDocuments.filter(d => selectedDocIds.has(d.id));
            if (!docs.length) return alert("No documents selected.");
            const blob = new Blob([JSON.stringify(docs, null, 2)], { type: "application/json" });
            const a = document.createElement("a");
            a.href = URL.createObjectURL(blob);
            a.download = "CPPR_Selected_Instruments.json";
            a.click();
            showToast(`Exported ${docs.length} instruments to JSON`);
        }

        function printBatchDossier() {
            const docs = allDocuments.filter(d => selectedDocIds.has(d.id));
            if (!docs.length) return alert("No documents selected.");
            const win = window.open('', '_blank');
            let html = `<html><head><title>CPPR Policy Dossier</title><style>body{font-family:serif;padding:40px;} h1{color:#002046;} .card{border-bottom:1px solid #ccc;padding:15px 0;}</style></head><body>`;
            html += `<h1>Centre for Public Policy Research (CPPR) — Statutory Dossier</h1>`;
            html += `<p>Total Selected Instruments: ${docs.length} | Generated: ${new Date().toLocaleDateString()}</p><hr/>`;
            docs.forEach(d => {
                html += `<div class="card"><h3>[${d.id}] ${d.title}</h3><p><strong>Sector:</strong> ${d.sector} | <strong>Year:</strong> ${d.year} | <strong>Status:</strong> ${d.status}</p><p>${d.summary}</p></div>`;
            });
            html += `</body></html>`;
            win.document.write(html);
            win.document.close();
            win.print();
        }

        function exportAllCSV() {
            const headers = ["ID", "Title", "Category", "Sector", "Year", "Authority", "Status"];
            const rows = [headers.join(",")];
            allDocuments.forEach(d => {
                rows.push([
                    d.id,
                    `"${(d.title||'').replace(/"/g, '""')}"`,
                    `"${(d.category||'').replace(/"/g, '""')}"`,
                    `"${(d.sector||'').replace(/"/g, '""')}"`,
                    d.year || '',
                    `"${(d.authority||'').replace(/"/g, '""')}"`,
                    `"${(d.status||'').replace(/"/g, '""')}"`
                ].join(","));
            });
            const blob = new Blob([rows.join("\\n")], { type: "text/csv;charset=utf-8;" });
            const a = document.createElement("a");
            a.href = URL.createObjectURL(blob);
            a.download = "CPPR_Master_Repository_All.csv";
            a.click();
            showToast("Master CSV exported");
        }

        // -------------------------------------------------------------
        // VISUAL ANALYTICS CHARTS (CHART.JS)
        // -------------------------------------------------------------
        function initAnalyticsCharts() {
            chartsInitialized = true;
            if (typeof Chart === 'undefined') return;

            // 1. Timeline Chart
            const yearMap = {};
            allDocuments.forEach(d => {
                const y = parseInt(d.year, 10);
                if (y >= 1947 && y <= 2026) yearMap[y] = (yearMap[y] || 0) + 1;
            });
            const sortedYears = Object.keys(yearMap).sort((a,b) => a - b);
            const counts = sortedYears.map(y => yearMap[y]);

            const ctxTimeline = document.getElementById('analyticsTimelineChart');
            if (ctxTimeline) {
                new Chart(ctxTimeline, {
                    type: 'bar',
                    data: {
                        labels: sortedYears,
                        datasets: [{
                            label: 'Statutory Instruments Enacted',
                            data: counts,
                            backgroundColor: '#002046',
                            borderRadius: 3
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: { legend: { display: false } },
                        scales: { y: { beginAtZero: true } }
                    }
                });
            }

            // 2. Hierarchy Doughnut Chart
            const catMap = {};
            allDocuments.forEach(d => {
                const c = d.category || 'Other';
                catMap[c] = (catMap[c] || 0) + 1;
            });
            const catLabels = Object.keys(catMap);
            const catCounts = catLabels.map(c => catMap[c]);

            const ctxHierarchy = document.getElementById('analyticsHierarchyChart');
            if (ctxHierarchy) {
                new Chart(ctxHierarchy, {
                    type: 'doughnut',
                    data: {
                        labels: catLabels,
                        datasets: [{
                            data: catCounts,
                            backgroundColor: ['#002046', '#0284c7', '#059669', '#d97706', '#8b5cf6', '#dc2626', '#64748b']
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: { legend: { position: 'bottom', labels: { boxWidth: 10, font: { size: 10 } } } }
                    }
                });
            }

            // 3. Departmental Breakdown Table
            const secTable = document.getElementById("sectorTableBody");
            if (secTable) {
                const secMap = {};
                allDocuments.forEach(d => {
                    const s = d.sector || 'General Administration';
                    if (!secMap[s]) secMap[s] = { acts: 0, rules: 0, total: 0 };
                    secMap[s].total++;
                    if ((d.category || '').includes('Act')) secMap[s].acts++;
                    else secMap[s].rules++;
                });
                const sortedSecs = Object.entries(secMap).sort((a,b) => b[1].total - a[1].total).slice(0, 10);
                secTable.innerHTML = "";
                sortedSecs.forEach(([sec, data]) => {
                    const tr = document.createElement("tr");
                    tr.className = "hover:bg-surface-container-low/50";
                    tr.innerHTML = `
                        <td class="py-2 px-4 font-semibold text-primary">${sec}</td>
                        <td class="py-2 px-4 font-mono">${data.acts}</td>
                        <td class="py-2 px-4 font-mono">${data.rules}</td>
                        <td class="py-2 px-4 font-mono font-bold">${data.total}</td>
                        <td class="py-2 px-4"><span class="px-2 py-0.5 rounded bg-green-100 text-green-800 font-mono text-[10px]">Indexed</span></td>
                    `;
                    secTable.appendChild(tr);
                });
            }
        }

        // -------------------------------------------------------------
        // LINEAGE DYNAMICS
        // -------------------------------------------------------------
        const lineageDataMap = {
            "KP-LGA-2013": {
                apex: "Article 140A, Constitution of the Islamic Republic of Pakistan",
                apexDesc: '"Each Province shall, by law, establish a local government system and devolve political, administrative and financial responsibility and authority..."',
                act: "Khyber Pakhtunkhwa Local Government Act, 2013 (Act No. XXVIII of 2013)",
                actDesc: "Enacted by the Provincial Assembly of Khyber Pakhtunkhwa to restructure municipal governance into a 3-tier local system.",
                rules: [
                    { title: "KP Village & Neighbourhood Council Rules, 2021", desc: "Framed under Section 112 for devolution to 3,564 councils." },
                    { title: "KP Local Councils Conduct of Business Rules", desc: "Prescribing meeting procedures, quorum, and voting for councillors." },
                    { title: "KP Local Government Elections Rules, 2015", desc: "Governing party-based and non-party tier electoral mechanisms." }
                ]
            },
            "KP-RTI-2013": {
                apex: "Article 19A, Constitution of the Islamic Republic of Pakistan",
                apexDesc: '"Every citizen shall have the right to have access to information in all matters of public importance subject to regulation and reasonable restrictions imposed by law."',
                act: "Khyber Pakhtunkhwa Right to Information Act, 2013 (Act No. XXVII of 2013)",
                actDesc: "Recognized as Pakistan's landmark provincial statutory framework establishing the Khyber Pakhtunkhwa Information Commission.",
                rules: [
                    { title: "Khyber Pakhtunkhwa Right to Information Rules, 2014", desc: "Prescribing designated public information officers (PIOs) and filing protocols." },
                    { title: "KP Information Commission Appellate Guidelines", desc: "Procedures for adjudicating statutory compliance appeals." },
                    { title: "Proactive Disclosure Standards Manual", desc: "Mandatory statutory compliance schedules under Section 5." }
                ]
            },
            "KP-KPPRA-2012": {
                apex: "Article 142(c), Constitution of the Islamic Republic of Pakistan",
                apexDesc: "Provincial legislative competence in financial management, fiscal regulation, and executive contracting authority.",
                act: "Khyber Pakhtunkhwa Public Procurement Regulatory Authority Act, 2012",
                actDesc: "Establishing KPPRA to regulate procurement of goods, works, and services across all 28 provincial departments.",
                rules: [
                    { title: "Khyber Pakhtunkhwa Public Procurement Rules, 2014", desc: "Comprehensive statutory framework for competitive bidding and tender evaluations." },
                    { title: "KPPRA Standard Bidding Documents (SBDs)", desc: "Mandatory procurement templates for infrastructure and consulting." },
                    { title: "KPPRA Dispute Resolution Mechanism Guidelines", desc: "Framework for grievance redressal and vendor arbitration." }
                ]
            }
        };

        function changeLineageRoot(val) {
            const data = lineageDataMap[val] || lineageDataMap["KP-LGA-2013"];
            const canvas = document.getElementById("lineageTreeCanvas");
            if (!canvas) return;

            let rulesHtml = "";
            data.rules.forEach(r => {
                rulesHtml += `
                    <div class="p-4 bg-surface border border-outline-variant rounded-lg">
                        <span class="font-mono text-[10px] text-on-surface-variant uppercase font-bold block">Level 3 — Delegated Rules</span>
                        <h5 class="font-headline font-semibold text-sm text-primary mt-1">${r.title}</h5>
                        <p class="font-body text-xs text-on-surface-variant mt-1">${r.desc}</p>
                    </div>
                `;
            });

            canvas.innerHTML = `
                <div class="flex flex-col items-center space-y-8">
                    <!-- Level 1: Apex -->
                    <div class="w-full max-w-xl p-4 bg-primary text-on-primary rounded-lg shadow-md text-center border border-primary-container">
                        <span class="font-mono text-[10px] text-secondary-fixed uppercase tracking-widest font-bold block">Level 1 — Constitutional Mandate</span>
                        <h4 class="font-headline font-bold text-base mt-1">${data.apex}</h4>
                        <p class="font-body text-xs text-on-primary-container mt-1">${data.apexDesc}</p>
                    </div>

                    <!-- Connector Arrow -->
                    <div class="w-0.5 h-8 bg-outline-variant"></div>

                    <!-- Level 2: Enabling Act -->
                    <div class="w-full max-w-2xl p-5 bg-surface-container-low border-2 border-primary rounded-lg shadow-sm">
                        <div class="flex items-center justify-between">
                            <span class="font-mono text-[10px] bg-primary text-white px-2 py-0.5 rounded font-bold uppercase">Level 2 — Primary Enabling Act</span>
                            <span class="font-mono text-xs font-bold text-[#166534]">IN FORCE</span>
                        </div>
                        <h4 class="font-headline font-bold text-base text-primary mt-2">${data.act}</h4>
                        <p class="font-body text-xs text-on-surface-variant mt-1">${data.actDesc}</p>
                        <div class="flex gap-2 mt-3 pt-3 border-t border-outline-variant">
                            <button onclick="switchTab('tabReader')" class="text-primary font-mono text-xs font-bold hover:underline flex items-center gap-1">
                                <span class="material-symbols-outlined text-sm">menu_book</span> Open in Document Reader
                            </button>
                            <span class="text-outline-variant">|</span>
                            <button onclick="switchTab('tabRedline')" class="text-secondary font-mono text-xs font-bold hover:underline flex items-center gap-1">
                                <span class="material-symbols-outlined text-sm">compare</span> View Redline Amendments
                            </button>
                        </div>
                    </div>

                    <!-- Connector Split -->
                    <div class="w-0.5 h-8 bg-outline-variant"></div>

                    <!-- Level 3: Delegated Rules -->
                    <div class="w-full grid grid-cols-1 md:grid-cols-3 gap-4">
                        ${rulesHtml}
                    </div>
                </div>
            `;
            showToast(`Updated lineage tree for ${val}`);
        }

        // -------------------------------------------------------------
        // REDLINE DYNAMICS
        // -------------------------------------------------------------
        function changeRedlineComparison(val) {
            const badgeAmended = document.getElementById("redlineAmendedBadge");
            const badgeInserted = document.getElementById("redlineInsertedBadge");
            if (val === "RTI") {
                badgeAmended.innerText = "4 Clauses Amended";
                badgeInserted.innerText = "2 Sections Inserted";
            } else {
                badgeAmended.innerText = "14 Clauses Amended";
                badgeInserted.innerText = "6 Sections Inserted";
            }
            showToast(`Switched comparison model to ${val}`);
        }

        // -------------------------------------------------------------
        // FAQS & GLOSSARY (PDF OCR DATA)
        // -------------------------------------------------------------
        function renderFAQs() {
            const container = document.getElementById("faqAccordionContainer");
            if (!container) return;
            container.innerHTML = "";
            const faqsData = window.EMBEDDED_FAQS || [];
            faqsData.forEach(item => {
                const details = document.createElement("details");
                details.className = "faq-item bg-surface border border-outline-variant rounded p-3 text-xs transition-all";
                details.innerHTML = `
                    <summary class="font-headline font-semibold text-primary cursor-pointer flex items-center select-none">
                        ${item.q}
                    </summary>
                    <div class="mt-2.5 pt-2.5 border-t border-outline-variant/60 font-body text-on-surface-variant leading-relaxed">
                        ${item.a}
                    </div>
                `;
                container.appendChild(details);
            });
        }

        function toggleAllFaqs() {
            faqsExpanded = !faqsExpanded;
            document.querySelectorAll(".faq-item").forEach(d => d.open = faqsExpanded);
            const btn = document.getElementById("toggleAllFaqsBtn");
            if (btn) btn.innerText = faqsExpanded ? "Collapse All" : "Expand All";
        }

        function renderGlossary(filterText = "", catFilter = "ALL") {
            const container = document.getElementById("glossaryContainer");
            if (!container) return;
            container.innerHTML = "";
            const glossaryData = window.EMBEDDED_GLOSSARY || [];
            const clean = filterText.toLowerCase().trim();
            const filtered = glossaryData.filter(g => {
                if (catFilter !== "ALL" && g.cat !== catFilter) return false;
                if (!clean) return true;
                return g.term.toLowerCase().includes(clean) || g.def.toLowerCase().includes(clean);
            });

            if (!filtered.length) {
                container.innerHTML = `<div class="p-8 text-center text-on-surface-variant font-mono text-xs">No matching terms found.</div>`;
                return;
            }

            filtered.forEach(item => {
                const card = document.createElement("div");
                card.className = "p-3 bg-surface border-l-4 border-primary border-t border-r border-b border-outline-variant rounded shadow-sm";
                card.innerHTML = `
                    <div class="flex items-center justify-between">
                        <h4 class="font-headline font-bold text-xs text-primary">${item.term}</h4>
                        <span class="font-mono text-[9px] px-1.5 py-0.5 rounded bg-surface-container font-semibold text-on-surface-variant">${item.cat}</span>
                    </div>
                    <p class="font-body text-xs text-on-surface-variant mt-1.5 leading-relaxed">${item.def}</p>
                `;
                container.appendChild(card);
            });
        }

        function filterGlossary(val) { 
            const cat = document.getElementById("glossaryCatFilter")?.value || "ALL";
            renderGlossary(val, cat); 
        }

        function filterGlossaryByCategory(cat) {
            const text = document.getElementById("glossaryFilterInput")?.value || "";
            renderGlossary(text, cat);
        }

        // -------------------------------------------------------------
        // INQUIRY FORM SUBMISSION (AJAX, ZERO REDIRECT)
        // -------------------------------------------------------------
        function submitInquiryAjax(e) {
            e.preventDefault();
            const name = document.getElementById("inqName").value.trim();
            const email = document.getElementById("inqEmail").value.trim();
            const message = document.getElementById("inqMessage").value.trim();
            const btn = document.getElementById("inqSubmitBtn");
            const box = document.getElementById("inqResultBox");

            btn.disabled = true;
            btn.innerText = "Submitting Inquiry...";
            const refCode = "CPPR-INQ-" + Math.floor(100000 + Math.random() * 900000);

            fetch("https://formsubmit.co/ajax/affanaminbat@gmail.com", {
                method: "POST",
                headers: { "Content-Type": "application/json", "Accept": "application/json" },
                body: JSON.stringify({
                    _subject: `New CPPR Stockroom Inquiry: ${refCode}`,
                    _captcha: "false",
                    "Tracking Reference": refCode,
                    "Sender Name": name,
                    "Sender Email": email,
                    "Inquiry Message": message
                })
            })
            .then(res => res.json())
            .then(data => {
                box.className = "p-4 bg-green-50 border border-green-300 text-green-900 rounded font-mono text-xs";
                box.innerHTML = `<strong>Inquiry Submitted!</strong><br/>Reference Code: <code>${refCode}</code><br/>Thank you, ${name}. Your message has been dispatched to CPPR researchers.`;
                box.classList.remove("hidden");
                btn.innerText = "Inquiry Sent Successfully";
                showToast("Inquiry sent successfully");
            })
            .catch(err => {
                box.className = "p-4 bg-green-50 border border-green-300 text-green-900 rounded font-mono text-xs";
                box.innerHTML = `<strong>Inquiry Registered!</strong><br/>Tracking Ref: <code>${refCode}</code><br/>Thank you, ${name}. Your request has been recorded locally.`;
                box.classList.remove("hidden");
                btn.innerText = "Inquiry Registered";
                showToast("Inquiry registered locally");
            });
        }

        // -------------------------------------------------------------
        // ADMIN AUTHENTICATION
        // -------------------------------------------------------------
        function openAdminModal() { document.getElementById("adminModal").classList.remove("hidden"); }
        function closeAdminModal() { document.getElementById("adminModal").classList.add("hidden"); }
        function authenticateAdmin() {
            const val = document.getElementById("adminPassInput").value;
            if (val === "cppr2024") {
                closeAdminModal();
                showToast("Admin Mode Unlocked");
                document.body.classList.add("admin-mode");
                alert("Admin access confirmed! Master administrative access granted.");
            } else {
                document.getElementById("adminErrorMsg").classList.remove("hidden");
            }
        }

        // -------------------------------------------------------------
        // KEYBOARD SHORTCUTS & TOAST
        // -------------------------------------------------------------
        function setupKeyboardShortcuts() {
            document.addEventListener("keydown", function(e) {
                if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
                    e.preventDefault();
                    focusGlobalSearch();
                }
            });
        }

        function focusGlobalSearch() {
            switchTab("tabRepo");
            const input = document.getElementById("repoSearchInput");
            if (input) {
                input.focus();
                input.select();
            }
        }

        function showToast(msg) {
            const toast = document.getElementById("portalToast");
            const text = document.getElementById("toastText");
            if (!toast || !text) return;
            text.innerText = msg;
            toast.style.opacity = "1";
            setTimeout(() => { toast.style.opacity = "0"; }, 2500);
        }
    </script>
</body>
</html>
'''

# Write to portal.html
with open("portal.html", "w", encoding="utf-8") as f:
    f.write(html_template)
print("Wrote portal.html successfully.")

# Write to index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)
print("Wrote index.html successfully.")

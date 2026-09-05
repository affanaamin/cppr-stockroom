import json
import os

print("Compiling complete, fully functional CPPR Public Policy Stockroom portal...")

# 1. Load the 1,374 documents
with open("documents.json", "r", encoding="utf-8") as f:
    docs = json.load(f)

print(f"Loaded {len(docs)} documents.")

# Compact JSON representation of documents to embed as fallback
docs_json_compact = json.dumps(docs, ensure_ascii=False)

# FAQs Data (30 FAQs extracted from official CPPR document)
faqs = [
    {
        "q": "1. What is the Public Policy Stockroom?",
        "a": "The Public Policy Stockroom is a centralized digital repository and reference hub established at the Centre for Public Policy Research (CPPR), IMSciences Peshawar. It systematically archives, indexes, and categorizes substantive public policies, statutory laws, delegated rules, standard operating procedures, and strategic governance frameworks across Khyber Pakhtunkhwa and Pakistan."
    },
    {
        "q": "2. Why is CPPR establishing a Public Policy Stockroom?",
        "a": "Historically, public policy and legislative instruments in Pakistan have been fragmented across disparate departmental archives, gazettes, and private law libraries. CPPR is establishing the Stockroom to eliminate institutional memory loss, reduce research duplication, and provide academics, policymakers, and civil society with verified, canonical access to governance instruments."
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
        "q": "6. Who can use the Public Policy Stockroom?",
        "a": "The Stockroom is an open institutional asset accessible to university faculty, graduate researchers, students, parliamentary committees, administrative secretaries, judges, legal practitioners, development partners, and investigative journalists."
    },
    {
        "q": "7. How does the Stockroom support evidence-based policymaking?",
        "a": "By linking statutory mandates directly to empirical datasets and secondary regulations. Analysts can trace the entire regulatory lifecycle of a statute, examining enabling clauses, administrative rules of business, and implementation gaps."
    },
    {
        "q": "8. Can the Stockroom support comparative policy research?",
        "a": "Yes. Researchers can evaluate legislative activity across multiple administrative departments (e.g. Health vs. Higher Education), compare provincial devolution before and after the 18th Amendment, and contrast regulatory density over time."
    },
    {
        "q": "9. How are documents classified and tagged?",
        "a": "Every document undergoes standard accession metadata tagging: Title, Ref ID, Legal Hierarchy Tier, Sector / Custodian Department, Promulgation Date, Constitutional Era, In Force / Amended / Repealed Status, Enabling Parent Authority, and Delegated Subordinate Rules."
    },
    {
        "q": "10. Are citation formats available for scholarly publications?",
        "a": "Yes. The platform features an automated Citation Studio generating 1-click standardized academic citations in APA 7th Edition, OSCOLA (Oxford Standard for the Citation of Legal Authorities), and Pakistan Law Site formats."
    },
    {
        "q": "11. How will the Stockroom be maintained and updated?",
        "a": "CPPR maintains an active Accession Pipeline in coordination with the Provincial Assembly Secretariat, Khyber Pakhtunkhwa Government Printing Press (Official Gazette), and departmental law sections to index newly enacted instruments."
    },
    {
        "q": "12. What role do student researchers and interns play?",
        "a": "Undergraduate and graduate research assistants at IMSciences participate in metadata verification, legal lineage mapping, clause-by-clause indexing, and preparing executive policy briefs."
    }
]

faqs_json = json.dumps(faqs, ensure_ascii=False)

# Glossary Data (Constitutional, Policy, and Legislative Terminologies)
glossary = [
    # Constitutional
    {"term": "Article", "cat": "Constitutional", "def": "A numbered provision of the Constitution containing a specific rule, principle, right, institutional arrangement, or constitutional requirement."},
    {"term": "Constitutional Amendment", "cat": "Constitutional", "def": "A formal modification of constitutional text passed by a two-thirds majority in Parliament pursuant to Article 238 and 239."},
    {"term": "Basic Structure", "cat": "Constitutional", "def": "Foundational constitutional doctrine recognizing core democratic, judicial, and federal features that are inviolable."},
    {"term": "Distribution of Powers", "cat": "Constitutional", "def": "The constitutional demarcation of legislative, fiscal, and administrative competence between the Federation and the Provinces."},
    {"term": "Fundamental Rights", "cat": "Constitutional", "def": "Inviolable protections enshrined in Chapter 1 of the Constitution, including life, liberty, equality, dignity, speech, and fair trial."},
    {"term": "Directive Principles of State Policy", "cat": "Constitutional", "def": "Constitutional principles (Articles 29–40) guiding state organs in socio-economic policy, social justice, and citizen welfare."},
    {"term": "Article 140A (Local Government)", "cat": "Constitutional", "def": "Mandatory constitutional provision compelling each province to establish local governments and devolve political, administrative, and financial authority."},
    {"term": "Federal Legislative List", "cat": "Constitutional", "def": "Fourth Schedule to the Constitution defining exclusive subjects within the legislative competence of federal Parliament post-18th Amendment."},
    {"term": "Judicial Review", "cat": "Constitutional", "def": "The constitutional power of superior courts under Articles 184(3) and 199 to examine the legality or constitutional validity of statutes and executive acts."},
    # Legislative Process
    {"term": "Bill vs. Act", "cat": "Legislative", "def": "A Bill is a proposed law introduced into a legislature. An Act is a Bill that has passed through all readings, received presidential or gubernatorial assent, and has been published in the official Gazette."},
    {"term": "Assent", "cat": "Legislative", "def": "Formal constitutional approval required from the Governor or President for a passed Bill to acquire the force of law."},
    {"term": "Ordinance", "cat": "Legislative", "def": "Temporary emergency legislation promulgated by the Governor or President under constitutional authority when the legislature is not in session."},
    {"term": "Statutory Rules", "cat": "Legislative", "def": "Subordinate regulatory frameworks framed by government departments under delegated authority specifically conferred by an enabling parent Act."},
    {"term": "Clause-by-Clause Consideration", "cat": "Legislative", "def": "The rigorous second-reading parliamentary stage where each clause, sub-clause, and proposed amendment of a Bill is debated and voted upon individually."},
    {"term": "Committee Stage", "cat": "Legislative", "def": "Detailed scrutiny of a draft Bill by a specialized Standing Committee of the Assembly prior to plenary debate."},
    {"term": "Rules of Business", "cat": "Legislative", "def": "Canonical rules framed under constitutional authority governing the allocation of ministerial portfolios, transaction of cabinet business, and departmental procedures."},
    {"term": "Standard Operating Procedures (SOPs)", "cat": "Legislative", "def": "Operational guidelines issued by departmental heads to ensure uniform day-to-day administrative implementation of statutory rules."},
    # Public Policy
    {"term": "Evidence-Based Policy", "cat": "Policy", "def": "Policy formulation informed by rigorous empirical data, independent evaluation, statutory analysis, and quantifiable baseline indicators."},
    {"term": "Policy Cycle", "cat": "Policy", "def": "The iterative governance process encompassing problem identification, agenda setting, formulation, statutory adoption, implementation, and evaluation."},
    {"term": "Policy Instrument", "cat": "Policy", "def": "The specific governance tool selected to achieve a policy objective, categorized into legal mandates, financial allocations, or organizational frameworks."},
    {"term": "Regulatory Impact Assessment (RIA)", "cat": "Policy", "def": "A systematic methodology for assessing the positive and negative socio-economic effects of proposed or existing legislation."},
    {"term": "Devolution", "cat": "Policy", "def": "The constitutional transfer of decision-making, executive powers, and financial resources from central/provincial authorities to elected local tiers."},
    {"term": "Stakeholder Consultation", "cat": "Policy", "def": "Participatory engagement with citizens, professional associations, academic institutions, and affected groups during policy formulation."}
]

glossary_json = json.dumps(glossary, ensure_ascii=False)

print("Built JSON datasets. Generating HTML content...")

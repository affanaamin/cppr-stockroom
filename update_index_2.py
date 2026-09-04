import sys
import re

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

faq_html = """
    <!-- TAB: FAQs & Glossary -->
    <div id="tabFAQsGlossary" class="tab-content">
      <div style="margin-bottom: 2rem">
        <h2 style="color: #1f4e78; font-size: 1.5rem; margin-bottom: 0.5rem">
          📚 Frequently Asked Questions & Glossary
        </h2>
        <p style="color: var(--muted-color); font-size: 1rem; line-height: 1.6;">
          Find answers to common questions about the CPPR Public Policy Stockroom, and explore key constitutional, policy, and legislative terminologies in Pakistan.
        </p>
      </div>

      <!-- FAQ Section -->
      <h3 class="glossary-section-title" style="margin-top:0;">Frequently Asked Questions (FAQs)</h3>

      <details class="faq-accordion">
        <summary>1. What is the Public Policy Stockroom?</summary>
        <div class="faq-content">
          The Public Policy Stockroom is a centralized reference and resource hub being established at the Centre for Public Policy Research (CPPR). It will bring together public policy, legal, regulatory, constitutional, strategic, and related government documents in one organized platform, making them easier to find, access, study, and use.
        </div>
      </details>

      <details class="faq-accordion">
        <summary>2. Why is CPPR establishing a Public Policy Stockroom?</summary>
        <div class="faq-content">
          Public policy and legal documents in Pakistan are often scattered across government departments, institutions, official websites, libraries, archives, and other sources. Finding relevant documents can therefore be time-consuming and difficult.<br><br>
          The Stockroom is intended to address this challenge by creating a single, organized point of reference for public policy-related information and documentation.
        </div>
      </details>

      <details class="faq-accordion">
        <summary>3. What is the main purpose of the Stockroom?</summary>
        <div class="faq-content">
          The primary purpose is to establish a centralized, organized, and regularly updated repository of Pakistan's public policy and related legal documents.<br><br>
          It will help users locate relevant information more efficiently and provide easier access to the primary documents needed for policy research, analysis, education, and practice.
        </div>
      </details>

      <details class="faq-accordion">
        <summary>4. What types of documents will the Stockroom contain?</summary>
        <div class="faq-content">
          The Stockroom is planned to include a broad range of public policy and legal resources, including:
          <ul style="margin-top: 0.5rem; margin-left: 1.5rem;">
            <li>Public policies</li>
            <li>Laws and Acts</li>
            <li>Constitutional provisions and amendments</li>
            <li>Rules of Business</li>
            <li>Standard Operating Procedures (SOPs)</li>
            <li>Government strategies and plans</li>
            <li>International treaties and conventions</li>
            <li>Pakistan's international legal commitments</li>
            <li>Historical policy documents</li>
            <li>Other relevant policy and regulatory instruments</li>
          </ul>
        </div>
      </details>

      <details class="faq-accordion">
        <summary>5. What period will the Stockroom initially cover?</summary>
        <div class="faq-content">
          The initial focus will be on the post-18th Constitutional Amendment period, beginning in 2010. This period is particularly significant because the 18th Amendment brought important changes to the distribution of legislative and administrative responsibilities.<br><br>
          The Stockroom will subsequently expand to cover policy and legal instruments dating back to 1947, and, where feasible, relevant pre-partition documents.
        </div>
      </details>

      <details class="faq-accordion">
        <summary>6. How will the Stockroom be organized?</summary>
        <div class="faq-content">
          The primary organizing principle will be sector-wise categorization. This will allow users to navigate directly to the area of public policy relevant to their interests or work.<br><br>
          Within each sector, resources may be further organized into categories such as laws and Acts, constitutional provisions, policies, strategies, international treaties, historical documents, and other regulatory instruments.
        </div>
      </details>

      <details class="faq-accordion">
        <summary>7. Who can use the Public Policy Stockroom?</summary>
        <div class="faq-content">
          The Stockroom is intended to serve a broad range of users, including students, researchers, faculty members, universities, academic institutions, public policy practitioners, government departments, policymakers, public officials, journalists, media professionals, UN agencies, NGOs, civil society organizations, and other individuals and institutions working on public policy and governance.
        </div>
      </details>

      <details class="faq-accordion">
        <summary>8. How will researchers and academics benefit?</summary>
        <div class="faq-content">
          Researchers and academics will have access to a more organized collection of primary policy and legal sources. This can reduce the time spent searching across multiple sources and support evidence-based research, policy analysis, comparative research, and academic work.
        </div>
      </details>

      <details class="faq-accordion">
        <summary>9. How will the Stockroom support evidence-based policymaking?</summary>
        <div class="faq-content">
          Evidence-based policymaking depends on access to reliable primary sources. By bringing original laws, Acts, policies, strategies, and international commitments together in an organized repository, the Stockroom will make it easier for users to consult primary documents rather than relying solely on secondary interpretations.
        </div>
      </details>

      <details class="faq-accordion">
        <summary>10. What is the long-term vision for the Stockroom?</summary>
        <div class="faq-content">
          The long-term vision is to establish a comprehensive, accessible, and regularly updated Public Policy Stockroom at CPPR that serves as a trusted reference and resource hub for public policy research and practice.<br><br>
          Over time, it is intended to bring together Pakistan's contemporary and historical public policy, legal, regulatory, and international commitment landscape in one accessible location.
        </div>
      </details>

      <!-- Glossary Section 1: Constitutional Wordlist -->
      <h3 class="glossary-section-title">Constitutional Terminology</h3>
      <div class="glossary-grid">
        <div class="glossary-card">
          <h4>Constitution</h4>
          <p>The supreme legal framework of Pakistan. It establishes the structure of the State, defines powers and responsibilities of institutions, provides for fundamental rights, and sets out the relationship between the federation and provinces.</p>
        </div>
        <div class="glossary-card">
          <h4>Amendment</h4>
          <p>A formal change made to the Constitution through the special procedure prescribed by the Constitution.</p>
        </div>
        <div class="glossary-card">
          <h4>Basic Structure</h4>
          <p>A general constitutional concept referring to fundamental features of a constitution that are considered foundational.</p>
        </div>
        <div class="glossary-card">
          <h4>Distribution of Powers</h4>
          <p>The constitutional allocation of legislative, executive, and other governmental powers among the federation and provinces and among State institutions.</p>
        </div>
        <div class="glossary-card">
          <h4>Fundamental Rights</h4>
          <p>Rights guaranteed by the Constitution, including protections relating to life, liberty, equality, dignity, freedom, and other constitutional rights, subject to constitutional limitations.</p>
        </div>
        <div class="glossary-card">
          <h4>Parliamentary Democracy</h4>
          <p>A system of government in which the executive is politically responsible to the elected legislature within the constitutional framework.</p>
        </div>
      </div>

      <!-- Glossary Section 2: Policy Wordlist -->
      <h3 class="glossary-section-title">Public Policy Terminology</h3>
      <div class="glossary-grid">
        <div class="glossary-card">
          <h4>Public Policy</h4>
          <p>A course of action, framework, or set of decisions adopted or pursued by government to address public problems and achieve public objectives.</p>
        </div>
        <div class="glossary-card">
          <h4>Evidence-Based Policy</h4>
          <p>Policy development or decision-making informed by credible evidence, research, data, analysis, and documented experience.</p>
        </div>
        <div class="glossary-card">
          <h4>Action Plan</h4>
          <p>A practical document setting out specific activities, responsibilities, timelines, and sometimes indicators for implementing a policy or strategy.</p>
        </div>
        <div class="glossary-card">
          <h4>Policy Cycle</h4>
          <p>A conceptual framework describing stages through which public policy may progress, such as problem identification, agenda-setting, formulation, adoption, implementation, monitoring, and evaluation.</p>
        </div>
        <div class="glossary-card">
          <h4>Regulation</h4>
          <p>A binding rule or requirement issued by a competent authority under legal authority to govern particular activities, conduct, or sectors.</p>
        </div>
        <div class="glossary-card">
          <h4>Stakeholder</h4>
          <p>An individual, group, institution, or organization that is affected by, has an interest in, or can influence a policy, programme, or decision.</p>
        </div>
      </div>

      <!-- Glossary Section 3: Legislative Process Wordlist -->
      <h3 class="glossary-section-title">Legislative Process Terminology</h3>
      <div class="glossary-grid">
        <div class="glossary-card">
          <h4>Bill vs. Act</h4>
          <p>A <strong>Bill</strong> is a proposed law introduced in Parliament or a Provincial Assembly. An <strong>Act</strong> is a Bill that has completed the required legislative process and received the necessary assent, thereby becoming law.</p>
        </div>
        <div class="glossary-card">
          <h4>Assent</h4>
          <p>Formal constitutional approval of a Bill after it has been passed through the required legislative stages.</p>
        </div>
        <div class="glossary-card">
          <h4>Ordinance</h4>
          <p>A temporary law promulgated under constitutional authority when the relevant legislature is not in session and the prescribed constitutional conditions are met.</p>
        </div>
        <div class="glossary-card">
          <h4>Committee Stage</h4>
          <p>The stage at which a Bill is examined in detail by the relevant parliamentary committee, where applicable.</p>
        </div>
      </div>
    </div>
"""

# Insert the HTML block before <!-- TAB 6: CONTACT & ABOUT CPPR -->
if 'id="tabFAQsGlossary"' not in content:
    content = content.replace('<!-- TAB 6: CONTACT & ABOUT CPPR -->', faq_html + '\n    <!-- TAB 6: CONTACT & ABOUT CPPR -->')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected HTML successfully.")

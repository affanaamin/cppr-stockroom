import sys

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS
css_to_insert = '''
      /* FAQ & Glossary Styling */
      .faq-accordion {
        margin-bottom: 1rem;
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        box-shadow: var(--shadow-sm);
        overflow: hidden;
        transition: box-shadow 0.2s ease, transform 0.2s ease;
      }
      .faq-accordion:hover {
        box-shadow: var(--shadow-md);
      }
      .faq-accordion summary {
        padding: 1.25rem 1.5rem;
        font-size: 1.05rem;
        font-weight: 600;
        color: #1f4e78;
        cursor: pointer;
        list-style: none;
        display: flex;
        justify-content: space-between;
        align-items: center;
        user-select: none;
      }
      body.dark-mode .faq-accordion summary {
        color: #60a5fa;
      }
      .faq-accordion summary::-webkit-details-marker {
        display: none;
      }
      .faq-accordion summary::after {
        content: '▼';
        font-size: 0.8rem;
        transition: transform 0.3s ease;
      }
      .faq-accordion[open] summary::after {
        transform: rotate(180deg);
      }
      .faq-accordion .faq-content {
        padding: 0 1.5rem 1.25rem 1.5rem;
        font-size: 0.95rem;
        color: var(--text-color);
        line-height: 1.6;
        border-top: 1px solid var(--border-color);
        margin-top: 0.5rem;
        padding-top: 1rem;
      }
      .glossary-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.2rem;
      }
      .glossary-card {
        background: var(--card-bg);
        border-left: 4px solid #1f4e78;
        border-top: 1px solid var(--border-color);
        border-right: 1px solid var(--border-color);
        border-bottom: 1px solid var(--border-color);
        border-radius: 10px;
        padding: 1.2rem;
        transition: transform 0.2s ease;
      }
      body.dark-mode .glossary-card {
        border-left-color: #3b82f6;
      }
      .glossary-card:hover {
        transform: translateX(3px);
        box-shadow: var(--shadow-sm);
      }
      .glossary-card h4 {
        color: #1f4e78;
        font-size: 1.05rem;
        margin-bottom: 0.5rem;
        font-weight: 700;
      }
      body.dark-mode .glossary-card h4 {
        color: #60a5fa;
      }
      .glossary-card p {
        font-size: 0.9rem;
        color: var(--text-color);
        line-height: 1.5;
      }
      .glossary-section-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: var(--text-color);
        margin: 2.5rem 0 1.5rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid var(--border-color);
      }
'''
if '/* FAQ & Glossary Styling */' not in content:
    content = content.replace('</style>', css_to_insert + '\n    </style>', 1)

# 2. Add Tab Button
tab_btn = '''      <button class="tab-btn" onclick="switchTab('tabFAQsGlossary')">
        📚 FAQs & Glossary
      </button>
      <button class="tab-btn" onclick="switchTab('tabContact')">'''

if "switchTab('tabFAQsGlossary')" not in content:
    content = content.replace('''      <button class="tab-btn" onclick="switchTab('tabContact')">''', tab_btn)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Script finished')

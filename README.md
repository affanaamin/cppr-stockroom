# CPPR Public Policy Stockroom
### Centre for Public Policy Research (CPPR) — Institute of Management Sciences (IMSciences), Peshawar

A centralized, empirical digital repository and analytical stockroom cataloguing **1,374 substantive public policy instruments**, primary statutes, statutory rules, regulations, sector strategies, and standard operating procedures (SOPs) across all 28 administrative departments of the Government of Khyber Pakhtunkhwa.

---

## 🏛️ Core Architecture & Governance Standard

The stockroom adheres strictly to the **15-Level Master Legal Hierarchy & Policy-to-Implementation Chain** and the **20-Column Relational Schema**:

1. **`ID`**: Unique sequential master identifier (`1` to `1,374`)
2. **`Document Title`**: Standardized legal title (Title Cased, clean legal nomenclature)
3. **`Category`**: 15 Regulatory Hierarchy Levels *(Acts, Rules, Rules of Business, Policies, SOPs, Plans)*
4. **`Jurisdiction`**: Provincial (*Khyber Pakhtunkhwa*) / Federal (*Pakistan*)
5. **`Geographical Scope`**: Provincial / District / Local Councils / National
6. **`Sector / Department`**: 28 Official KP Government Departments
7. **`Institution`**: Designated Administrative Department / Secretariat Body
8. **`Issuing Authority`**: Enacting Legislature / Executive Department
9. **`Enactment Date`**: Gazetted promulgation date
10. **`Year`**: Enactment year
11. **`Constitutional Era`**: 4 Historical Constitutional Eras
    * *Post-18th Amendment (2010 – Present)*
    * *Post-1973 Constitution Era (1973 – 2009)*
    * *Post-Independence Era (1947 – 1972)*
    * *Pre-Partition Era (Pre-1947)*
12. **`Legal Status`**: Operative legal status (*Active / Enacted / Amended / Repealed*)
13. **`Legal Authority`**: Enabling constitutional or statutory authority
14. **`Parent Document`**: Parent primary law or constitutional article
15. **`Policy Link`**: Associated sectoral reform policy or strategy roadmap
16. **`Implementation Link`**: Operational guidelines and implementation SOPs
17. **`Related Documents`**: Subordinate regulations, by-laws, and amendment acts
18. **`Executive Policy Brief`**: Formatted executive policy summary
19. **`Keyword Tags`**: Structured thematic keywords
20. **`Source / Drive URL`**: Verified document link / official gazette PDF

---

## 📊 Repository Summary

| Legal Hierarchy Tier | Category | Count |
| :---: | :--- | :---: |
| **Level 5** | Acts / Statutes / Legislation / Ordinances | **814** |
| **Level 6** | Statutory Rules & Regulations / By-Laws | **227** |
| **Level 8** | Sector Policies & Strategies | **144** |
| **Level 12** | Guidelines, SOPs & Administrative Manuals | **103** |
| **Level 7** | KP Rules of Business 1985 & Conduct Rules | **69** |
| **Level 1** | Constitutional Framework & Amendments | **16** |
| **Level 10** | Plans & Action Plans | **12** |
| **Level 4** | International Commitments | **1** |
| **Level 14** | Monitoring & Evaluation Framework | **1** |
| **Total** | **Strictly Substantive Policy Documents** | **1,374** |

---

## 📂 Deliverables & File Structure

```
cppr-stockroom/
├── index.html                               # Interactive CPPR Web Portal & Visual Analytics
├── documents_data.js                        # Master Portal JavaScript Dataset (1,374 records)
├── documents.json                           # Clean 20-Column Relational JSON Repository
├── cppr.db                                  # Relational SQLite Database
├── CPPR_Master_Inventory.xlsx               # 4-Tab Formatted Master Excel Workbook
├── CPPR_Documents.xlsx                      # Clean Distribution Spreadsheet
├── CPPR_All_Policy_Documents_Compiled.txt   # Master Text Compilation & Executive Briefs (2.6 MB)
├── README.md                                # Repository Documentation
├── requirements.txt                         # Python Dependencies
├── assets/                                  # CSS, Icons, & Static Assets
└── archive/                                 # PDF Archive & Pipeline Scripts
```

---

## 🚀 Running the Stockroom Portal

1. **Direct Web Access:** Open [`index.html`](file:///c:/Users/Affan/Desktop/cppr-stockroom/index.html) in any modern web browser.
2. **Local Python Server (Optional):**
   ```bash
   python -m http.server 8000
   ```
   Then navigate to `http://localhost:8000` in your browser.

---

### © Centre for Public Policy Research (CPPR) — IMSciences Peshawar
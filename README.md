# Data Engineer  -  Study Library

A curated collection of **52 study files** (49 PDFs + Python script + JSON + reference link) covering SQL, PySpark, Python, Azure Databricks, Azure Data Factory, Data Modeling, ETL, and Data Engineering interview prep.

**Live site (GitHub Pages):** https://munibk.github.io/DataEngineering/

The repository ships with a single-file dashboard (`index.html`) that lets you:

- Browse all files by **content topic** or **folder**
- Search across names, paths, and topics
- Track your reading progress (Unread / In progress / Done) per file  -  saved in your browser
- Spot mis-named or misfiled content via visible badges

---

## Quick stats

| | |
|---|---|
| Total files | **52** |
| Total size | **~200 MB** |
| Folders | **9** (`Interview`, `Project`, `Python`, `Spark`, `sql`, `Text`, `Tools/ADB`, `Tools/ADF`, `others`) |
| Topics (content-based) | **19** |
| Misfiled / misnamed / duplicate | **8** (see flags table below) |

---

## Heads-up  -  flags

After reading every PDF, these files were flagged because their filename does not match the actual content:

| File | Flag | What it actually is |
|---|---|---|
| `Spark/1744697184048.pdf` | `MISFILED` | A **Data Engineering File Types** cheat-sheet (CSV/Parquet/Avro). Nothing Spark-specific. |
| `sql/INTRO_2.pdf` | `MISNAMED` | Not an SQL intro  -  it's a **Window Functions Zero-to-Hero** deep dive (28 pg). |
| `Spark/L1.pdf` | `MISNAMED` | Not "Lesson 1"  -  it's the **Top 100 PySpark Functions** reference. |
| `Spark/Data Engineer .pdf` | `MISNAMED` | A **PySpark Scenario Q&A** (Nitya CloudTech), not generic DE notes. |
| `Spark/Senario_based_tcs.pdf` | `MISNAMED` | Not TCS-specific  -  it's by Prominent Academy, covering streaming/fraud detection. |
| `Spark/Senario_based.pdf` | `DUPLICATE` | Same content as `Spark/Data Engineer .pdf`. |
| `Spark/DAG.pdf` | `IMAGE-ONLY` | No extractable text  -  slide diagrams only. |
| `Tools/ADB/ADB_2.pdf` | `NARROW` | Just Part 9 of a Delta Lake series ("Deletion Vectors")  -  narrow scope, not a general ADB doc. |

---

## Content categorization

### SQL

#### 1. SQL Intro & Reference
| File | What's inside |
|---|---|
| `sql/INTRO_1.pdf` | SQL Q&A fundamentals  -  keys, normalization (1NF - 5NF), joins, DELETE vs TRUNCATE, UNION (24 pg) |
| `sql/INTRO_3.pdf` | SQL Commands Reference  -  DDL / DML / DCL / TCL / DQL (56 pg) |
| `sql/INTRO_4.pdf` | Zero-to-Advance SQL  -  30-Day Plan (45 pg) |

#### 2. SQL Window Functions
| File | What's inside |
|---|---|
| `sql/INTRO_2.pdf` ? misnamed | SQL Window Functions Zero-to-Hero by Shailesh  -  OVER(), PARTITION BY, frames, LAG/LEAD, running totals (28 pg) |
| `sql/WFSQL.pdf` | 5 Essential SQL Window Functions by Dawn Choo (14 pg) |

#### 3. SQL Advanced Topics
| File | What's inside |
|---|---|
| `sql/CTE_VS_Sub_query.pdf` | CTE vs Subqueries comparison by Tushar Wagh |
| `sql/SSP.pdf` | SQL Stored Procedures  -  comprehensive guide (Raghavendra) |
| `sql/sql_optimization.pdf` | Query Optimization  -  indexing, refactoring, execution plans |

#### 4. SQL Practice & Interview
| File | What's inside |
|---|---|
| `sql/INTERVIEW_QUESTIONS.pdf` | Accenture Data Analyst SQL Questions (1 - 4 YoE, 9 - 13 LPA) |
| `sql/QUESTIONS.pdf` | LeetCode-style Database Problems with full schemas (105 pg) |
| `sql/QUESTIONS_1.pdf` | 10 Complex SQL Queries Every Developer Should Master (Learnbay) |

### PySpark / Spark

#### 5. PySpark Intro & Architecture
| File | What's inside |
|---|---|
| `Spark/Apachesparkbeg.pdf` | Apache Spark for Beginners  -  genesis, Hadoop, RDD, DAG, architecture (30 pg) |
| `Spark/INTRO.pdf` | Day 1  -  PySpark & Databricks Architecture (Swapnil Thorat) |
| `Spark/pyspark_1.pdf` | What is PySpark?  -  Py4J, RDDs, basics (Udaya G, 31 pg) |
| `Spark/1744854540663.pdf` | PySpark tutorial  -  SparkSession, DataFrames, key functions (16 pg) |
| `Spark/pyspark122page.pdf` | Master Spark  -  One Post to Rule Them All  -  5Vs / RDD / DAG / shuffling / lazy eval (112 pg) |
| `Spark/DAG.pdf` ? image-only | Spark DAG slides (no extractable text) |

#### 6. PySpark Functions Reference
| File | What's inside |
|---|---|
| `Spark/L1.pdf` ? misnamed | Top 100 PySpark Functions Reference (30 pg) |
| `Spark/pysparkfunctions.pdf` | Top 50 Most-Used PySpark Functions (11 pg) |

#### 7. PySpark Tips & Optimization
| File | What's inside |
|---|---|
| `Spark/pysparktrciks.pdf` | 12 PySpark Tricks  -  selectExpr, broadcast, cache, explode, coalesce (Karthik Kondpak) |

#### 8. PySpark / Spark Interview Q&A
| File | What's inside |
|---|---|
| `Spark/interview_question.pdf` | Top 50 PySpark Interview Q&A  -  Jay C  -  Azure DE prep (57 pg) |
| `Spark/interview_question_1.pdf` | Top 50+ Apache Spark Interview Q&A  -  Spark Core / Streaming / SQL / GraphX / MLlib (25 pg) |
| `Spark/interview_question_2.pdf` | DE Interview Scenarios  -  partitioning, data skew, repartition vs coalesce, AQE |

#### 9. PySpark Scenario-Based
| File | What's inside |
|---|---|
| `Spark/Data Engineer .pdf` ? misnamed | PySpark Scenario Q&A by Nitya CloudTech |
| `Spark/Senario_based.pdf` ?? duplicate | Same content as above |
| `Spark/Senario_based_tcs.pdf` ? misnamed | Real-time Streaming Scenarios by Prominent Academy  -  watermarking, sliding windows, fraud detection, broadcast, bloom filters |

#### 10. SQL ? PySpark Mapping
| File | What's inside |
|---|---|
| `Spark/SQLVSSPARK.pdf` | Spark DataFrame API vs Spark SQL  -  side-by-side cheat sheet (11 pg) |
| `Spark/SQLVSSPARK_1.pdf` | SQL ? PySpark DML equivalents  -  Atharva Jirafe (8 pg) |

### Python

#### 11. Python Practice & Interview
| File | What's inside |
|---|---|
| `Python/1703635703555.pdf` | 140+ Basic Python Programs (Jupyter-notebook style, 96 pg) |
| `Python/1743143545317.pdf` | Most-Asked Python Interview Q&A  -  data types, OOP, lambdas, pandas/numpy (26 pg) |
| `Python/interview_practice.py` | Your own practice file  -  `prime_number`, `palindrome`, `vowel_replace_space` |
| `Python/test.json` | Sample JSON read by the practice script |

### Azure / Cloud

#### 12. Azure DE Interview
| File | What's inside |
|---|---|
| `Interview/INTERVIEW_QUESTIONS.pdf` | Azure DE Interview Q&A  -  Topicwise  -  PySpark / SQL / Databricks / ADF / ADLS / Python / Data Modeling (57 pg) |
| `Interview/INTERVIEW_QUESTIONS_1.pdf` | Azure DE Interview Q&A  -  Companywise  -  14 companies including Tiger Analytics, Deloitte, KPMG, TCS, Cognizant (68 pg) |
| `Interview/Top 52 Azure Data Engineering Questions & Answers guide.pdf` | Top 52 Azure DE Q&A  -  ADF, time travel, medallion, Unity Catalog, SCD, clusters (14 pg) |

#### 13. Azure Databricks
| File | What's inside |
|---|---|
| `Tools/ADB/ADB_1.pdf` | Intro to Azure Databricks  -  Praveen Patel (8 pg) |
| `Tools/ADB/ADB_2.pdf` ? narrow | Lakehouse Part 9  -  Delta Lake Deletion Vectors (Anil Reddy) |
| `Tools/ADB/Exam.pdf` | Databricks Certified DE Associate  -  Official Practice Exam, 45 Q with answers |
| `Tools/ADB/interviewquestions.pdf` | Databricks DE Associate Practice Bank  -  105 pg comprehensive Q bank (Sourav Banerjee) |

#### 14. Azure Data Factory
| File | What's inside |
|---|---|
| `Tools/ADF/1.pdf` | ADF Scenario 29  -  Bulk Copy Multiple Tables: Azure SQL DB ? ADLS (Lookup + ForEach + Copy) |
| `Tools/ADF/2.pdf` | ADF Scenario 15  -  Copy data from REST API ? Azure Data Lake |
| `Tools/ADF/ADF.txt` | LinkedIn URL reference (Praveen Patel) |

### Foundational Concepts

#### 15. Data Engineering Concepts
| File | What's inside |
|---|---|
| `others/DET.pdf` | Data Engineering Terms Glossary  -  pipelines, ETL vs ELT, Lake/Warehouse/Mart (12 pg) |

#### 16. Data Cleaning
| File | What's inside |
|---|---|
| `others/DC.pdf` | Data Cleaning with SQL  -  COALESCE / IFNULL / ISNULL (Muhammad Umar Hanif) |
| `others/DC_1.pdf` | Data Cleaning  -  Brief Guide (Artists of Data Science)  -  3-step process |

#### 17. Data Modeling
| File | What's inside |
|---|---|
| `others/DM.pdf` | Data Modeling  -  Conceptual/Logical/Physical, keys, normalization (Raushan Kumar) |
| `others/DM_1.pdf` | Data Modeling  -  Visual Foundation by codebasics.io |

#### 18. File Types & Storage
| File | What's inside |
|---|---|
| `Spark/1744697184048.pdf` ? misfiled | DE File Types Cheat Sheet  -  CSV, TSV, JSON, XML, Parquet, Avro, ORC, Excel |

### Reading

#### 19. eBooks & Long-form
| File | What's inside |
|---|---|
| `Text/BD_TEXT.pdf` | The Big Book of Data Engineering  -  3rd Ed (Databricks, 125 pg)  -  DLT, Unity Catalog, Auto Loader, Streaming + 5 case studies |
| `Text/DE_TEXT.pdf` | Delta Lake: Up and Running (O'Reilly Early Release, Bennie Haelen)  -  Lakehouse, Delta Lake transaction log, medallion (56 pg) |
| `Text/ETL_TEXT.pdf` | Understanding ETL (O'Reilly Early Release, Matt Palmer)  -  fundamentals, ingestion patterns (34 pg) |

### Project Ideas

#### 20. Project Resource Links
| File | What's inside |
|---|---|
| `Project/1742186639894.pdf` | 10 FREE Data Analytics Projects  -  curated GitHub + YouTube links |

---

## Suggested study path

If you're prepping for an Azure DE interview from scratch, the following order works well:

1. **Foundations**  -  `others/DET.pdf` (glossary), `others/DM.pdf` + `others/DM_1.pdf` (modeling), `Text/ETL_TEXT.pdf` (ETL)
2. **SQL**  -  `sql/INTRO_1.pdf` ? `sql/INTRO_3.pdf` ? `sql/INTRO_2.pdf` (window functions, even though misnamed) ? `sql/SSP.pdf` + `sql/CTE_VS_Sub_query.pdf` ? `sql/sql_optimization.pdf` ? `sql/QUESTIONS.pdf` (practice)
3. **PySpark**  -  `Spark/Apachesparkbeg.pdf` ? `Spark/pyspark_1.pdf` ? `Spark/INTRO.pdf` ? `Spark/pyspark122page.pdf` (deep dive) ? `Spark/L1.pdf` (function reference)
4. **Azure**  -  `Text/DE_TEXT.pdf` (Delta Lake book) ? `Tools/ADB/ADB_1.pdf` ? `Tools/ADF/1.pdf` + `Tools/ADF/2.pdf` ? `Text/BD_TEXT.pdf` (Databricks ebook)
5. **Interview prep**  -  `Interview/INTERVIEW_QUESTIONS.pdf` (topic-wise) ? `Interview/INTERVIEW_QUESTIONS_1.pdf` (company-wise) ? `Spark/interview_question.pdf` + `Spark/interview_question_2.pdf` (scenarios)
6. **Cert (optional)**  -  `Tools/ADB/Exam.pdf` + `Tools/ADB/interviewquestions.pdf`

---

## How to use `index.html`

Open the live site at https://munibk.github.io/DataEngineering/ (or open `index.html` locally with a double-click).

- **Search bar**  -  type any keyword (matches name, path, topic, or flag)
- **Topic dropdown**  -  filter by real content (e.g. "SQL Window Functions", "PySpark Scenarios")
- **Status dropdown**  -  show only Unread / In progress / Done files
- **Status circle** on each card  -  click to cycle reading status
- **Reset progress**  -  button in the header (with confirmation)

Progress is saved in your browser's `localStorage`, so it persists across page reloads but is per-device.

---

## Tech notes

- **No build step**  -  pure HTML/CSS/JavaScript, no dependencies
- **Works offline**  -  open `index.html` locally
- **Pages deploy**  -  `.nojekyll` skips Jekyll for fast static serving

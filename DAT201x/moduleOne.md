## Introduction

### SELECT
**SELECT**: Specifies columns to display
- all columns in a table, specific columns, columns from multiple tables, literal values, expressions

### Clause Execution Order
<img src="https://raw.githubusercontent.com/TAPEZONE128/270125units/refs/heads/main/DAT201x/images/diagram-export%20(1).png" length="300" width="300"/>

### SELECT Statement Clauses
1. **FROM** Clause - Determines where data originates
2. **WHERE** Clause - Filters rows based on conditions
3. **GROUP BY** Clause - Groups results by specific columns
4. **HAVING** Clause - Filters aggregated groups, Applied after grouping
5. **ORDER BY** Clause - Sorts results explicitly, ascending/descending sorting

### Best Practices for SELECT Queries
- Avoid SELECT * (Star) Queries

**Risks of Using SELECT:**
- Table structure changes can break queries
- Unnecessary data transfer
- Less explicit column control

### Advanced SELECT Techniques
**Column Aliasing**
``` sql
SELECT name AS product,  list_price * 0.9 AS sale_price
```
**Alias Benefits:**
- Rename columns for clarity
- Perform calculations
- Create more meaningful column names
  
---

## SQL (Structure Query Language)
- **Origin:** Developed by IBM in the 1970s for database interrogation
**Standardization:**
- Adopted by American National Standards Institute (ANSI)
- Internationally recognized standard

### **Microsoft's Implementation:** Transact SQL (T-SQL)
**Characteristics:**
- Largely similar to other SQL platforms
- Contains Microsoft-specific extensions
- Used in SQL Server and Azure SQL Database

### Platform Differences
| Platform | Full Support | Limitations |
|----------|--------------|-------------|
| SQL Server | Complete T-SQL features | Local file interactions |
| Azure SQL Database | Large subset of features | Some server-specific functionalities restricted |

### SQL Language Characteristics
- **Language Type** - Declarative, Not Procedural
- **Key Principles** - dataset, not individual rows; describing desired result; mathematical set theory

### Declarative Language Approach
<img src="https://raw.githubusercontent.com/TAPEZONE128/270125units/refs/heads/main/DAT201x/images/image.png" length="500" width="500"/>

### Relational Database Fundamentals
**Core Concepts:**
- Multiple interconnected tables
- Each table represents a specific entity
- Normalized data structure 

### Key Database Design Elements
- **Primary Key:** Unique identifier for each table row
- **Foreign Key:** Establishes relationships between tables
- **Normalization:** Reduces data redundancy

### Database Object Organization
- **Schemas:** Namespace for organizing database objects
**Fully Qualified Object Name Structure:**
  - Server Name
  - Database Name
  - Schema Name
  - Object Name

### Schema Example
<img src="https://raw.githubusercontent.com/TAPEZONE128/270125units/refs/heads/main/DAT201x/images/diagram-export.png" length="500" width="500"/>

### SQL Statement Types
**Data Manipulation Language (DML)**
- Querying databases
- Updating data
- Deleting data

### Other SQL Language Categories
1. DDL (Data Definition Language)
- Creating databases
- Altering structures
- Dropping objects
2. DCL (Data Control Language)
- Setting permissions
- Securing database objects











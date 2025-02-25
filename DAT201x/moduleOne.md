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
- Avoid `SELECT *` Queries

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
  
---
## SQL SELECT Queries

### Database Context and Connection 
**Key Concept: Selecting the Correct Database**
- Default connection is often to the `master` system database
- Switching databases prevents potential errors like "object not found"

### Basic SELECT Statements 
**SELECT Statement Fundamentals**
  - Basic syntax: `SELECT [columns] FROM [table]`
  - `SELECT *` retrieves all columns (not recommended as a best practice)
  - Specify exact columns needed for efficiency

### Best Practices for SELECT Queries
**Column Selection**
  - Avoid `SELECT *`
  - Explicitly list required columns
  - Improves query performance and readability

### Column Aliases and Expressions
**Creating Calculated Columns**
  - Use mathematical operations within SELECT
  - Assign meaningful names using `AS` keyword
  - Example: `ListPrice - StandardCost AS Margin`

### Alias Naming Conventions
**Recommended Practices**
  - Always use `AS` when naming columns
  - Prevents accidental column name misassignment
  - Provides clarity in query results

### Data Type and Concatenation Behaviors
**String and Numeric Interactions**
  - String concatenation uses + operator
  - Numeric addition requires compatible data types
  - `NULL` values propagate through calculations

### Null Handling Rules
**NULL Value Characteristics**
  - Represents "unknown" value
  - Any calculation involving `NULL` results in NULL
  - Not treated as empty string or zero

### Data Type Compatibility Table
| Operation | Behavior | Example |
|-----------|----------|---------|
| String + String | Concatenation | 'Black' + '58' = 'Black58' |
| Number + String | Error | Incompatible types |
| Any + NULL | Results in NULL | x + NULL = NULL |

### Common Pitfalls to Avoid
- Forgetting commas in column lists
- Using `SELECT *` in production queries
- Ignoring data type compatibility
- Not handling `NULL` values appropriately

### Practical Query Writing Tips
- Use semicolons to terminate statements
- Be explicit about column selection
- Consider performance implications
- Validate data type compatibility

### Mermaid Diagram: Query Construction Workflow
<img src="https://github.com/TAPEZONE128/270125units/blob/main/DAT201x/images/diagram-export%20(2).png" length="300" width="300"/>

---

## Data Type Conversion in SQL: CAST and CONVERT Functions

### Introduction to Data Type Conversion
- Fundamental technique for transforming data between different types in SQL
- Critical for data manipulation and compatibility between different data formats

## CAST Function Basics

### Key Characteristics
- Converts numeric values to character strings
- Allows concatenation of different data types
- Prevents type mismatch errors during data operations

### Practical Example
- Converting Product ID from number to varchar
- Enables string concatenation with product names
- Important: Prevents concatenation errors between numbers and strings 

## `CONVERT` Function

### Similarities and Differences with CAST
- Performs similar data type conversions
- Provides more flexibility, especially with date formatting
- Offers additional conversion options

### Date Conversion Techniques
- Converts dates to different string representations
- Uses specific format codes for standardization
- **ISO Standard Format Code 126:** Provides universal date representation

## Date Conversion Formats
| Format Code | Description | Example |
|-------------|-------------|---------|
| Default | Basic date/time | 2023-05-15 10:30 AM |
| 126 | ISO Standard | 2023-05-15T10:30:00 |

## Numeric Casting Challenges

### Handling Mixed Data Types
- Some columns contain both numeric and text values
- Direct integer casting can cause conversion errors
- **Solution:** Conditional casting with null handling 

### Casting Strategy
- Attempt to convert numeric values
- Return null for non-convertible entries
- Provides flexible data transformation approach

### Potential Conversion Strategies
<img src="https://github.com/TAPEZONE128/270125units/blob/main/DAT201x/images/diagram-export%20(3).png" length="500" width="500"/>

### Advanced Considerations
- Different systems may handle conversions differently
- Client applications might interpret converted data uniquely
- Always test conversions in target environment

---
## Introduction to Transact SQL (T-SQL)
- Foundational database querying language
- Part of Microsoft SQL Server ecosystem
- Designed for managing and manipulating relational database information

### Basic SELECT Statement 
**Key Capabilities**
  - **Select All Rows:** Retrieve entire dataset
  - **Column Selection:** Choose specific columns for output
  - **Column Aliasing:** Rename columns for clarity and readability

**Data Manipulation Techniques**
  - **Expressions:** Calculate values during query execution
  - Data Type Conversion:
    1. String to Number
    2. Number to String
    3. Date to String transformations

**Null Value Handling**
  - **Null Concept:** Represents unknown or missing information
  - Strategies for managing null values in queries
  - Importance of understanding null's unique behavior in database operations

---

## Learning Recommendations

### Practical Learning Approach
**Lab Exercise:**
  - Download lab instructions
  - Set up Azure SQL Database
  - Complete challenge scenarios
  - Compare solutions with provided answer files

### Recommended Study Workflow
<img src="https://github.com/TAPEZONE128/270125units/blob/main/DAT201x/images/diagram-export%20(4).png" length="300" width="300"/>

### Key Terminology Table
| Term | Definition | Context |
|------|------------|---------|
| SELECT | Primary query command | Retrieving database data |
| Alias | Column/table nickname | Improving query readability |
| Null | Unknown value |Representing missing information |
| Expression | Calculated value | Deriving new data during query |

---

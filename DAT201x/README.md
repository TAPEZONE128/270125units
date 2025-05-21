# Data Query with Transact SQL (T-SQL)

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

## Understanding Null Values in Databases

### What is a Null Value? 
  - **Definition:** A null value represents an unknown or missing data point
  - **Key Distinctions:**
    - Not an empty string
    - Not zero
    - Not "nothing"
    - Represents a state of information absence

### ANSI Null Behavior Standards 
**Standard Null Handling Rules**
  - Any expression involving a null results in null
  - Example Scenarios:
    - Adding something to an unknown value = unknown
    - Concatenating strings with null = null
  - Recommended Practice:
    - Keep standard null handling enabled
    - Avoid custom null interpretation settings

## Comparing Null Values 

### Null Comparison Challenges
**Comparing two null values yields:**
  - Technically "unknown"
  - Practically treated as false

- Cannot definitively determine equality between nulls

### Checking for Null Values 
**Proper Null Identification**
  - **Correct Method:** Use `IS NULL`
  - **Incorrect Method:** Do NOT use = `NULL`
  - **Example Query:** `SELECT * FROM table WHERE column IS NULL`

## Null vs. Empty Values 

### Key Differences
  - **Null:** Truly unknown value
  - **Empty:** Known to be nothing
  - **Can be represented by:**
    - Two quotation marks ""
    - Zero 0
    - Intentionally blank entry

## Null Handling Functions
1. **ISNULL Function**
  - Checks if a column is null
  - Allows specifying a default value
  - **Examples:**
    - `ISNULL(address_line, '')` returns empty string if null
    - `ISNULL(discount, 0)` returns zero if null

2. **COALESCE Function**
  - Evaluates multiple columns in order
  - Returns first non-null value
  - **Use Case:** Contact Information Fallback
    - Email → Phone → Mobile Number

## Practical Null Handling Strategy

### Recommended Approach
  - Understand null as "unknown"
  - Use standard null comparison methods
  - Implement fallback strategies with COALESCE
  - Avoid unnecessary null entries

### Null Handling Diagram
<img src="https://github.com/TAPEZONE128/270125units/blob/main/DAT201x/images/diagram-export%20(6).png" length="300" width="300"/>

### Common Null Scenarios

| Scenario | Null Handling | Recommended Action |
|----------|---------------|--------------------|
| Missing Email | Use COALESCE | Provide alternative contact |
| Zero Discount | Use ISNULL | Default to standard rate |
| Incomplete Address | Mark specific fields null | Partial information acceptable |

### Key Takeaways
  - Null ≠ Empty
  - Always use `IS NULL` for comparisons
  - Leverage `COALESCE` for flexible data retrieval
  - Maintain data integrity through careful null management

---
## Transact-SQL Data Types

## Numeric Data Types: Exact vs. Floating Point 

### Exact Numeric Types
**Precision and Accuracy**
  - Provide absolute specific numeric representation
  - Maintain exact decimal place values
  - Ideal for financial calculations or scenarios requiring precise numbers

### Floating Point Numbers
**Characteristics**
  - Approximate representations (e.g., π ≈ 3.14)
  - Potential for slight inaccuracies beyond certain decimal places
  - Useful for scientific or approximate calculations

### Integer Variations 
**Storage Space Allocation**
  - Different integer types based on binary bit allocation
  - Ranges determined by number of bits assigned

### Integer Type Progression:
| Type | Bit Size | Range |
|------|----------|-------|
| Tiny Int | 8 bits | 0-255 |
| Small Int | 16 bits | -32,768 to 32,767 |
| Int | 32 bits | Larger range |
| Big Int | 64 bits | Extremely large range |

## Data Type Compatibility and Conversion 

### Conversion Types
1. **Implicit Conversion**
  - Automatic type conversion between compatible types
  - Works for similar data types (strings, numbers)
2. **Explicit Conversion**
  - Manual conversion using functions
  - **Key conversion functions:**
    - `CAST`
    - `CONVERT`
    - `PARSE`
    - `STR`

## Date Conversion Challenges 
- **Locale-Dependent Date Formats**
  - Potential misinterpretation of date order
  - Example: 05/06/2015 could mean:
    - May 6th, 2015 (US format)
    - June 5th, 2015 (European format)

### Safe Conversion Techniques
  - Use `TRY_CAST` for error-tolerant conversions
  - Explicitly specify conversion formats
  - Avoid relying on implicit date conversions

## Additional Data Types 
### Specialized Data Types
  - **Date and Time**
    - `DATETIME`
    - `DATETIME2`
    - Individual date/time storage options
      
  - **Binary Data Types**
    - Binary storage
    - Image storage
    - XML document storage

  - **Geospatial Types**
    - Geography
    - Geometry
    - Location-based data storage

## Key Conversion Considerations
  - Always specify explicit conversion when possible
  - Be aware of potential data loss
  - Understand locale and format differences
  - Use appropriate conversion functions for specific scenarios

### Mermaid Conversion Flow Diagram
<img src="https://raw.githubusercontent.com/TAPEZONE128/270125units/refs/heads/main/DAT201x/images/diagram-export%20(7).png" length="300" width="300"/>

---

## Handling Null Values in SQL: Advanced Techniques

### Understanding Null Value Conversion Strategies 
  - **TryCast Technique:** Convert problematic values to manageable formats
    - Converts non-numeric values to null
    - Allows transformation of inconsistent data types
    - Provides a way to handle mixed data in columns

### Null Conversion Methods
**Numeric Conversion**
  - Use `TryCast()` to convert values to integers
  - Null values automatically become zero
  - Prevents query interruption due to type mismatches

### Concatenation with Null Values 
  - **Null Concatenation Challenge:** Any expression with null results in null
  - **Solution Strategies:**
    - Convert null values to empty strings
    - Enables successful string concatenation
    - Preserves available data elements

## Null Handling Functions

### NULLIF Function 
  - **Purpose:** Replace specific values with null
  - **Example Use Case:**
    - Convert "multi-color" to null
    - Useful for data standardization
    - Allows filtering out unwanted categorical values

### COALESCE Function 
  - **Key Feature:** Finds first non-null value in a series of columns
  - **Practical Application:**
    - Useful for date tracking in product tables
    - Can combine multiple potential date columns
    - Ensures a value is always returned

## CASE Expressions for Null Handling 

### Search CASE Technique
 - **Flexible Logical Evaluation**
 - **Use Cases:**
   - Determine product sales status
   - Create derived columns based on null conditions
   - Implement complex conditional logic

### Case Statement Variants 
1. **Searched CASE**
  - Multiple conditional checks
  - Flexible logic implementation
2. **Simple CASE**
  - Direct column value comparison
  - Simpler syntax for straightforward transformations

### Database Design Considerations

**Null Frequency as Design Indicator**
  - Excessive nulls might suggest poor database design
  - Recommend reviewing data model
  - Aim for minimal null values

### Null Handling Best Practices
  - Always have a strategy for null values
  - Use appropriate conversion techniques
  - Consider database design implications

### Null Handling Decision Tree

<img src="https://raw.githubusercontent.com/TAPEZONE128/270125units/refs/heads/main/DAT201x/images/diagram-export%20(8).png" length="300" width="300"/>

### Key Takeaways
  - Null values are not errors but data states
  - Multiple techniques exist for managing nulls
  - Proper handling prevents query failures
  - Conversion methods depend on specific use case


---

# SQL Sorting and Result Filtering Techniques

## Sorting Results with `ORDER BY`

### Basic Sorting
- Default sorting is ascending (`ASC`)
- Can specify sorting direction:
  - `ASC`: Ascending order (0 to 100, A to Z)
  - `DESC`: Descending order (100 to 0, Z to A)

### Multi-Column Sorting
**Example syntax:**
```sql
SELECT Category, ProductName, Price
FROM Products
ORDER BY Category ASC, Price DESC;
```
- First sorts by `Category` ascending
- Then sorts by `Price` descending within each category

## Limiting Results with `TOP`

### Selecting Top N Results
- Use `TOP` to limit returned rows
- Can specify number or percentage

**Examples:**
```sql
SELECT TOP 10 * FROM Products;
SELECT TOP 5 PERCENT * FROM Products;
```

### Handling Ties
- `WITH TIES` includes additional rows with equal values
- Ensures all rows matching the top N criteria are returned

## Pagination Techniques

### Using `OFFSET` and `FETCH`
- Skip initial rows and retrieve next set

**Example:**
```sql
ORDER BY Price DESC
OFFSET 10 ROWS
FETCH NEXT 10 ROWS ONLY;
```

### Syntax Flexibility
- `ROW` and `ROWS` are interchangeable
- `FIRST` and `NEXT` mean the same thing

---

# Understanding `SELECT` and `DISTINCT` in SQL

## Basic SELECT Behavior
- A standard `SELECT` statement returns **all rows** in your result set.
  - Each row in your original table appears in the output.
  - **Duplicate values** are included by default.
  - The number of result rows matches the number of rows in the source table.

## Introducing `DISTINCT`: Eliminating Duplicates

### Single Column `DISTINCT`
- To see unique values in a column, use the `DISTINCT` keyword:
```sql
SELECT DISTINCT Color FROM Products;
```
- This query returns only unique color values, removing repetitions.

### Multiple Column `DISTINCT`
- `DISTINCT` can also be used with multiple columns:
```sql
SELECT DISTINCT Color, Size FROM Products;
```
- SQL returns unique **combinations** of color and size.

## Important Characteristics
- `DISTINCT` operates at the **row level**.
- It shows **unique row combinations**, not individual column uniqueness.
- Helps simplify result sets by removing redundant information.

## Practical Example

Consider a `Products` table with the following rows:
```
Blue, Medium
Blue, Large
Yellow, Small
Blue, Medium
```

- **Standard SELECT** (returns 4 rows):
```sql
SELECT Color FROM Products;
```

- **DISTINCT SELECT** (returns 2 rows: Blue, Yellow):
```sql
SELECT DISTINCT Color FROM Products;
```

## Best Practices
- Use `DISTINCT` when you need a summary of unique values.
- Be aware that `DISTINCT` can **impact query performance**.
- Consider your specific **data analysis needs** when choosing between standard and `DISTINCT` queries.

---



## **Module 3: Working with Multiple Tables (JOINs)**

### **Key Topics:**

* Concepts of Joins: Inner, Outer (Left, Right, Full)
* Join syntax: ANSI SQL-92 (`JOIN ... ON`) vs. old-style (`WHERE`)
* `Cartesian Product` and its accidental creation

### **Examples:**

```sql
-- Inner Join
SELECT p.Name AS ProductName, c.Name AS Category
FROM Product p
JOIN ProductCategory c ON p.CategoryID = c.CategoryID;

-- Left Outer Join
SELECT c.FirstName, s.SalesOrderNumber
FROM Customer c
LEFT JOIN SalesOrder s ON c.CustomerID = s.CustomerID;

-- Multiple Table Join
SELECT o.OrderDate, od.Quantity, p.Name
FROM SalesOrderHeader o
JOIN SalesOrderDetail od ON o.OrderID = od.OrderID
JOIN Product p ON od.ProductID = p.ProductID;
```

### **Notes:**

* Use aliases to clarify source tables.
* Use `LEFT JOIN` to keep all rows from the left table.
* `OUTER` keyword is optional: `LEFT JOIN` implies `LEFT OUTER JOIN`.

---

## **Module 4: Filtering Rows with Predicates**

### **Key Topics:**

* `WHERE` clause with operators: `=`, `<`, `>`, `<=`, `>=`, `<>`
* `BETWEEN`, `IN`, `LIKE`, `NOT`, `AND`, `OR`
* Null checks: `IS NULL`, `IS NOT NULL`

### **Examples:**

```sql
SELECT * FROM Products WHERE Color = 'Red';
SELECT * FROM Products WHERE Price BETWEEN 100 AND 200;
SELECT * FROM Products WHERE Size IN ('S', 'M', 'L');
SELECT * FROM Products WHERE ProductName LIKE 'A%';
SELECT * FROM Products WHERE ProductName LIKE '_B%';
SELECT * FROM Products WHERE EndDate IS NULL;
```

### **Notes:**

* `LIKE` supports `%` (any number of chars) and `_` (one char)
* Use parentheses `()` to group logical expressions for clarity.
* `IN` is more concise than multiple `OR` conditions.

---

## **Module 5: Aggregating Data**

### **Key Topics:**

* Aggregate functions: `SUM`, `AVG`, `COUNT`, `MIN`, `MAX`
* Grouping with `GROUP BY`
* Filtering grouped data using `HAVING`

### **Examples:**

```sql
SELECT CategoryID, COUNT(*) AS ProductCount
FROM Products
GROUP BY CategoryID;

SELECT CategoryID, AVG(Price) AS AvgPrice
FROM Products
GROUP BY CategoryID
HAVING AVG(Price) > 50;
```

### **Notes:**

* `GROUP BY` must include every selected non-aggregated column.
* `HAVING` filters aggregated results, whereas `WHERE` filters rows before grouping.

---

## **Module 6: Using Subqueries**

### **Key Topics:**

* Scalar subqueries, multi-row subqueries
* Subqueries in `SELECT`, `FROM`, `WHERE`, `HAVING`
* Correlated subqueries

### **Examples:**

```sql
-- Subquery in SELECT
SELECT Name, (SELECT AVG(Price) FROM Products) AS AvgPrice
FROM Products;

-- Subquery in WHERE
SELECT * FROM Products
WHERE CategoryID IN (SELECT CategoryID FROM Categories WHERE Name LIKE 'B%');

-- Correlated subquery
SELECT p.Name
FROM Products p
WHERE Price > (SELECT AVG(Price) FROM Products WHERE CategoryID = p.CategoryID);
```

### **Notes:**

* Correlated subqueries reference outer query columns.
* Can be performance-intensive; use carefully.

---

## **Module 7: Table Expressions**

### **Key Topics:**

* Derived tables
* Common Table Expressions (CTEs)
* Recursive CTEs

### **Examples:**

```sql
-- CTE
WITH ProductCTE AS (
  SELECT Name, Price FROM Products WHERE Price > 100
)
SELECT * FROM ProductCTE;

-- Recursive CTE
WITH Numbers AS (
  SELECT 1 AS Num
  UNION ALL
  SELECT Num + 1 FROM Numbers WHERE Num < 10
)
SELECT * FROM Numbers;
```

### **Notes:**

* CTEs improve readability and manage complexity.
* Recursive CTEs must include termination conditions.

---

## **Module 8: Set Operations**

### **Key Topics:**

* `UNION`, `UNION ALL`, `INTERSECT`, `EXCEPT`

### **Examples:**

```sql
-- UNION (removes duplicates)
SELECT Name FROM Products
UNION
SELECT Name FROM ArchivedProducts;

-- UNION ALL (keeps duplicates)
SELECT Name FROM Products
UNION ALL
SELECT Name FROM ArchivedProducts;

-- INTERSECT
SELECT Name FROM Products
INTERSECT
SELECT Name FROM ArchivedProducts;

-- EXCEPT
SELECT Name FROM Products
EXCEPT
SELECT Name FROM ArchivedProducts;
```

### **Notes:**

* All queries must have same number of columns and compatible types.
* Use `UNION ALL` for better performance when duplicates are acceptable.

---

## **Module 9: Data Modification**

### **Key Topics:**

* `INSERT`, `UPDATE`, `DELETE`
* Using subqueries in modification statements

### **Examples:**

```sql
-- INSERT
INSERT INTO Products (Name, Price) VALUES ('New Product', 99.99);

-- UPDATE
UPDATE Products SET Price = Price * 1.1 WHERE CategoryID = 3;

-- DELETE
DELETE FROM Products WHERE Discontinued = 1;
```

### **Notes:**

* Always ensure `WHERE` clause in `UPDATE`/`DELETE` to avoid full-table changes.
* `OUTPUT` clause can return affected rows.

---

## **Module 10: Transactions and Concurrency**

### **Key Topics:**

* ACID properties
* Transactions: `BEGIN`, `COMMIT`, `ROLLBACK`
* Isolation levels

### **Examples:**

```sql
BEGIN TRANSACTION;
UPDATE Accounts SET Balance = Balance - 100 WHERE AccountID = 1;
UPDATE Accounts SET Balance = Balance + 100 WHERE AccountID = 2;
COMMIT;
```

### **Notes:**

* Use `ROLLBACK` to undo changes in case of error.
* Isolation levels affect visibility and locking (e.g., `READ COMMITTED`, `SERIALIZABLE`).

---

## **Module 11: Error Handling and Programmability**

### **Key Topics:**

* `TRY...CATCH` blocks
* `THROW` and `RAISERROR`
* Stored procedures, functions, triggers

### **Examples:**

```sql
BEGIN TRY
  -- risky code
  UPDATE Products SET Price = -10;
END TRY
BEGIN CATCH
  PRINT ERROR_MESSAGE();
  ROLLBACK;
END CATCH;

-- Stored procedure
CREATE PROCEDURE GetExpensiveProducts
AS
BEGIN
  SELECT * FROM Products WHERE Price > 1000;
END;
```

### **Notes:**

* Use `TRY...CATCH` for robust error handling.
* Store logic in procedures/functions for reuse and abstraction.

---


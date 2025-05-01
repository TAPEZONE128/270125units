
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

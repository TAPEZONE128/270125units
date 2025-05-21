# Fundamentals of Database System

## Basic Database Operations
- **CRUD Operations:** Create, Read, Update, and Delete – fundamental actions for managing data in databases.
- **Unstructured Data:** Data without a predefined format (e.g., images, videos, social media posts).
- **Structured Data:** Organized data stored in a predefined format (e.g., tables in relational databases).

## Advantages of Using Databases in Business Operations
- Improved data organization and accessibility.
- Enhanced security and data integrity.
- Better decision-making with real-time data.
- Scalability and efficiency in handling large datasets.

## Terminologies
- **Big Data or NoSQL Systems:** Created to manage data for social media applications.
- **Database:** A collection of related data.
- **Data:** Facts that can be recorded.
- **DBMS:** Enables users to create a database system.

## Jobs
- **Database Administrator:** Authorizes access, coordinates, and monitors (accountable for security breaches).
- **Database Designer:** Identifies the data to be stored and chooses the appropriate structure.
- **End Users:** Access the database for querying, updating, and generating reports.
  1. **Casual End Users:** May need different information each time.
  2. **Naive/Parametric End Users:** Make up a sizable portion of database end users.
  3. **Sophisticated End Users:** Familiarize themselves with the facilities of the DBMS.
  4. **Standalone Users:** Maintain a personal database by using ready-made programs that provide an easy-to-use interface.
- **System Analysts:** Determine the requirements for end users.
- **Application Programmers:** Test, debug, document, and maintain (implement specifications as programs).
- **Software Engineer/Developer:** Familiar with the full range of capabilities provided by the DBMS to accomplish their tasks.

## Advantages of Using the DBMS Approach
- **Controlling Redundancy:** Improves performance in queries.
- **Restricting Unauthorized Access:** Provides a security and authorization subsystem.
- **Providing Persistent Storage for Program Details:** Ensures data survives the termination of program execution.
- **Providing Storage Structures and Search Techniques for Efficient Query Processing:** Responsible for choosing an efficient query execution plan.
- **Providing Backup and Recovery:** Supports recovery from hardware or software failures.
- **Providing Multiple User Interfaces:** Offers a variety of user interfaces (e.g., GUIs).
- **Representing Complex Relationships among Data:** Manages numerous varieties of interrelated data.
- **Enforcing Integrity Constraints:** Defines and enforces constraints (e.g., a record must be related to a course record).
- **Permitting Inferencing and Actions Using Rules and Triggers:**
  - **Deductive Databases:** Infer new information using rules.
  - **Triggers:** Automate actions based on table updates.
  - **Stored Procedures & Active Databases:** Enhance automation and enforcement of rules.

## Implications of the Database Approach
- **Enforcing Standards:** DBAs can enforce naming, format, and reporting standards.
- **Reduced Development Time:** New applications can be developed faster with a DBMS.
- **Flexibility:** Structural changes can be made without disrupting data and applications.
- **Up-to-Date Information:** Real-time updates are visible to all users.
- **Economies of Scale:** Consolidation reduces redundancy and costs.

## History of Database Applications
- **Early Databases (Hierarchical & Network Models):** Lacked flexibility and abstraction, requiring complex reorganization for new queries.
- **Relational Databases:** Introduced data abstraction, query languages, and improved flexibility.
- **Object-Oriented Databases (OODBs):** Enhanced modeling for complex applications but had limited adoption.
- **XML & E-Commerce:** Enabled structured data exchange on the web.
- **Specialized Databases:** Used in scientific research, multimedia, spatial data, and time-series applications.
- **Big Data & NoSQL:** Emerged to handle large-scale, non-relational data storage.

## When Not to Use a DBMS
- High initial costs and complexity.
- Simple, static applications.
- Real-time systems with strict performance needs.
- Embedded systems with limited storage.
- Industries like CAD, GIS, and telecommunications often use specialized solutions.

## Database Models, Normalization, Transactions, and Optimization

---

## Different Database Models

Database models define how data is structured, stored, and manipulated. The four main types of database models are:

### 1. Hierarchical Model
- Data is organized in a tree-like structure.
- Parent-child relationships where each parent can have multiple children, but each child has only one parent.
- Efficient for representing hierarchical data, such as an organizational chart.
- **Example**: XML data storage.

### 2. Network Model
- Similar to the hierarchical model, but a child can have multiple parents.
- Uses graph structures with records and relationships.
- More flexible than the hierarchical model but complex.
- **Example**: IDMS (Integrated Database Management System).

### 3. Relational Model
- Data is stored in tables (relations) consisting of rows (tuples) and columns (attributes).
- Uses SQL for data management.
- Most widely used model due to its simplicity and flexibility.
- **Example**: MySQL, PostgreSQL, Oracle, SQL Server.

### 4. Object-Oriented Model
- Stores data as objects (similar to object-oriented programming).
- Objects contain attributes (properties) and methods (functions).
- Supports complex data types, such as multimedia and geographic data.
- **Example**: ObjectDB, db4o.

---

## Entity-Relationship (ER) Diagram for a Library Management System

An ER diagram visually represents the relationships between entities in a database.

### Entities and Attributes:
- **Book**: (BookID, Title, Author, ISBN, Status)
- **Student**: (StudentID, Name, Email, ContactNumber)
- **Librarian**: (LibrarianID, Name, Email, ContactNumber)
- **Transaction**: (TransactionID, BookID, StudentID, IssueDate, DueDate, ReturnDate)

### Relationships:
- A student can borrow multiple books.
- A book can be borrowed by multiple students over time.
- A librarian manages the book lending process.

---

## Normalization

Normalization is the process of structuring a relational database to reduce redundancy and improve data integrity. It involves dividing a database into smaller tables while maintaining relationships.

### 1NF (First Normal Form)
- Eliminates duplicate columns.
- Ensures each column contains atomic (indivisible) values.
- **Example**:
  - Non-1NF: `Student(StudentID, Name, Subjects)` → (Subjects = "Math, Science")
  - 1NF: `Student(StudentID, Name)`, `Subjects(StudentID, Subject)`

### 2NF (Second Normal Form)
- Must be in 1NF.
- Ensures no partial dependency (every non-key attribute is fully dependent on the primary key).
- **Example**:
  - Non-2NF: `Order(OrderID, ProductID, ProductName, CustomerName)`
  - 2NF: `Order(OrderID, CustomerName)`, `OrderDetails(OrderID, ProductID, ProductName)`

### 3NF (Third Normal Form)
- Must be in 2NF.
- No transitive dependency (non-key attribute should not depend on another non-key attribute).
- **Example**:
  - Non-3NF: `Student(StudentID, Name, Department, DepartmentLocation)`
  - 3NF: `Student(StudentID, Name, DepartmentID)`, `Department(DepartmentID, DepartmentLocation)`

### BCNF (Boyce-Codd Normal Form)
- Must be in 3NF.
- Ensures every determinant is a candidate key.
- **Example**:
  - If a university assigns multiple instructors to a course but instructors can teach only one course at a time, BCNF ensures proper structuring.

---

## Transactions and Concurrency

### Transaction
A transaction is a sequence of one or more database operations that must be executed as a single unit.

#### ACID Properties:
- **Atomicity**: All operations must be completed or rolled back.
- **Consistency**: Database remains in a valid state.
- **Isolation**: Transactions do not interfere with each other.
- **Durability**: Changes persist even after system failure.

### Concurrency
Concurrency control ensures multiple transactions execute simultaneously without conflicts.

#### Issues in Concurrency:
- **Lost Updates**: Two transactions update the same data, causing one update to be lost.
- **Dirty Reads**: A transaction reads uncommitted data.
- **Non-Repeatable Reads**: A value changes between two reads in a single transaction.
- **Phantom Reads**: New rows appear in subsequent reads.

#### Concurrency Control Techniques:
- Locking (Shared & Exclusive locks)
- Timestamp-based ordering
- Optimistic concurrency control

---

## Indexing and Query Optimization

### Indexing

Indexing improves query performance by creating efficient data structures.

#### Common Types of Indexes:
1. **B-tree Index**
   - Uses a balanced tree data structure.
   - Supports efficient range queries and exact match lookups.
   - Widely used due to effectiveness with large datasets.
2. **Hash Index**
   - Uses a hash function to map values to a hash table.
   - Efficient for exact match lookups.
   - Not suitable for range queries.
3. **Bitmap Index**
   - Suitable for columns with a small number of distinct values.
   - Uses bitmap vectors for fast logical operations.
4. **Spatial Index**
   - Designed for spatial/geographic data queries.
   - Supports nearest neighbor and range searches.
5. **Clustered Index**
   - Sorts data rows in a table based on the index key.
   - Speeds up range queries significantly.

### Query Optimization

A query optimizer improves query efficiency by selecting the best execution plan.

#### Common Techniques:
1. **Cost-Based Optimization**
   - Uses statistics to estimate costs of query plans.
   - Chooses the plan with the lowest cost.
2. **Join Optimization**
   - Efficient join strategies:
     - Nested Loop Join (small datasets)
     - Hash Join (large indexed datasets)
     - Merge Join (sorted datasets)
3. **Predicate Pushdown**
   - Moves filters closer to the data source.
   - Reduces data processed during query execution.
4. **Parallel Execution**
   - Runs queries across multiple threads or processors.
   - Speeds up execution on large datasets.





# Software Engineering 1

## Software Engineering Overview  
- **Software** - Computer programs and documentation; can be **custom-built** or for the **general market**.  

### Good Software Attributes  
- **Maintainability**: Easy to modify and update.  
- **Dependability**: Reliable and secure.  
- **Usability**: User-friendly and intuitive.  
- **Efficiency**: Optimized for performance and resource usage.  

## Software Engineering  
Concerned with all aspects of software production.  

### Key Differences  
- **Software Engineering vs. Computer Science**:  
  - **Computer Science (CS)** focuses on **theory and algorithms**.  
  - **Software Engineering (SE)** focuses on **practical software development**.  
- **Software Engineering vs. System Engineering**:  
  - **Software Engineering** focuses on **software**.  
  - **System Engineering** includes **hardware, processes, and overall system integration**.  

## Core Software Engineering Activities  
1. **Specification** – Defining system requirements.  
2. **Development** – Designing and implementing software.  
3. **Validation** – Ensuring the software meets user needs.  
4. **Evolution** – Maintaining and updating the software.  

## Challenges & Costs  
- **Challenges**:  
  - Managing **diverse system requirements**.  
  - **Reducing delivery time** while maintaining quality.  
  - Ensuring **software reliability**.  
- **Costs**:  
  - **60% Development**, **40% Testing**.  
  - **Software evolution costs** often **exceed initial development** costs.  

## Software Engineering Techniques  
- Different methods apply to different systems:  
  - **Prototyping** for games and user-driven applications.  
  - **Strict specifications** for **safety-critical** systems (e.g., medical or aerospace software).  
- The **Web** has influenced:  
  - Programming languages.  
  - Software reuse.  
  - Distributed systems.  

## Types of Software Applications  
1. **Stand-alone** – Runs on a local computer (e.g., Office apps, CAD tools).  
2. **Interactive Transaction-Based** – Web-based and cloud systems.  
3. **Embedded Control** – Manages hardware devices (e.g., anti-lock brakes, mobile phones).  
4. **Batch Processing** – Processes data in bulk (e.g., billing systems).  
5. **Entertainment** – Games and multimedia applications.  
6. **Modeling & Simulation** – Used in scientific and engineering fields.  
7. **Data Collection** – Gathers sensor data for further processing.  
8. **Systems of Systems** – Integrated software components working together.  

## Software Engineering Ethics  
- **Confidentiality** – Respect client/employer data privacy.  
- **Competence** – Accept only work within expertise.  
- **Intellectual Property** – Protect patents, copyrights, and proprietary information.  
- **Computer Misuse** – Avoid unethical or illegal activities (e.g., hacking, malware).  

## Key Takeaways  
- **Software Engineering** involves all software development activities.  
- **Software isn’t just code**—it includes documentation, maintenance, and user support.  
- Different **software types require specialized development** approaches.  
- **Ethics and professional responsibility** are integral to software engineering.

---

## Software Development Life Cycle (SDLC)

**Software Development Life Cycle (SDLC)** - a structured approach to plan, design, develop, test, and maintain software systems  
- ensures development in a systematic, efficient, and predictable way, helping to manage complexity and improve the quality of the final product.

---

## Stages of SDLC

### 1. Planning:
**Definition:** Gathering initial requirements, identifying project goals, and developing a project plan. Helps outline the project scope, timeline, resources, budget, and potential risks.  
**Activities:** Resource allocation, risk analysis, project scheduling, and feasibility analysis.

### 2. Analysis:
**Definition:** System requirements are defined in greater detail. Includes gathering both functional and non-functional requirements from stakeholders.  
**Activities:** Requirement gathering, system modeling, and creating data flow diagrams or use cases.

### 3. Design:
**Definition:** Transforms the requirements into a blueprint for the system. Includes both high-level system architecture and detailed designs for each component.  
**Activities:** Creating system architecture diagrams, user interface designs, database designs, and software component specifications.

### 4. Implementation (Coding):
**Definition:** Actual coding of the software based on the design documents. Developers write the code using appropriate programming languages, libraries, and frameworks.  
**Activities:** Writing code, integrating system components, and unit testing.

### 5. Testing:
**Definition:** Ensures the software is bug-free and meets the specified requirements. Involves various types of testing such as unit testing, integration testing, system testing, and acceptance testing.  
**Activities:** Writing test cases, executing tests, fixing defects, and conducting performance evaluations.

### 6. Deployment:
**Definition:** Once the software passes testing, it is deployed to the production environment where it can be accessed by users.  
**Activities:** Installation, configuration, and deployment of the software. This may include deploying updates or patches as necessary.

### 7. Maintenance:
**Definition:** After the software is deployed, maintenance involves monitoring the system, fixing issues, and implementing updates and enhancements based on user feedback or new requirements.  
**Activities:** Bug fixes, software updates, performance monitoring, and system improvements.

---

## Different Models of SDLC

### 1. Waterfall Model:
**Description:** Linear and sequential approach where each phase must be completed before moving on to the next.  
**Strengths:** Simple to understand and implement. Well-suited for projects with clearly defined requirements.  
**Weaknesses:** Inflexible to changes; late-stage changes can be costly and difficult.

### 2. Agile Model:
**Description:** An iterative and incremental model where the software is developed in small, manageable chunks, called iterations or sprints. Each iteration results in a usable product increment.  
**Strengths:** Flexibility, adaptability to changes, frequent delivery of working software, and active collaboration with stakeholders.  
**Weaknesses:** Can lead to scope creep if not properly managed, and requires strong communication.

### 3. Spiral Model:
**Description:** Combines iterative development (like Agile) with systematic aspects of the Waterfall model. Focuses on risk management and involves planning, designing, developing, testing, and refining iteratively.  
**Strengths:** Emphasis on risk assessment and management, adaptable for large and complex projects.  
**Weaknesses:** Can be expensive and time-consuming due to multiple iterations and extensive documentation.

### 4. V-Model (Verification and Validation Model):
**Description:** An extension of the Waterfall model, where each development phase corresponds to a testing phase. Emphasizes validation and verification at each stage of development.  
**Strengths:** Clearly defined stages and testing phases, improving the quality of the software.  
**Weaknesses:** Inflexible for changes after requirements are defined and difficult to scale for larger projects.

---

## Software Requirements Engineering

**Software Requirements Engineering** - process of gathering, analyzing, specifying, and validating the requirements for a software system. Ensures that the software solution meets the needs of stakeholders and aligns with business goals.

## Key Steps in Requirements Engineering:
1. **Elicitation:** Gathering requirements from stakeholders (users, customers, domain experts).
2. **Analysis:** Defining clear, unambiguous, and consistent requirements.
3. **Specification:** Documenting the requirements in a formal, structured way.
4. **Validation:** Ensuring the requirements meet stakeholder needs and are feasible.

---

## Functional vs. Non-Functional Requirements

### 1. Functional Requirements:
**Definition:** Describing specific behaviors or functions the system must support. These requirements specify actions, inputs, outputs, and interactions.  
**Examples:** User authentication, data processing, payment processing, report generation.

### 2. Non-Functional Requirements:
**Definition:** How the system performs certain functions or characteristics it should have. These are quality attributes that describe system performance, security, scalability, and reliability.  
**Examples:** Performance (response time), security (encryption), availability (99% uptime), usability, and maintainability.

---

## Elicitation Techniques

### 1. Interviews:
**Definition:** One-on-one or group meetings with stakeholders to gather information about their needs, expectations, and pain points.  
**Strengths:** Provides direct feedback, allows for in-depth understanding of requirements.  
**Weaknesses:** Can be time-consuming and potentially biased based on interviewee's perspective.

### 2. Brainstorming:
**Definition:** Group discussions to generate creative ideas and identify requirements in a collaborative environment.  
**Strengths:** Promotes team engagement and idea sharing.  
**Weaknesses:** May result in unstructured or unrealistic ideas.

### 3. Prototyping:
**Definition:** Creating an early, simplified version of the system (prototype) to help stakeholders visualize and refine their requirements.  
**Strengths:** Helps clarify requirements, improves user involvement, and provides early feedback.  
**Weaknesses:** Can lead to misunderstandings if the prototype is not representative of the final product.

### 4. Surveys/Questionnaires:
**Definition:** Using structured forms to collect data from a large number of stakeholders or users.  
**Strengths:** Efficient for gathering information from many people.  
**Weaknesses:** Limited to the types of questions asked and can result in vague or ambiguous answers.

### 5. Observation:
**Definition:** Observing users in their natural environment to understand how they interact with systems or perform tasks.  
**Strengths:** Provides real-world insights and highlights unspoken or implicit requirements.  
**Weaknesses:** Time-consuming and may not be representative of all user contexts.

---

## Writing Software Requirements Specification (SRS)

**Software Requirements Specification (SRS)** - a document that formally captures all the functional and non-functional requirements of the software system. It provides a detailed description of the software’s intended functionality, interfaces, performance criteria, and constraints.

## Key Elements of an SRS:

1. **Introduction:** Provides an overview of the software system, its goals, and the intended audience for the document.  
2. **Overall Description:** Includes system perspective, user characteristics, constraints, and assumptions.  
3. **System Features:** A detailed description of each system feature, including functional requirements, user interactions, and system behavior.  
4. **External Interface Requirements:** Describes how the system will interact with external systems, hardware, and users.  
5. **Non-functional Requirements:** Covers performance, security, reliability, and other quality attributes.  
6. **Appendices:** Additional information such as acronyms, terminology, or glossary used in the SRS.

The SRS document serves as the foundation for system design, development, testing, and maintenance. It provides a clear, agreed-upon understanding between stakeholders, ensuring everyone has a shared vision for the system’s capabilities and limitations.



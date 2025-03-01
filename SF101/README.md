# System Fundamentals

## Computer System Fundamentals
### A computer system has three main components:
### a. Hardware
  - Physical parts of the computer.
  - Examples:
    - **Input Devices**: Keyboard, mouse, touchscreen.
    - **Output Devices**: Monitor, printer, speakers.
    - **Processing Unit**: Central Processing Unit (CPU) – the brain of the computer.
    - **Storage**: Hard drives, SSDs, USB flash drives.
### b. Software
  - Instructions that tell the computer what to do.
  - Types of software:
    - **System Software:** Operating systems like Windows, macOS, Linux.
    - **Application Software:** Programs like Word, Excel, Photoshop.
    - **Utility Software:** Tools like antivirus, disk cleanup, and file compression.
### c. Firmware
  - Low-level software embedded in hardware (e.g., BIOS or UEFI).
  - It helps initialize hardware and allows software to interact with it.

---

> An operating system (OS) is a software component that acts as an intermediary between computer hardware and software applications. It provides a platform for running applications and managing system resources efficiently.

- to *abstract hardware complexity and provide a user-friendly interface* for users to interact with the computer system.
- manages hardware resources: CPU, memory, storage, and I/O devices
- ensuring that *multiple applications can run concurrently* and share resources efficiently.

---
## Types of OS
- **Desktop Operating Systems**: Designed for personal computers and workstations, examples include Microsoft Windows, macOS (formerly OS X), and various Linux distributions (e.g., Ubuntu, Fedora).
- **Server Operating Systems**: Optimized for server environments, providing services such as web hosting, file sharing, and database management. Examples include Windows Server, Linux distributions (e.g., CentOS, Debian), and Unix variants (e.g., Solaris, FreeBSD).
- **Mobile Operating Systems**: Designed for smartphones, tablets, and other mobile devices, examples include Android (Google), iOS (Apple), and Windows Phone (Microsoft, discontinued).
- **Embedded Operating Systems**: Used in embedded systems and IoT (Internet of Things) devices, examples include embedded Linux distributions (e.g., OpenWrt), FreeRTOS, and Windows Embedded Compact.
- **Real-Time Operating Systems (RTOS)**: Designed for applications requiring deterministic response times like automotive and medical devices, examples include VxWorks, FreeRTOS, and QNX.

---
## Functions and Components
### 1. Process Management:
- involves creating, scheduling, and managing processes, which are instances of executing programs. The operating system allocates CPU time to processes, switches between processes to provide multitasking, and ensures proper synchronization and communication between processes.
### 2. Memory Management: 
- involves allocating, deallocating, and managing system memory resources to ensure efficient utilization and protection of memory.
### 3. File System Management:
- organizing and managing files and directories stored on disk storage devices. The operating system provides file system services such as file creation, deletion, reading, writing, and access control to facilitate data storage, retrieval, and manipulation.
### 4. Device Management: 
- involves controlling and coordinating access to input/output (I/O) devices such as keyboards, mice, displays, printers, and storage devices. The operating system interacts with device drivers to communicate with hardware devices, manages device resources, and provides services such as device configuration, data transfer, and error handling.

---

## **Computer System**  
A **computer system** is an integrated set of hardware and software designed to process data and execute tasks efficiently.

### **a. Central Processing Unit (CPU) architecture and functionality**  
- The **CPU** is the "brain" of the computer, executing instructions and processing data.  
- **Components**:
  - **ALU (Arithmetic Logic Unit)** – Performs mathematical and logical operations.  
  - **CU (Control Unit)** – Directs the operation of the processor.  
  - **Registers** – Small, high-speed storage for immediate data execution.  
- **Architecture Types**:
  - **Von Neumann Architecture** – Shared memory for both data and instructions.  
  - **Harvard Architecture** – Separate memory for data and instructions.  
  - **RISC vs. CISC** – RISC (Reduced Instruction Set Computing) is optimized for speed, while CISC (Complex Instruction Set Computing) has a broader set of instructions.

### **b. Memory Hierarchy**  
- **Registers** – Smallest, fastest storage within the CPU.  
- **Cache Memory** – Stores frequently accessed data to improve speed.  
- **RAM (Random Access Memory)** – Volatile memory used for active processes.  
- **ROM (Read-Only Memory)** – Stores firmware and essential boot instructions.  
- **Virtual Memory** – Uses part of the hard drive as RAM when physical memory is full.  

### **c. Storage Devices**  
- **HDD (Hard Disk Drive)** – Mechanical, large-capacity storage with slower speeds.  
- **SSD (Solid-State Drive)** – Faster, flash-based storage with no moving parts.  
- **Cloud Storage** – Remote storage accessed via the internet, scalable and flexible.  

### **d. Motherboard and Buses**  
- **Motherboard** – The main circuit board connecting all components.  
- **Buses**:
  - **System Bus** – Transfers data between the CPU, memory, and peripherals.  
  - **Address Bus** – Carries memory addresses from CPU to RAM.  
  - **Data Bus** – Transfers actual data between components.  

---

## **System Software and Utilities**  
System software manages hardware and provides a platform for applications.

### **a. System Software vs. Application Software**  
- **System Software** – Includes the operating system (OS) and utilities, managing hardware.  
- **Application Software** – User-focused programs like word processors and web browsers.  

### **b. Role of Compilers, Interpreters, and Assemblers**  
- **Compiler** – Translates high-level language into machine code before execution.  
- **Interpreter** – Translates and executes code line by line.  
- **Assembler** – Converts assembly language into machine code.  

### **c. Utility Programs**  
- **File Management** – Organizes and maintains files (e.g., Windows Explorer).  
- **Diagnostics** – Detects and resolves system issues.  
- **Antivirus** – Protects against malware and cyber threats.  

---

## **Networking Fundamentals**  
Networking allows computers to communicate and share resources.

### **a. Basic Networking Concepts**  
- **LAN (Local Area Network)** – A network within a limited area (e.g., office, home).  
- **WAN (Wide Area Network)** – A large network covering broad geographical areas.  
- **Internet** – A global network connecting billions of devices.  

### **b. Network Protocols**  
- **TCP/IP (Transmission Control Protocol/Internet Protocol)** – Governs data transmission.  
- **HTTP (Hypertext Transfer Protocol)** – Handles web browsing and data requests.  
- **FTP (File Transfer Protocol)** – Transfers files between computers.  

### **c. Network Topologies and Devices**  
- **Topologies** – Network layout structures (Star, Bus, Mesh, Ring).  
- **Devices**:
  - **Router** – Directs data between networks.  
  - **Switch** – Manages data traffic within a network.  
  - **Firewall** – Protects networks from unauthorized access.  

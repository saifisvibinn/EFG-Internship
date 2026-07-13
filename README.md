# BI & Data Engineering Assignments

This repository contains the deliverables for three Business Intelligence and Data Engineering assignments covering ETL development, SQL Server Data Warehouse design, SSIS, and Power BI dashboard development.

---

# Project Assignment 1
## Monthly Summary Dashboard with ETL & Star Schema

### Objective

Design and implement an interactive Monthly Summary Dashboard using a complete ETL pipeline, a SQL Server Data Warehouse, and a Star Schema model.

---

## Data Preparation & Modeling

The project includes:

- Build an ETL process to load CSV files
- Standardize date and time fields
- Remove duplicate records
- Join lookup tables to create a Star Schema
- Identify Fact and Dimension tables
- Create a `Dim_Date` table to support Time Intelligence
- Develop an interactive Power BI dashboard

---

## ETL & Star Schema Implementation

### Phase 1 – Requirements Gathering & Schema Design

#### 1. Analyze Reporting Needs
- Define KPIs and business metrics
- Identify reporting requirements ✅ Completed

#### 2. Identify Source Data
Review and analyze source CSV files:

- Sales
- Products
- Customers
- Additional lookup/reference files

#### 3. Design Star Schema
- Define Fact Tables
- Define Dimension Tables
- Create an Entity Relationship Diagram (ERD)
- Document relationships and keys

---

### Phase 2 – SQL Server Data Warehouse Setup

#### 4. Create Dimension Tables

Examples:

- Dim_Customer
- Dim_Product
- Dim_Date
- Dim_Region

#### 5. Create Fact Tables

Examples:

- Fact_Sales
- Fact_Transactions

#### 6. Establish Relationships

- Primary Keys
- Foreign Keys
- Referential Integrity

---

### Phase 3 – ETL Development Using SSIS

#### 7. Set Up SSIS Project

- Create an SSIS project using Visual Studio and SSDT
- Organize packages according to the ETL workflow

#### 8. Load Dimensions

- Create dedicated SSIS packages for Dimension tables
- Apply transformations and business rules

#### 9. Build Fact Load

- Perform Lookups
- Apply surrogate keys
- Load transactional data into Fact tables

#### 10. Create Master Package

- Orchestrate execution using Execute Package Tasks
- Ensure Dimension packages execute before Fact packages
- Add logging and error handling

---

# Project Assignment 2
## Sigma Capital Market Overview Analysis

### Objective

Analyze the Sigma Capital Market Overview page and identify all available data points that can be used for reporting and dashboarding.

---

## Data Sources

- Market Overview
- QSE Trading Reports

---

## Scope

### Investor Participation Breakdown

- Egyptian Investors %
- Arab Investors %
- Foreign Investors %
- Local Institutions %
- Retail vs Institutional Split

### Trading Activity by Investor Type

- Buy Value
- Sell Value
- Net Buy/Sell
- Trading Percentage

### Market Breadth Metrics

- Advancing Stocks
- Declining Stocks
- Unchanged Stocks
- Advance/Decline Ratio

### Sector Activity

- Sector Name
- Turnover Value
- Market Share %

### Block Trades

- Company Name
- Quantity
- Value
- Number of Trades

---

## Deliverables

Provide:

- Complete inventory of all available fields
- Source location/page section for each field
- Identify whether each field is:
  - Directly extractable
  - Requires calculation
- Dashboard recommendations
- KPI recommendations

---

# Project Assignment 3
## EFG One App Analysis & Dashboard Design

### Objective

Analyze the EFG One mobile application from a Business Intelligence perspective and design executive dashboards that help management understand customer behavior, digital adoption, trading activity, and overall business performance.

---

## Phase 1 – Application Assessment

Review and document:

- Main application modules
- User journey
- Customer experience flow
- Trading functionality
- Portfolio functionality
- Notification and engagement features
- Market and research features

---

## Phase 2 – Data Discovery

Identify all reportable data elements.

### Customer Information

- Customer ID
- Client Segment
- Country
- Risk Profile
- Registration Date

### Login & Usage Analytics

- Login Date/Time
- Session Duration
- Device Type
- Operating System
- Application Version
- User Activity Frequency

### Trading Analytics

- Orders
- Buy/Sell Activity
- Trading Volume
- Trading Value
- Market Activity

### Portfolio Analytics

- Portfolio Value
- Cash Balance
- Assets Under Management (AUM)
- Asset Allocation
- Daily Profit & Loss (P&L)

### Engagement Analytics

- Active Users
- Daily Active Users (DAU)
- Monthly Active Users (MAU)
- Most Visited Screens
- Feature Utilization

---

## Phase 3 – KPI Design

### Customer Analytics

- Total Customers
- Active Customers
- New Customers
- Retention Rate

### Digital Adoption

- DAU
- MAU
- Login Frequency
- Feature Adoption Rate
- App Engagement Score

### Trading Analytics

- Orders Count
- Trading Volume
- Trading Value
- Top Traded Securities

### Portfolio Analytics

- Assets Under Management (AUM)
- Average Portfolio Value
- Customer Growth

---

## Phase 4 – Dashboard Design

### Executive Dashboard

- Active Users
- Trading Value
- Assets Under Management (AUM)
- New Customer Acquisition
- Key Business KPIs

### Customer Analytics Dashboard

- Customer Segmentation
- Retention Analysis
- Geographic Distribution

### Trading Dashboard

- Trading Trends
- Buy vs Sell Analysis
- Market Activity

### Portfolio Dashboard

- AUM Trends
- Asset Allocation
- Portfolio Distribution

---

# Required Software

Install the following before starting:

- Microsoft SQL Server Management Studio (SSMS)
- Microsoft SQL Server
- Power BI Desktop
- Visual Studio 2022
- SQL Server Integration Services (SSIS Extension)

---

# Technologies

- SQL Server
- SSMS
- SSIS
- Visual Studio 2022
- Power BI
- CSV Data Sources
- Star Schema
- ETL Pipeline
- Data Warehouse
```

# BigQuery AI Agent | Google Cloud

![Google Cloud](https://img.shields.io/badge/Google_Cloud-Agent_Runtime-4285F4?logo=googlecloud&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![BigQuery](https://img.shields.io/badge/BigQuery-Integrated-669DF6?logo=googlebigquery&logoColor=white)
![Challenge](https://img.shields.io/badge/GENAI160-100%2F100-success)

## Overview

A hands-on Google Cloud AI engineering project completed as part of the **Govern Agent Access with Gemini Platform (GENAI160)** challenge lab.

The project demonstrates how to deploy an AI agent using Google's Agent Development Kit (ADK), connect it to BigQuery, and securely manage access through Agent Identity and IAM.

**Challenge Lab Result: 100/100**

## Project Objectives

- Deploy a BigQuery-enabled AI agent to Google Cloud Agent Runtime.
- Configure dedicated Agent Identity authentication.
- Implement secure BigQuery access using IAM.
- Enable natural-language interaction with invoice data.
- Validate the deployed agent through Agent Runtime Playground.

## Technology Stack

| Technology | Purpose |
|------------|---------|
| Google Cloud | Cloud infrastructure |
| Google ADK | AI agent development |
| Agent Runtime | Agent deployment |
| Vertex AI | Generative AI integration |
| Gemini | Language model |
| BigQuery | Invoice data storage and querying |
| Agent Identity | Dedicated agent authentication |
| Cloud IAM | Access control |
| Python 3.12 | Deployment runtime |

## Architecture

The solution follows this workflow:

1. A user submits a natural-language request through Agent Runtime Playground.
2. The deployed ADK agent interprets the request using Gemini.
3. The agent uses its BigQuery toolset to generate and execute SQL queries.
4. BigQuery authorizes access through the agent's dedicated identity.
5. The agent returns the query results in natural language.

### Security Configuration

The deployed agent was assigned a dedicated Agent Identity rather than relying on a shared service account.

The following IAM roles were granted directly to the agent:

- `roles/bigquery.user`
- `roles/bigquery.dataEditor`

This demonstrates identity-based access control for AI agents interacting with cloud data.

## Implementation

### 1. Environment Setup

Configured Google Cloud Shell and installed the required Python dependencies for Google ADK and Agent Runtime.

### 2. Agent Deployment

Configured and deployed the BigQuery-enabled agent using Python and Google Cloud Agent Runtime.

**Deployment result:** Successful

### 3. Agent Identity Configuration

Assigned the deployed agent a dedicated identity and configured the required BigQuery IAM permissions.

### 4. Agent Validation

Tested the agent through Agent Runtime Playground using natural-language queries against invoice data.

## Validation Results

| Test | Result |
|------|--------|
| Agent deployment | Passed |
| Agent Identity configuration | Passed |
| BigQuery IAM permissions | Passed |
| Natural-language SQL querying | Passed |
| April 2026 invoice total | $7,672.85 |
| Unpaid invoice count | 6 |
| Total unpaid balance | $15,889.00 |
| Invoice schema retrieval | Passed |

### Example Prompts

**Invoice analysis**
> What was the total sum of the invoice totals that arrived in April 2026? What invoices are not paid?

**Outstanding invoices**
> What is the total number of unpaid invoices we currently have?

**Schema inspection**
> What is the schema of the invoice table?

All three prompts returned the expected results.

## Challenge Lab Achievement

**Google Cloud Skills Boost**

- **Lab:** Govern Agent Access with Gemini Platform
- **Lab ID:** GENAI160
- **Final Score:** 100/100
- **Status:** Successfully Completed

## Key Learnings

Through this project, I gained practical experience in:

- Deploying AI agents using Google ADK.
- Integrating generative AI with BigQuery.
- Configuring Agent Identity and IAM permissions.
- Using natural language to analyze structured data.
- Validating AI agent functionality in a managed cloud environment.

## Project Status

**Challenge Lab Completed Successfully**

This repository documents a completed hands-on Google Cloud challenge lab. The agent was deployed and validated in a temporary lab environment.

The original cloud resources are not maintained as a live deployment.

## Author

**Wendell D. Velarde**

Cloud Computing | AI Engineering | Generative AI | Automation

---

*Built as part of a hands-on Google Cloud learning experience.*

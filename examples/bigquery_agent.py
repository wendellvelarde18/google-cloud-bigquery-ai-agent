"""
BigQuery AI Agent - Portfolio Example
Author: Wendell D. Velarde

Inspired by Google Cloud GENAI160:
Govern Agent Access with Gemini Platform.

This is an original educational example, not the
original challenge lab source code.

Requires Google ADK and Google Cloud authentication.
"""

import os

from google.adk.agents import Agent
from google.cloud import bigquery


PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
MODEL = os.environ.get("MODEL", "gemini-2.5-flash")


def query_invoices(sql_query: str) -> dict:
    """Execute a read-only SQL query against BigQuery."""

    if not PROJECT_ID:
        return {"error": "GOOGLE_CLOUD_PROJECT is not configured."}

    sql = sql_query.strip()

    if not sql.upper().startswith("SELECT"):
        return {"error": "Only SELECT queries are permitted."}

    try:
        client = bigquery.Client(project=PROJECT_ID)

        job_config = bigquery.QueryJobConfig(
            dry_run=False,
            use_query_cache=True,
            maximum_bytes_billed=100_000_000,
        )

        result = client.query(
            sql,
            job_config=job_config,
        ).result()

        rows = [dict(row.items()) for row in result]

        return {
            "status": "success",
            "row_count": len(rows),
            "data": rows[:100],
        }

    except Exception as error:
        return {"error": str(error)}


root_agent = Agent(
    name="bigquery_invoice_agent",
    model=MODEL,
    description=(
        "AI agent that analyzes invoice data "
        "stored in Google BigQuery."
    ),
    instruction=(
        "You are a finance data analysis assistant. "
        "Help users understand invoice records using BigQuery. "
        "Generate read-only SQL queries. "
        "Never modify or delete invoice data. "
        "Use the query_invoices tool to retrieve results. "
        "Only report information returned by the tool."
    ),
    tools=[query_invoices],
)

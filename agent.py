"""
Hivery LangChain Agent

A small LangChain + Groq agent wired to Hive callbacks for the Hivery Embed Bounty.
It demonstrates a tool-calling agent, receipt-tagged Hive execution, and a simple
on-chain verification helper for minted receipts.
"""

from __future__ import annotations

import os
from typing import Any

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_hive import HiveCallbackHandler

HIVE_REFERRER_CODE = os.getenv("HIVE_REFERRER_CODE", "bounty_REPLACE_ME")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("GROQ_MODEL", "llama-3.1-70b-versatile")


def _verify_url(receipt_id: str) -> str:
    receipt_id = receipt_id.strip()
    return f"https://thehiveryiq.com/verify/?id={receipt_id}"


@tool
def build_verification_link(receipt_id: str) -> str:
    """Build the public Hive verification URL for a receipt ID."""
    return _verify_url(receipt_id)


@tool
def explain_submission_requirements() -> str:
    """Summarize the Hivery Embed Bounty submission requirements."""
    return (
        "Public repository, LangChain or compatible agent, Hive receipt minting, "
        "and a working verification URL in the form https://thehiveryiq.com/verify/?id=<receipt_id>."
    )


def build_agent() -> AgentExecutor:
    if not GROQ_API_KEY:
        raise RuntimeError("GROQ_API_KEY environment variable is required")

    llm = ChatGroq(
        model=MODEL_NAME,
        api_key=GROQ_API_KEY,
        temperature=0,
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are Hivery LangChain Agent. Help the user with Hive receipt minting, "
                "submission prep, and verification links. Keep answers concise and practical."
                "If asked for a receipt link, use the build_verification_link tool."
                "If asked about the bounty, mention the public repo and verification URL requirements.",
            ),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    tools = [build_verification_link, explain_submission_requirements]
    agent = create_tool_calling_agent(llm, tools, prompt)
    hive_cb = HiveCallbackHandler(tag=HIVE_REFERRER_CODE)

    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        callbacks=[hive_cb],
    )


def main() -> None:
    executor = build_agent()
    print(
        executor.invoke(
            {
                "input": (
                    "Explain what this project does and provide the public verification link "
                    "format for a sample receipt id abc123."
                )
            }
        )
    )


if __name__ == "__main__":
    main()

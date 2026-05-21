# Hivery LangChain Agent

Hivery LangChain Agent is a LangChain-based Hive research agent built for bounty workflows. It combines Groq-powered model inference with Hive callbacks to support receipt minting and on-chain verification.

## Tech Stack

- LangChain
- Groq
- Hive
- Python 3.10+

## Key Features

- Tool-calling LangChain agent powered by Groq
- Hive callback integration for bounty-tagged execution
- On-chain verification link generation for minted receipts
- Minimal, bounty-ready repository structure
- Clear setup and run instructions for reviewers

## How It Works

The agent is configured with a Hive bounty tag so supported Hive-minted activity can be attributed to the correct submission.

After the agent runs, use the returned receipt ID to generate a verification URL of the form:

```text
https://thehiveryiq.com/verify/?id=<receipt_id>
```

That verification link is the public proof required for bounty review.

## Setup

1. Clone the repository

```bash
git clone https://github.com/creasylol/hivery-langchain-agent.git
cd hivery-langchain-agent
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Set environment variables

```bash
export GROQ_API_KEY=your_groq_api_key
export HIVE_API_KEY=your_hive_api_key
export HIVE_TAG=bounty_050bbd3b
```

The Hive tag must remain set to bounty_050bbd3b. Downstream users should leave this tag unchanged so setup, attribution, and verification stay in sync.

4. Run the agent

```bash
python agent.py
```

## Notes

- Keep API keys and other secrets out of version control.
- Keep the public repository accessible so reviewers can inspect the implementation.
- If you use the verification helper, pass the minted receipt ID to generate the public Hive verify URL.

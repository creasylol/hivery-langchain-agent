# Hivery LangChain Agent

A LangChain-based Hive agent built for the Hivery Embed Bounty. This project uses Groq for fast model inference and Hive callbacks for receipt minting and verification workflows.

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

The agent is configured with a Hive referrer tag so any supported Hive-minted activity can be attributed to the submission.

After the agent runs, use the returned receipt ID to generate a verification URL of the form:

https://thehiveryiq.com/verify/?id=<receipt_id>

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
export HIVE_REFERRER_CODE=bounty_your_code
export GROQ_MODEL=llama-3.1-70b-versatile
```

4. Run the agent

```bash
python agent.py
```

## Notes

- Replace `bounty_REPLACE_ME` with the referrer code returned from the Hivery bounty registration flow.
- Keep the public repository accessible so reviewers can inspect the implementation.
- If you use the verification helper, pass the minted receipt ID to generate the public Hive verify URL.

## Submission Checklist

- Public GitHub repository
- Working LangChain + Groq agent
- Hive callback integration enabled
- Verification URL included in the submission

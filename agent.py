from openai import OpenAI
from dotenv import load_dotenv
import os

from rag import search_knowledge_base
from tools import check_internet, check_dns, get_system_info


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def helpdesk_agent(user_query):
    """
    AI IT Helpdesk Agent.
    Uses RAG + troubleshooting tools.
    """

    # 1. Search the knowledge base
    knowledge = search_knowledge_base(user_query)

    knowledge_text = "\n\n".join(knowledge)

    # 2. Run diagnostic tools
    internet_result = check_internet()
    dns_result = check_dns()
    system_result = get_system_info()

    # 3. Create context for the AI
    prompt = f"""
You are an AI IT Helpdesk Agent.

Your job is to diagnose common technical problems
and recommend safe troubleshooting steps.

USER PROBLEM:
{user_query}

RELEVANT KNOWLEDGE BASE INFORMATION:
{knowledge_text}

DIAGNOSTIC RESULTS:

Internet:
{internet_result}

DNS:
{dns_result}

System Information:
{system_result}

Based on the user's problem, knowledge base and diagnostic
results:

1. Identify the likely problem.
2. Explain the reason in simple language.
3. Give step-by-step troubleshooting instructions.
4. If the problem cannot be confirmed, clearly say that.
5. Do not invent diagnostic results.

Keep the answer clear and practical.
"""

    # 4. Ask AI to analyze everything
    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text


# Test the Agent
if __name__ == "__main__":

    question = "My computer is connected to Wi-Fi but websites are not opening."

    print("\n===== AI IT HELPDESK AGENT =====\n")

    answer = helpdesk_agent(question)

    print(answer)
from gradio_client import Client

SPACE_NAME = "Qwen/Qwen3-Demo"


def generate_response(prompt, temperature=0.3, max_tokens=500):

    # Connect to the free Qwen Space
    client = Client(SPACE_NAME)

    # Qwen model settings
    settings = {
        "model": "qwen3-235b-a22b",
        "sys_prompt": (
            "You are an educational AI assistant. "
            "Explain concepts accurately, clearly, "
            "and in a student-friendly manner."
        ),
        "thinking_budget": 38
    }

    # Send the prompt
    result = client.predict(
        prompt,
        settings,
        api_name="/add_message"
    )

    # Second returned value contains chatbot information
    chatbot_data = result[1]

    # -----------------------------------------
    # Extract chatbot conversation
    # -----------------------------------------
    if isinstance(chatbot_data, dict):

        messages = chatbot_data.get("value", [])

        if isinstance(messages, list):

            # Search from the latest message
            for message in reversed(messages):

                if not isinstance(message, dict):
                    continue

                # We only want the assistant's response
                if message.get("role") != "assistant":
                    continue

                content = message.get("content", [])

                # Assistant content is a list
                if isinstance(content, list):

                    # Search for final text
                    for part in reversed(content):

                        if isinstance(part, dict):

                            if part.get("type") == "text":

                                answer = part.get("content", "")

                                if answer:
                                    return answer.strip()

    return "No final answer was generated."
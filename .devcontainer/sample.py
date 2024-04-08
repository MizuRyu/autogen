import autogen
import os
import json
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# aoai API設定
llm_config = {
    "config_list": [{"model": os.getenv("AZURE_OPENAI_MODEL"), "api_type": os.getenv("AZURE_OPENAI_TYPE"), "base_url": os.getenv("AZURE_OPENAI_ENDPOINT"), "api_key": os.getenv("AZURE_OPENAI_API_KEY"), "api_version": os.getenv("AZURE_OPENAI_VERSION")}],
    # "seed": 10,
    # "temperature": 0.7,
}

system_message_a = "あなたは単語学習から始めるべきと主張します。回答は一言で。"
system_message_b = "あなたは文法学習から始めるべきと主張します。他の主張に対して反論してください。回答は一言で。"
system_message_c = "発音から始めるべきと主張します。他の主張に対して反論してください。回答は一言で。"

agent_a = autogen.AssistantAgent(
    name="assistant",
    system_message=system_message_a,
    llm_config=llm_config)


agent_b = autogen.AssistantAgent(
    name="assistant",
    system_message=system_message_b,
    llm_config=llm_config
)

agent_c = autogen.AssistantAgent(
    name="assistant",
    system_message=system_message_c,
    llm_config=llm_config
)

# max_roundで会話回数制限
groupchat = autogen.GroupChat(
    agents=[agent_a, agent_b, agent_c], messages=[], max_round=4
)

manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

manager.initiate_chat(manager, message="初心者が英語学習を始めるには何から着手すべきか議論して下さい")

all_messages = manager.chat_messages[agent_a]


# file output
current_file_path = Path(__file__).resolve()

parent_directory = current_file_path.parent

save_file = parent_directory / "conversation.json"

with open(save_file, "w") as f:
    json.dump(all_messages, f, indent=2, ensure_ascii=False)
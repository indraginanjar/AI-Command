from argparse import ArgumentParser, Namespace
from openai.types.chat.chat_completion import ChatCompletion, Choice
from subprocess import CompletedProcess
import argparse
import openai
import os
import subprocess

client = openai.Client(
    api_key=os.environ.get("AI_COMMAND_OPENAI_API_KEY"),
)

parser: ArgumentParser = argparse.ArgumentParser("aicommand")

parser.add_argument(
    "prompt", help="Prompt describing task/command to produce and execute.", type=str
)

shell: str = "powershell"

if os.name != "nt":
    shell = "pwsh"

customShell: str = os.environ.get("AI_COMMAND_SHELL")

if customShell is not None:
    shell = customShell

args: Namespace = parser.parse_args()
print("Prompt:\n" + args.prompt.strip())

prompt: str = "Create a " + shell + " script. Answer without giving explanation, just pure script. Do not mark the produced script as a code."
prompt += '"""' + args.prompt.strip() + '"""'
temperature: float = 0.7
max_tokens: int = 60

chat_completion: ChatCompletion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
)

choice: Choice = chat_completion.choices[0]
generated_text = choice.message.content.strip()
print("Generated command:\n" + generated_text)

user_input: str = input("Do you want to execute the generated command? (y)es/(n)o: ")
lowered_user_input: str = user_input.lower()

user_choose_to_execute: bool = lowered_user_input == "yes" or lowered_user_input == "y"

if user_choose_to_execute:
    print("Executing generated command ...")

    if shell == 'powershell' or shell == 'pwsh':
        result: CompletedProcess[bytes] = subprocess.run(
            [shell, "-Command", generated_text], stdout=subprocess.PIPE
        )
    else:
        result: CompletedProcess[bytes] = subprocess.run(
            [shell, "/c", generated_text], stdout=subprocess.PIPE
        )
    print(result.stdout.decode("utf-8"))
else:
    print("You choose not to execute the generated command.")

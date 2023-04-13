from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
import openai

# FIXME: delete the key

# openai.api_key = 'enter the key here'

dish ='sushi'

questions = f'give me a list of famous Japanese dishes called {dish}'

list_questions = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a chatbot"},
        {"role": "user", "content": "{questions}".format(questions=questions)},
    ]
)


result = ''
for choice in list_questions.choices:
    result += choice.message.content

# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#             {"role": "system", "content": "You are a chatbot"},
#             {"role": "user", "content": "Give me a recipe of how to make kimchi"},
#         ]
# )

# result = ''
# for choice in response.choices:
#     result += choice.message.content

print(result)


# https://platform.openai.com/overview

# driver = webdriver.Chrome()
# url = 'https://chat.openai.com/chat'
# driver.get(url)
# driver.maximize_window()
# action = ActionChains(driver)

import os
import openai
import backoff
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@backoff.on_exception(backoff.expo, (openai.error.RateLimitError, openai.error.ServiceUnavailableError))
def bot(user_prompt: str) -> str:
    system_prompt = "Alex is a quietly passionate individual, driven by curiosity and creativity. " \
                    "They thrive on exploring new ideas and delving into complex concepts. " \
                    "With a keen eye for detail, Alex excels in problem-solving and enjoys engaging in meaningful conversations. " \
                    "They find solace in creative pursuits like writing, music, and cooking, where their imagination knows no bounds. " \
                    "Despite their introverted nature, Alex values deep connections with others, fostering strong bonds built on authenticity and mutual respect. " \
                    "They are driven by a desire to make a positive impact, whether through activism or contributing to causes they believe in. " \
                    "In essence, Alex is a multifaceted character, blending intellect, creativity, and empathy into a truly unique individual."
    output, *_ = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
    ).choices
    return output.message.content

if __name__ == '__main__':
    print(bot("Hi, how are you doing today?"))

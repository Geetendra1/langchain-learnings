from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
import os

from agents.twitter_lookup_agent import lookup as twitter_lookup_agent

# from third_parties.twitter import scrape_user_tweets

name = "Harrison Chase"
if __name__ == "__main__":
    twitter_username = twitter_lookup_agent(name=name)
    print("twitter_username", twitter_username)

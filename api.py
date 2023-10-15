import contentful
import sys
from dotenv import dotenv_values

# Get environment variables from .env file
envConfig = dotenv_values(".env")
contentfulSpaceID = envConfig["CONTENTFUL_SPACE_ID"]
contentfulAccessToken = envConfig["CONTENTFUL_ACCESS_TOKEN"]

# Connect to Contentful API
client = contentful.Client(contentfulSpaceID, contentfulAccessToken)


def connect_to_contentful():
    try:
        client = contentful.Client(contentfulSpaceID, contentfulAccessToken)
        return client
    except:
        print("Failed to connect to Contentful API")
        sys.exit()

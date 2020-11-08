import json
from botocore.vendored import requests

original_api = "https://pixabay.com/api/?key="
pixabay_api_key = "xxxxxxxxxxxxxxxxxx"

def lambda_handler(event, context):
    # TODO implement
    print (event["keywords"])
    keywords = event["keywords"]
    if len(keywords) <3:
        no_to_retrieve = 6
    else:
        no_to_retrieve = 4
    final_output = {}
    final_output["urls"]=[]
    for keyword in keywords:
        keyword = keyword.replace(" ",'+')
        pixabay_api = original_api+pixabay_api_key+"&q="+keyword+"&image_type=photo&safesearch=true&per_page="+str(no_to_retrieve)
        response = requests.get(pixabay_api)
        info =[]
        if response:
            output = response.json()
            for each in output["hits"]:
                temp = {}
                temp["small"] = each["previewURL"]
                temp["medium"] = each["webformatURL"].replace("_640","_340") #180
                temp["large"] = each["largeImageURL"]
                final_output["urls"].append(temp)
                
    return final_output


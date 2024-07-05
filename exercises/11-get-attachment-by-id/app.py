import requests
import numpy as np
import pandas as pd

def get_attachment_by_id(attachment_id):
    # Your code here
    # lo mismo de siempre: 
    url = 'https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php'
    response = requests.get(url)
    if response.status_code == 200:    
        data = response.json()
        posts = data['posts']
        for post in posts:
            for att in post['attachments']:
                if att['id'] == attachment_id:
                    print("This is the URL of the attachment: ")
                    return att['url']
            
    
                else: 
                    return f"Error - no attachments found for the given id."
    else:
        return f"Something went wrong. Error code: {response.status_code}"
    

print(get_attachment_by_id(104))
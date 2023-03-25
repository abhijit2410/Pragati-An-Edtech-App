import shutil
import requests

"""
# OPEN BROWSER AND GET IMAGE LINK TO BE DOWNLOADED
"""

# imagePath = "https://edumilestones.com/blog/images/What-after-12th.png"

def img_download(imagePath):

    response = requests.get(imagePath, stream = True)
    path = "app/images/" + imagePath.split("/")[-1]
    with open(path, 'wb') as f:
        print("Image Saved")
        shutil.copyfileobj(response.raw, f)
        return path
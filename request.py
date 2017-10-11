import requests
import json
import numpy as np
from PIL import Image
import random
from apikey import getApiKey

def createRandomPicture(width, height):
    picture = np.zeros((height, width, 3), dtype=np.uint8)
    randomSeed = getRandomInt(1, 0, 2**128)
    if randomSeed is None:
        return
    random.seed(randomSeed[0])
    for i in range(width):
        for j in range(height):
            picture[i, j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    img = Image.fromarray(picture, "RGB")
    img.save("pic.png")

def getRandomInt(n, minInput, maxInput):
    apiKey = getApiKey()
    params = {"jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": apiKey,
            "n": n,
            "min": minInput,
            "max": maxInput
        },
        "id": 2015}
    headers = {"content-type": 'application/json'}
    r = requests.post("https://api.random.org/json-rpc/1/invoke", data=json.dumps(params), headers=headers).json()
    try:
        return r['result']['random']['data']
    except KeyError:
        return None

createRandomPicture(128,128)

# -*- coding: utf-8 -*-
"""OpenAI Generate Image from Text Prompt.ipynb

Original file is located at
    https://colab.research.google.com/drive/1tXUS4BYIqarugFDi5MWBqXR2QPhxTNb9
"""

!pip install openai

"""##### Environment variable for the hidden openAI API Key"""

# Commented out IPython magic to ensure Python compatibility.
# %env OPENAI_API_KEY=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

"""##### import the relevant libraries"""

import urllib.request
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

import openai
import os
import matplotlib.pyplot as plt
import numpy as np
import urllib.request
from PIL import Image


openai.api_key = os.getenv("OPENAI_API_KEY")
def generate_image(input_string): 
  response = openai.Image.create(
    prompt=input_string,
    n=1,
    size="512x512"
  )
  image_url = response['data'][0]['url']
  return image_url

input_string = "a bird in the branch of the tree"
output = generate_image(input_string)
print(f"Input: {input_string}\nOutput: {output}")

urllib.request.urlretrieve(output, 'output.png')
img = Image.open('output.png')
img_array = np.array(img)

plt.figure(figsize=(9,9))
ax = plt.axes(xticks=[], yticks=[])
ax.imshow(img_array)

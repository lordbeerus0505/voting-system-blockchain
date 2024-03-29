import requests
'''import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import patches'''
from io import BytesIO
import os

# If you are using a Jupyter notebook, uncomment the following line.
#%matplotlib inline

class Face_Detector:
    def detect(self,path):
        # Replace <Subscription Key`> with your valid subscription key.
        subscription_key = "250e2655ae5b4c2fbf5a649e0cae99aa" #DSFace API

        # Set image path from local file.
        image_path = path#os.path.join('D:\\codefundo\\Webapp\\visaSample1.jpg')

        assert subscription_key

        # You must use the same region in your REST call as you used to get your
        # subscription keys. For example, if you got your subscription keys from
        # westus, replace "westcentralus" in the URI below with "westus".
        #
        # Free trial subscription keys are generated in the westcentralus region.
        # If you use a free trial subscription key, you shouldn't need to change
        # this region.
        face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

        image_data = open(image_path, "rb")

        headers = {'Content-Type': 'application/octet-stream',
                'Ocp-Apim-Subscription-Key': subscription_key}
        params = {
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,' +
            'emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
        }

        response = requests.post(face_api_url, params=params, headers=headers, data=image_data)
        response.raise_for_status()
        faces = response.json() 
        if len(faces)==1:
            return True
        return False
# Display the original image and overlay it with the face information.
# image_read = open(image_path, "rb").read()
# image = Image.open(BytesIO(image_read))

# plt.figure(figsize=(8, 8))
# ax = plt.imshow(image, alpha=1)
# for face in faces:
#     fr = face["faceRectangle"]
#     fa = face["faceAttributes"]
#     origin = (fr["left"], fr["top"])
#     p = patches.Rectangle(
#         origin, fr["width"], fr["height"], fill=False, linewidth=2, color='b')
#     ax.axes.add_patch(p)
#     plt.text(origin[0], origin[1], "%s, %d"%(fa["gender"].capitalize(), fa["age"]),
#              fontsize=20, weight="bold", va="bottom")
# _ = plt.axis("off")
# plt.show()

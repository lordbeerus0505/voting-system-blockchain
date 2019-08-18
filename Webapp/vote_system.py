import pymongo
import re
import os
import base64
import pdb
import json
from visa_verif import OCR
from emotion_detect import Emotion_Detector
#from detect import Detector
from face_detect import Face_Detector
fd = open("config.txt")
data = json.load(fd)
class Voting:
    uid,fname,lname,age,address,photo,criminal_records=('',)*7
    def __init__(self):
        self.uid="XXXX"
        self.fname="default"
        self.lname="default"
        self.age=21
        self.address="default"
        self.gender="XXXX"
        self.ward=10000
        self.photo="pic.jpg"
        
    #perform validation on the front end itself and carry on.
    def register_candidate(self,uid,fname,lname,age,address,gender,ward,photo,criminal_records): #additional details are needed for this operation.
        self.uid,self.fname,self.lname,self.age,self.address,self.photo,self.criminal_records,self.gender,self.ward=uid,fname,lname,age,address,photo,criminal_records,gender,ward
        return (self.validate("candidate") and self.register_db("candidate"))
        
        #make call to blockchain registercandidate function
    def validate(self,category):
        ###########################USE THIS ONLY IF YOU HAVE SUPPORT FOR IT ELSE BUZZ OFF#############################
        obj=Face_Detector()
        if obj.detect(os.path.join("D:\\codefundo\\Webapp\\static\\images",self.photo))!=True:
            return False
        # pdb.set_trace()
        if category=="candidate":
            if re.match(r'\b\d{12}\b',self.uid) and int(self.age)>=25 and self.address!="default" and self.fname!="default" and self.lname!="default" and self.photo!="pic.jpg" and self.ward!=10000:
                return True
            else:
                return False
        else:
            if re.match(r'\b\d{12}\b',self.uid) and int(self.age)>=18 and self.address!="default" and self.fname!="default" and self.lname!="default" and self.photo!="pic.jpg" and self.ward!=10000:
                return True
            else:
                return False
    def check_emotion(self):
        obj=Emotion_Detector()
        image=open("img.jpg","rb")
        return obj.detect(image)
    def visa_verification(self,path):
        
        #ocr based verif
        obj=OCR()
        return obj.recognise(path)
        # pass
    def register_voter(self,uid,fname,lname,age,address,gender,ward,photo):
        self.uid,self.fname,self.lname,self.age,self.address,self.photo,self.gender,self.ward=uid,fname,lname,age,address,photo,gender,ward
        return (self.validate("voter") and self.register_db("voter"))
    def register_voter_overseas(self,uid,fname,lname,age,address,gender,ward,photo,visa):
        self.uid,self.fname,self.lname,self.age,self.address,self.photo,self.gender,self.ward,self.visa=uid,fname,lname,age,address,photo,gender,ward,visa
        path=data["ImgPath"]+"\\"+self.visa
        return (self.validate("voter_overseas") and self.register_db("voter_overseas") and self.visa_verification(path))# run if dependencies satisfied
        ##############################################################RUN THE ABOVE visa_verification only post dependency resolution
        ######################################################################################################################
        ########################################################################################################

        #make call to blockchain registervoter function

    def cast_vote(self,uid,fname,lname,vote_uid):
        #make call to blockchain cast_vote function with true for vote variable
        return
    def register_db(self,category):
        # import pdb; pdb.set_trace()
        
        # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        # mydb = myclient["codefundo"]


        uri = "mongodb://codefundocosmos:UWXagx9GOSlg84Z3XqB2k1vTbIqtncuTrfr9WV6jMqH8GrL9TsFyiWBWbv6i1wvHlhyPGjzmtZ0cPjewox3aEA==@codefundocosmos.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
        myclient = pymongo.MongoClient(uri)
        mydb=myclient.codefundo
        # import pdb; pdb.set_trace()
        #with open( os.path.abspath(os.path.join("\codefundo\Webapp\static\PurpleAdmin-Free-Admin-Template-master\images",self.photo)),"rb") as img:
        #with open(os.path.abspath(os.path.join("\codefundo\Webapp\static\PurpleAdmin-Free-Admin-Template-master\images", self.photo)),"rb") as img:
        with open(os.path.join(data["ImgPath"],self.photo),"rb") as img:
            encoded_string = base64.b64encode(img.read())
        if category=="candidate":
            mycol=mydb['cand_reg']
            mycol.insert_one({"UID":self.uid,"First Name":self.fname,"Last Name":self.lname,"Age":self.age,"Address":self.address,
                        "Gender":self.gender,"Ward No":self.ward,"Photo":encoded_string,"Criminal":self.criminal_records,"vote_count":1})
        elif category=='voter':
            mycol=mydb['vote_reg']
            mycol.insert_one({"UID":self.uid,"First Name":self.fname,"Last Name":self.lname,"Age":self.age,"Address":self.address,
                        "Gender":self.gender,"Ward No":self.ward,"Photo":encoded_string})
        else:
            mycol=mydb['vote_reg']
            mycol.insert_one({"UID":self.uid,"First Name":self.fname,"Last Name":self.lname,"Age":self.age,"Address":self.address,
                        "Gender":self.gender,"Ward No":self.ward,"Photo":encoded_string,"Overseas Status":True})
        return True
    # def retrieve_image(request): USE THIS TO RETRIEVE THE IMAGE FROM MONGO
    #     data = db.database_name.find()
    #     data1 = json.loads(dumps(data))
    #     img = data1[0]
    #     img1 = img['image']
    #     decode=img1.decode()
    #     img_tag = '<img alt="sample" src="data:image/png;base64,{0}">'.format(decode)
    #     return HttpResponse(img_tag)
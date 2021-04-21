import pytesseract
import cv2
import re
pytesseract.pytesseract.tesseract_cmd=r'Tesseract-OCR\\tesseract.exe'
str="images/croppedImage.jpg"
def detect_license_plate():
    img=cv2.imread(str)
    result=pytesseract.image_to_string(img)
    result = result.replace('\n', '')
    result = re.sub('\W+', '', result)

    mystates = ['AP', 'AR', 'AS', 'BR', 'CG', 'GA', 'GJ', 'HR', 'HP', 'JK', 'JH', 'KA', 'KL', 'MP', 'MH', 'MN', 'ML',
                'MZ', 'NL', 'OD', 'PB', 'RJ', 'SK', 'TN', 'TS', 'TR', 'UA', 'UK', 'UP', 'WB', 'AN', 'CH', 'DN', 'DD',
                'DL', 'LD', 'PY']

    matched = re.match("[A-Z]{1,2}[0-9]{1,2}[A-Z]{1,2}[0-9]{1,4}", result)
    is_match = bool(matched)
    print(is_match)

    def check(result):
            res=list(result)
            num=[2,3,6,7,8,9]
            for i in num:
                if(res[i]==('O' or 'D' or 'Q')):
                    res[i]='0'
                if(res[i]==('I' or 'T')):
                    res[i]='1'
                if(res[i]==('B' or 'R')):
                    res[i]='8'
                if(res[i]==('Z' or 'J')):
                    res[i]='7'
                if(res[i]=='Y'):
                    res[i]='4'
            return ("".join(res))
    if(not is_match):
        result=check(result)

    if (len(result) > 0):
        # res=re.findall("\s*[AP,AR,AS,BR,CG,GA,GJ,HR,HP,JK,JH,KA,KL,MP,MH,MN,ML,MZ,NL,OD,PB,RJ,SK,TN,TS,TR,UA,UK,UP,WB,AN,CH,DN,DD,DL,LD,PY]{2}\s*[0-9]{1,2}\s*[A-Z]{1,2}\s*[0-9]{1,4}\s*]?",cleanString)
        for word in mystates:
            if (word in result):
                res = re.findall(word + "[0-9]{1,2}\s*[A-Z]{1,2}\s*[0-9]{1,4}\s*]?", result)
                if (len(res) > 0):
                    res1=list(res[0])
                    res1.insert(2,' ')
                    res1.insert(5,' ')
                    res1.insert(8,' ')
                    res[0]="".join(res1)
                    return (res[0])
    res1=list(result)
    res1.insert(2,' ')
    res1.insert(5,' ')
    res1.insert(8,' ')
    result="".join(res1)
    return result
detect_license_plate()
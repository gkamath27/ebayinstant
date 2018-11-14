import json
import requests

headers = {'Content-Type': 'application/json',
'Accept' : 'application/json',
'X-EBAY-C-MARKETPLACE-ID' : 'EBAY-US',
'X-EBAY-C-ENDUSERCTX' : 'ip=0%3A0%3A0%3A0%3A0%3A0%3A0%3A1,userAgentAccept=*%2F*,userAgentAcceptEncoding=gzip%2C+deflate,userAgentAcceptCharset=null,userAgent=Mozilla%2F5.0+%28Windows+NT+6.1%3B+WOW64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F42.0.2311.90+Safari%2F537.36 medium,uri=%2Fexperience%2Fcheckout%2Fv1%2Fsession,referer=null,origUserId=origUserName%3Dalm_us_02%2CorigAcctId%3D26426910,clientId=eBayInc80-8977-4f05-a933-3daa1311213,physicalLocation=country%3DUS,contextualLocation=country%3DUSUS',
     'Authorization': 'Bearer v^1.1#i^1#p^1#f^0#I^3#r^0#t^H4sIAAAAAAAAAO1Yf2wTVRxf90vmHBhDREFjPcCIpL0fvXbtSSsdA5mwH7CBMGLIu7t327HrXXPv3bYSwWVENGiCYBQJqAv/oBIUQYNiAjEEQYRIIi4LCgkKE38HiEHFqO+u3dZNZC0bZCb2n/be+3x/fb4/+u4xbYVFD6yevfpSieum3I42pi3X5WKLmaLCgqmj83LHF+QwaQBXR9uktvz2vHPTEIhpcWE+RHFDR9DdGtN0JDiLYcoydcEASEWCDmIQCVgSaqOVcwXOywhx08CGZGiUu6I8TEkBMSSHJFb2lQZYBQTJqt6js84IU6LC+qHkY0TRDzhfIET2EbJghY4w0HGY4hg26GFZD8vXMQGB8wm83+v3+eop90JoItXQCcTLUBHHXcGRNdN8vbqrACFoYqKEilREZ9VWRyvKZ1bVTaPTdEVSPNRigC3U/2mGIUP3QqBZ8OpmkIMWai1JgghRdCRpob9SIdrjzDW471AdkGRegUHI+nxBRQrww0LlLMOMAXx1P+wVVfYoDlSAOlZxYjBGCRviMijh1FMVUVFR7ra/5llAUxUVmmFqZll0cbSmhorY1qEIEp4YMJsgjmtAgh6J1JAVg6YqCzLHSSIIBj2k2EQPD9hSD4BBjvxSShUJQJZjAyknkpZSKRjgxQxDl1WbUOSuMnAZJBHBgbyxabwRULVebUYVbHvbiwuk8cuG6u2EJzNs4UbdzjmMEZLczuPg2emVxthURQvDXg0DNxz6whSIx1WZGrjp1GmqtFpRmGrEOC7QdIvd6y0t3haf1zAbaI5hWHpR5dxaqRHGANWLV/sE/g3sUZ1QJEikkCrgRJz40krqmDigN1ARnuN9fIr2/l5FBq7+YyEtZLp/swxX8wRZUZH9ogIkUYZBf3A4mieSql96sPL1+RWO9Cz0yIGQ4uFDiuIR/XLAwyoQMhCKohQK/t9D2XVBrWTEYY2hqVIi4164IX3AIlwDTJzItBWuGB2yo8s6LrvXr2tstjwiCkBc9dq15pWMGG0AMuhox2N6etwSSUrcgwJFKzHdIh2aGZKMPKIVOANgUAFkSCrQMtSeAmdnAGoZq7ehWSlPdi9hO0MLffiszEgWwgYZDMRGsyrB7ISBDrQEViWUZWjQlBrJtM00sh54VkZga5yMO0hqOEMzEhlg2UCz8kYEKFPlDjRz5Xav90hl2nRp3CRFhjSjovF4RSxmYSBqsCLzA8nIO4xcMTqVnORHVEgkmcmsqnLyCO51UutFzZLXhMiwTPL24a22T511RhPUyR81Ng1Ng+ZCdsh5HmHpHcazzrVxkt0ZfKickF5fdIPKXtLIfMBLb2Bw/42EqwCPLEZYP8+xpYEA5x9SXDOcfNclruG0eV3Dm20gDOXr8DpJ97/3iuQ4H7bd9S7T7no71+ViaGYyO5G5tzBvQX7eLeORiqFXBYoXqQ06wJYJvU0wEQeqmVvoWjKh+5uWtJu2jseYO3rv2ory2OK0izfmrr6dAnbMuBI2yLIszwQ4H++vZyb27eazt+ePra7cvvjnsec/6nxzw3O/Ti2+/PS5PXcyJb0gl6sgJ7/dlXPzxrOHxFDnSWXM7O37jpbNKx910bWpBHdOE75Yd9sZ10qeKTxO7dl9efzDm748WghOJw4sXT5zasOH4RWh5V1U0YnzTb+9VdC97/4Fxa+O27pm0s6VEy423LftnUcDBzo5fOkXz7HN675dL+89+/vp/at2frfh01tf+uDBTnr1Cvqer9/4ZM3BTWs2HCw+vuXj2vMM/YI158KO0kTVM6u6rOn0E8u2bN7/yiwjeMbdfeTAX/qTfMvS+X983vVQ0fPvPzXFxW07dWLre3teay7bW/nnT4WPf7/+q3nC5vo5o5lFz27cN+fH1+/WmksPH6lyH3rxAn/s5SUd7q4f1iZOHh51qnvXrsWTd0/p/KzpkR2jqWT6/gYwv1qIAxUAAA=='}


#Make a call to create
def makeCreateServiceCall():

    api_url = 'http://phxxoneor-2823469.phx02.dev.ebayc3.com:8080/experience/checkout/v1/session'

    payload = ({'itemId':'330010768476','transactionId':'-1','quantity':'1'})
    print(headers)

    response = requests.post(api_url, data=json.dumps(payload),headers=headers)

    if response.status_code == 200:
        print("this is success");
        ssh_keys = json.loads(response.content.decode('utf-8'));
        sessionId = ssh_keys['meta']['__xo']['sessionId']
    # meta = ssh_keys['meta']
    # sessionId = meta[]
        print(sessionId)
        makePurchaseServiceCall(sessionId)
    else :
        print("there is an error"+str(response.status_code))


#Make a call to purchase

def makePurchaseServiceCall(sessionId):
    api_url = 'http://phxxoneor-2823469.phx02.dev.ebayc3.com:8080/experience/checkout/v1/session/'+sessionId+'/purchase'
    payload = ({'errorId': 'null'})

    print(api_url)
    response = requests.put(api_url,data=json.dumps(payload),headers=headers)

    if response.status_code == 200:
        print("this is purchase success");
        print(ssh_keys['meta']['__xo']['sessionId']);
    else :
        print("there is an error"+str(response.status_code))


makeCreateServiceCall()

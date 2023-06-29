import requests
from pprint import pprint
import json
import urllib
import urllib.request

vk_token = ' '
api_version='5.131'
user_ids=''
ya_token =''
foto_dict={}

# def get_users_info(token,api_ver,user_id):
#     url='https://api.vk.com/method/users.get'
#     params={
#      "user_ids": user_id,
#      "access_token": token,
#      "v": "5.131",
#      "fields": "education, sex,photo_id"
#  }
#     res = requests.get(url, params=params)
#     pprint(res.json())
def get_foto_info(token,api_ver):
    url='https://api.vk.com/method/photos.get'
    params={
        "user_ids": user_ids,
        "access_token": vk_token,
        "v": "5.131",
        "album_id":'profile',
        "foto_ids": 'foto_ids',
        "extended":'1',
        "photo_sizes":'1'
    }
    res=requests.get(url,params=params)
    dict=res.json()
    #pprint (dict)
    for i in dict['response']['items']:
        count_like=i['likes']['user_likes']
        for y in range(len(i['sizes'])):
            #count_like=['likes']['user_likes']
            url=i['sizes'][y]['url']
            foto_size=i['sizes'][y]['width']*i['sizes'][y]['height']
            foto_dict['count_like']=count_like
            foto_dict['foto_url']=url
            foto_dict['foto_size']=foto_size
        #pprint(foto_dict)
        return foto_dict
def get_file_yandex(token=ya_token):
    file_url=get_foto_info(token=vk_token,api_ver=api_version)
    disk_file_path=str(file_url['foto_url']).split(sep="?")
    url_path=disk_file_path[0]
    ya_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    headers ={'Content-Type':'application\json',
                'Authorization':f'OAuth {token}'
    }
    params ={" path":url_path,"overwrite":"true"}
    href_response=requests.post(url_path,headers=headers)
    print(href_response)
    #return ya_url.href_response()

#get_users_info(token=token,api_ver=api_version,user_id=user_ids)
get_foto_info(token=vk_token,api_ver=api_version)
get_file_yandex(token=ya_token)

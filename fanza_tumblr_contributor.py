import requests
import json
import pytumblr
import random

def main():
    #dmm_api_info
    APIID = 'DMM API ID'
    affiliateID = 'DMM affiliate ID'
    HITS = '5'
    KEYWORD = random.choice([
        '%E4%BB%81%E7%A7%91%E7%99%BE%E8%8F%AF&oq=%E4%BB%81%E7%A7%91%E7%99%BE%E8%8F%AF', #検索文字列１
        '%E6%96%B0%E4%BA%BA&oq=%E6%96%B0%E4%BA%BA', #検索文字列２
        '%E5%B7%A8%E4%B9%B3&oq=%E5%B7%A8%E4%B9%B3', #検索文字列３
        ])
    OFFSET = random.randint(1, 50)

    #tumblr_auth_info
    consumer_key = 'tumblr consumer key'
    consumer_secret = 'tumblr consumer secret key'
    oauth_token = 'tumblr oauth token' 
    oauth_token_secret = 'oauth token secret'
    blog_name = 'tumblr blog name'
    
    get_video = fanza_movie_list_up(APIID, affiliateID, HITS, OFFSET, KEYWORD)
    print(get_video)
    post_tumblr(list(get_video), consumer_key, consumer_secret, oauth_token, oauth_token_secret, blog_name)


def fanza_movie_list_up(apiid, affiliateID, hits, offset, keyword):
    url = 'https://api.dmm.com/affiliate/v3/ItemList?api_id='+ apiid +'&affiliate_id=' + affiliateID + '&site=FANZA&service=digital&floor=videoa&offset=' + str(offset) + '&hits=' + str(hits) + '&sort=date&keyword=' + keyword + '=json'
    r = requests.get(url)
    result_json = r.json()
    hits_rand_num = random.randint(0, 4) 
    return_list = []
    return_list = return_list + [result_json['result']['items'][hits_rand_num]['title']] 
    return_list = return_list + [result_json['result']['items'][hits_rand_num]['imageURL']['large']]
    return_list = return_list + [result_json['result']['items'][hits_rand_num]['affiliateURL']]

    return return_list
    
def post_tumblr(s_media_list, con_key, con_sec, oau_token, oau_sec, blog_name):
    title_info = s_media_list[0]
    body_info = "<h3>" + s_media_list[0] + "</h3><img src= " + s_media_list[1] + "><a href=" + s_media_list[2] + ">FANZAへアクセス</a>"
    #tags_info = s_media_actor
    print(body_info)
    client = pytumblr.TumblrRestClient(con_key, con_sec, oau_token, oau_sec)
    client.create_text(blog_name, state="published", title=title_info, body=body_info)
   
    print('ブログを投稿しました。')

if __name__ == '__main__':
    main()


# coding: utf-8

# In[4]:


import codecs
import pandas as pd
from pyvi import ViTokenizer
from underthesea import word_tokenize

df_vnexpress = pd.read_json(codecs.open('data/vnexpress.json','r','utf-8'))
df_dantri = pd.read_json(codecs.open('data/dantri.json','r','utf-8'))
df_vietnamnet = pd.read_json(codecs.open('data/vietnamnet.json','r','utf-8'))

data_vnexpress = pd.DataFrame(df_vnexpress.response['docs'])[['url','content']]
data_dantri = pd.DataFrame(df_dantri.response['docs'])[['url','content']]
data_vietnamnet = pd.DataFrame(df_vietnamnet.response['docs'])[['url','content']]

labels = [
('Chinh tri Xa hoi', 0),
('Cong Nghe', 1),
('Doi Song', 2),
('Du Lich', 3),
('Giai Tri', 4),
('Giao Duc', 5),
('Khoa hoc', 6),
('Kinh doanh', 7),
('Phap Luat ', 8),
('Suc Khoe', 9),
('The Gioi', 10),
('The Thao', 11),
('Xe', 12),
]


# In[5]:


regex_list_filter_url_dantri= [
('^.*dantri\.com\.vn\/bong-da-tbn\/'),
('^.*dantri\.com\.vn\/bong-da-trong-nuoc\/'),
('^.*dantri\.com\.vn\/chinh-tri\/'),
('^.*dantri\.com\.vn\/dien-thoai\/'),
('^.*dantri\.com\.vn\/doi-song\/'),
('^.*dantri\.com\.vn\/du-lich\/'),
('^.*dantri\.com\.vn\/du-lich-kham-pha\/'),
('^.*dantri\.com\.vn\/giai-tri\/'),
('^.*dantri\.com\.vn\/giao-duc-khuyen-hoc\/'),
('^.*dantri\.com\.vn\/khoa-hoc\/'),
('^.*dantri\.com\.vn\/khoa-hoc-cong-nghe\/'),
('^.*dantri\.com\.vn\/khoa-hoc-doi-song\/'),
('^.*dantri\.com\.vn\/khuyen-hoc\/'),
('^.*dantri\.com\.vn\/kinh-doanh\/'),
('^.*dantri\.com\.vn\/lam-dep\/'),
('^.*dantri\.com\.vn\/o-to-xe-may\/'),
('^.*dantri\.com\.vn\/phap-luat\/'),
('^.*dantri\.com\.vn\/suc-khoe\/'),
('^.*dantri\.com\.vn\/suc-manh-so\/'),
('^.*dantri\.com\.vn\/the-gioi\/'),
('^.*dantri\.com\.vn\/the-thao\/'),
('^.*dantri\.com\.vn\/the-thao-quoc-te\/'),
('^.*dantri\.com\.vn\/the-thao-trong-nuoc\/'),
('^.*dantri\.com\.vn\/vi-tinh\/'),
('^.*dantri\.com\.vn\/xa-hoi\/'),
('^.*dantri\.com\.vn\/van-hoa\/'),    
]
regex_content_match_dantri = '^(.*?[0-9]{2}\/[0-9]{2}\/[0-9]{4} \- [0-9]{2}\:[0-9]{2})'


# In[6]:


regex_list_filter_url_vnexpress= [
'^.*/vnexpress\.net\/bong-da\/',
'^.*/vnexpress\.net\/doi-song\/',
'^.*/vnexpress\.net\/du-lich\/',
'^.*/vnexpress\.net\/giai-tri\/',
'^.*/vnexpress\.net\/giao-duc\/',
'^.*/vnexpress\.net\/khoa-hoc\/',
'^.*/vnexpress\.net\/kinh-doanh\/',
'^.*/vnexpress\.net\/oto-xe-may\/',
'^.*/vnexpress\.net\/phap-luat\/',
'^.*/vnexpress\.net\/so-hoa\/',
'^.*/vnexpress\.net\/suc-khoe\/',
'^.*/vnexpress\.net\/the-gioi\/',
'^.*/vnexpress\.net\/the-thao\/',
]
regex_content_match_vnexpress = '^(.*?[0-9]{2}\:[0-9]{2} \(GMT\+7\))'


# In[7]:


regex_list_filter_url_vietnamnet= [
'^.*vietnamnet\.vn\/vn\/cong-nghe\/',
'^.*vietnamnet\.vn\/vn\/doi-song\/',
'^.*vietnamnet\.vn\/vn\/giai-tri\/',
'^.*vietnamnet\.vn\/vn\/giao-duc\/',
'^.*vietnamnet\.vn\/vn\/kinh-doanh\/',
'^.*vietnamnet\.vn\/vn\/oto-xe-may\/',
'^.*vietnamnet\.vn\/vn\/phap-luat\/',
'^.*vietnamnet\.vn\/vn\/suc-khoe\/',
'^.*vietnamnet\.vn\/vn\/the-gioi\/',
'^.*vietnamnet\.vn\/vn\/the-thao\/',
]
regex_content_match_vietnamnet= '^(.*?[0-9]{2}\:[0-9]{2} GMT\+7)'


# In[8]:


print('dantri: %d' %  data_dantri.shape[0])
print('express: %d' % data_vnexpress.shape[0])
print('vietnamnet: %d' % data_vietnamnet.shape[0])


# In[9]:


# Get all urls in domain https://dantri.com.vn
data_dantri = data_dantri[data_dantri.url.str.match(pat='^https://dantri\.com\.vn')]
# Get all urls in domain https://vnexpress.net
data_vnexpress = data_vnexpress[data_vnexpress.url.str.match(pat='^https://vnexpress\.net')]
# Get all urls in domain https://vietnamnet.vn
data_vietnamnet = data_vietnamnet[data_vietnamnet.url.str.match(pat='^https://(m\.)?vietnamnet\.vn')]


# In[10]:


def filter_url(data, regex_list_filter_url, regex_content_match):
    data_filterd_url = pd.DataFrame()
    for regex in regex_list_filter_url:
        print( '%.5d:  ' % data[data.url.str.match(regex)].shape[0] +regex)
        data_filterd_url = data_filterd_url.append(data[data.url.str.match(regex)],ignore_index=True)

    data = data_filterd_url[data_filterd_url.content.str.match(regex_content_match)]
    print(data.shape)
    return data


# In[11]:


def filter_short_data(data, num_dot):
    return data[data.content.str.count('[^\.]\.')>num_dot]


# In[12]:


data_vnexpress = filter_url(data_vnexpress, regex_list_filter_url_vnexpress,regex_content_match_vnexpress)

data_dantri = filter_url(data_dantri,regex_list_filter_url_dantri,regex_content_match_dantri)

data_vietnamnet = filter_url(data_vietnamnet,regex_list_filter_url_vietnamnet,regex_content_match_vietnamnet)


# In[13]:


regex_list_parse_vnexpress =[
 '^(.*?[0-9]{2}\:[0-9]{2} \(GMT\+7\))',
'(Quảng cáo Xem nhiều nhất.*)',
'(Tin liên quan\:.*)$',
'(Quảng cáo   Ý kiến bạn đọc.*)$',
'(Xem nhiều nhất.*)$',
'(Quảng cáo Quảng cáo.*)$',
'(Ý kiến bạn đọc.*)$',
'(Tags.*)$',
'(Quảng cáo  )$',
'(Gửi bài viết.*)$',
]


# In[14]:


regex_list_parse_dantri=[
    '^(.*?[0-9]{2}\/[0-9]{2}/[0-9]{4} - [0-9]{2}\:[0-9]{2})',
    '^(.*?Chia sẻ Dân trí)',
    '(Tag : .*)$',
]


# In[15]:


regex_list_parse_vietnamnet=[
 '^(.*?[0-9]{2}\:[0-9]{2} GMT\+7)',
    '(Gửi bình luận Chủ đề.*)$',
]


# In[16]:


for regex in regex_list_parse_vnexpress:
    data_vnexpress = data_vnexpress.replace(to_replace=regex,regex=True,value='')


# In[17]:


for regex in regex_list_parse_dantri:
    data_dantri = data_dantri.replace(to_replace=regex,regex=True,value='')


# In[18]:


for regex in regex_list_parse_vietnamnet:
    data_vietnamnet = data_vietnamnet.replace(to_replace=regex,regex=True,value='')


# In[19]:


data_vnexpress = filter_short_data(data_vnexpress,15)
data_dantri = filter_short_data(data_dantri,15)
data_vietnamnet = filter_short_data(data_vietnamnet,15)


# In[20]:


maps = [
    ( '\/bong-da\/',11),
    ('\/doi-song\/',2),
    ('\/du-lich\/', 3),
    ('\/giai-tri\/', 4),
    ('\/giao-duc\/', 5),
    ('\/khoa-hoc\/', 6),
    ('\/kinh-doanh\/', 7),
    ('\/oto-xe-may\/', 12),
    ('\/phap-luat\/', 8),
    ('\/so-hoa\/', 1),
    ('\/suc-khoe\/',9),
    ('\/the-gioi\/',10),
    ('\/the-thao\/', 11),
]
count = [0 for x in range(13)]

for name,idx in maps:
    count[idx]+=data_vnexpress[data_vnexpress.url.str.contains(name)].shape[0]
    data_vnexpress.loc[data_vnexpress.url.str.contains(name), 'label'] = idx
for label, idx in labels:
    print('%s: %d' % (label,count[idx]))
print('Sum: %d' % sum(count))


# In[21]:


maps = [
    ('\/cong-nghe\/', 1),
    ('\/doi-song\/', 2),
    ('\/doi-song\/du-lich\/', 3),
    ('\/giai-tri\/', 4),
    ('\/giao-duc\/', 5),
    ('\/kinh-doanh\/', 7),
    ('\/oto-xe-may\/', 12),
    ('\/phap-luat\/', 8),
    ('\/suc-khoe\/', 9),
    ('\/the-gioi\/', 10),
    ('\/the-thao\/', 11),
]
count = [0 for x in range(13)]

for name,idx in maps:
    count[idx]+=data_vietnamnet[data_vietnamnet.url.str.contains(name)].shape[0]
    data_vietnamnet.loc[data_vietnamnet.url.str.contains(name), 'label'] = idx
for label, idx in labels:
    print('%s: %d' % (label,count[idx]))
print('Sum: %d' % sum(count))


# In[22]:


maps = [
    ('\/bong-da-tbn\/', 11),
    ('\/bong-da-trong-nuoc\/', 11),
    ('\/chinh-tri\/', 0),
    ('\/dien-thoai\/', 1),
    ('\/doi-song\/', 2),
    ('\/du-lich\/', 3),
    ('\/du-lich-kham-pha\/', 3),
    ('\/giai-tri\/', 4),
    ('\/giao-duc-khuyen-hoc\/', 5),
    ('\/khoa-hoc\/', 6),
    ('\/khoa-hoc-cong-nghe\/', 6),
    ('\/khoa-hoc-doi-song\/', 6),
    ('\/khuyen-hoc\/', 5),
    ('\/kinh-doanh\/', 7),
    ('\/lam-dep\/', 9),
    ('\/o-to-xe-may\/', 12),
    ('\/phap-luat\/', 8),
    ('\/suc-khoe\/', 9),
    ('\/suc-manh-so\/', 1),
    ('\/the-gioi\/', 10),
    ('\/the-thao\/', 11),
    ('\/the-thao-quoc-te\/', 11),
    ('\/the-thao-trong-nuoc\/', 11),
    ('\/van-hoa\/', 4),
    ('\/vi-tinh\/', 1),
    ('\/xa-hoi\/', 0),
]
count = [0 for x in range(13)]

for name,idx in maps:
    count[idx]+=data_dantri[data_dantri.url.str.contains(name)].shape[0]
    data_dantri.loc[data_dantri.url.str.contains(name), 'label'] = idx
for label, idx in labels:
    print('%s: %d' % (label,count[idx]))
    
print('Sum: %d' % sum(count))


# In[ ]:


print('dantri: %d' %  data_dantri.shape[0])
print('express: %d' % data_vnexpress.shape[0])
print('vietnamnet: %d' % data_vietnamnet.shape[0])


# In[ ]:


data_vietnamnet['content'] = data_vietnamnet.apply(lambda row: word_tokenize(row['content'], format="text"), axis=1)

data_dantri['content'] = data_dantri.apply(lambda row: word_tokenize(row['content'], format="text"), axis=1)

data_vnexpress['content'] = data_vnexpress.apply(lambda row: word_tokenize(row['content'], format="text"), axis=1)


# In[ ]:


data_dantri.url.to_csv('url.csv',header=False,index=False)
data_vnexpress.url.to_csv('url2.csv',header=False,index=False)
data_vietnamnet.url.to_csv('url3.csv',header=False,index=False)


# In[ ]:


data_dantri.to_csv('filtered_data/dantri.csv',index=False, header=True)
data_vnexpress.to_csv('filtered_data/vnexpress.csv',index=False,header=True)
data_vietnamnet.to_csv('filtered_data/vietnamnet.csv',index=False,header=True)


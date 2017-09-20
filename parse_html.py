import re, urllib.request, os, sys, random, json
# save
def writeFile(path, s):
    # 打开
    fd = os.open(path, os.O_RDWR|os.O_CREAT)
    # 写入
    os.write(fd, bytes(s, 'UTF-8'))
    # 关闭
    os.close(fd)
    print('写入完成！%s\%s' % (os.getcwd(), path))
# html
def init_html(url):
    # 开始
    try :
        url = urllib.request.Request(url)
        url.add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/7.2.0.12990' ) #隐藏
        data = urllib.request.urlopen( url )
    except ( urllib.error.URLError ) :
        print( '网页打不开，请稍后 (或检查网络)' )
        sys.exit(0)
    # 解析 html
    html = data.read().decode('UTF-8')
    return html
# li
def init_li(li):
    arr = []
    for div in li:
        o = {}
        # o['url'] 网址
        o['url'] = re.search('href="(.+?)"', div).group(1)
        # o['img'] 图片
        o['img'] = re.search('src="(.+?)!list', div).group(1)
        # o['title'] 名称
        o['title'] = re.search('alt="(.+?)"', div).group(1)
        # o['money'] 价格
        o['money'] = re.search('<span class="item-price"><i>&yen;<\/i>(.+?)<\/span>', div).group(1)
        dateCity = re.search('<span class="item-time">(.+?)<\/span>', div).group(1).split(' ')
        # o['date'] 时间
        o['date'] = dateCity[0]
        # o['city'] 城市
        o['city'] = dateCity[1][0:2]
        arr.append(o)
    return arr
# json
def init_json(url):
    html = init_html(url)
    li = re.findall('<li class="wonderful-listItem ">([\s\S]+?)<\/li>', html)
    arr = init_li(li)
    return arr
# main
def main():
    start = 1
    end = 245

    arr = []
    for i in range(start, end + 1):
        print('提示：正在下载第 %s 页……', i)
        url = 'http://hd.8264.com/xianlu-0-0-0-0-0-2-' + str(i)
        arr = arr + init_json(url)
    # 写入
    writeFile("db.json", json.dumps(arr, indent=2, ensure_ascii=False))

if __name__ == '__main__' :
    main()
    print('运行结束')

# '''
# 姓名：{name}
# 网址：{url}'''.format(**{
#     'name': '瓜',
#     'url': 'space.bilibili.com/39066904',
# })

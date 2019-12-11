class spider():
    def __init__(self,url,q):
        self.url = url
        self.q = q
        self.headers = {
            'Host'
        }

    def run(self):
        self.parse_page()

    def send_request(self,url):
        '''
        :param url: 发送网页请求
        :return: 返回源码
        '''
        pass

    def parse_page(self):
        '''
        解析网站源码，采用xpath提取。
        :return:
        '''

        
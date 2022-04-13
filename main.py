from flask import Flask

"""
    URL과 URI차이
    URL: https://www.naver.com/news
    URI: https://www.naver.com/news?name=dev&pw=1111 전부
    주소: https://www.naver.com 까지
    라우팅: / news
    
    웹서버는 정적인 정보를 html 페이즈를 반환하는데 동적으로 데이터를 반환하도록 하기 위해서는 was 프레임 워크가 필요
    * WAS프레임워크로는 flask, django, rails, node.js등이 존재
    
    closer 예제 중하나
    def outer_func(num):
        def inner_func():
            return 'complex'
        return inner_func
    fn = outer_func(10)
    print(fn()) --> 'complex 
    다르게 표현하면 fn = outer_func(10)()
"""

# 플라스크에서 라우팅을 설정하는방법
app = Flask(__name__)

host_addr = "127.0.0.1"
port_num = "8080"
def html_creator(tag):
    def text_wrapper(msg):
        return f"<{tag}>{msg}<{tag}>"
    return text_wrapper

@app.route('/hello')
def hello():
    h1_html_tag = html_creator("h1")
    #h1_html_tag("Hello World")
    return h1_html_tag("Hello World")

if __name__ == "__main__":
    app.run(host=host_addr, port=port_num, debug=True)

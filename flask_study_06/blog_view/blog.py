from flask import Flask, Blueprint, request, render_template, make_response , jsonify, redirect, url_for

blog_abtest = Blueprint('blog', __name__)

@blog_abtest.route('/set_email', methods=['GET', 'POST'])
def test():
    if request.method == "GET":
        print(request.args.get('user_email'))
        return redirect(url_for('blog.test_blog'))

    elif request.method == "POST":
        print('set_email', request.headers)
        # content type이 application/json인 경우 get_json() 사용 가능
        print(request.form['user_email'])
        return redirect(url_for('blog.test_blog'))
    #return redirect("/blog/test_blog")
    

@blog_abtest.route('/test_blog', methods=['GET'])
def test_blog():
    return render_template('blog_A.html')
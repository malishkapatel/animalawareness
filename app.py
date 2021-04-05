from flask import Flask , render_template , session , request , redirect , url_for
app = Flask(__name__)

app.config['SECRET_KEY'] = 'rgvufsuebhfzdsh'
user_details = {'malishka' : '123' , 'arpita':'456' , 'ramya':'abc' ,}

@app.route('/index/<name>' , methods = ['POST' , 'GET'])
def index(name):
    return render_template('index1.html' , name = name)

# @app.route('/pizza')
# def pizza(): 
#     return '<h1>ilovepizza</h1>'
#THIS IS ABOUT LEARNING USING GET METHOD
@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return "<h1>Hi {}. You are from {}.You are on the query page!</h1>".format(name,location)
#THIS IS ABOUT POST METHOD
@app.route('/process' , methods = ['post'])
def process():
    name = request.form['name']
    location = request.form['location']
    print (name)
    return render_template('form.html' , name = name , location = location)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/register_user' , methods = ['post'])
def register_user():
    user = request.form.get('username')
    password = request.form.get('password')
    session['user'] = request.form['username']
    user_details[user] = password
    print (user_details)   
    return render_template('registersucess.html')


@app.route('/startquiz')
def startquiz():
    if session.get('authenticated') == True:
        session['score'] = 0
        session ['questions_attempted'] = {}
        return render_template('startquiz.html' , score = 0) 
    else:
        return render_template('loginfailure.html')

@app.route('/login' , methods = ["GET" , "POST"])
def login():
    if session.get('authenticated') == True:
        return render_template('loginsucess.html')
    else:
        return render_template('login.html')

@app.route('/user_validation' , methods = ['post'])
def user_validation():
    username = request.form.get('username')
    password = request.form.get('password')
    return_value = loginsucess(user_details , username , password)
    if return_value == True:
        session['authenticated'] = True
        return render_template('loginsucess.html', username = username)
    else: 
        session['authenticated'] = False
        return render_template('loginfailure.html')
    # getpass = user_details.get(user , "User not found")
    # if password == getpass:
    #     return render_template('loginsucess.html')
    # else:
    #     return render_template('login.html')
    # print (user_details)
def loginsucess(dictionary , username , password):
    if dictionary.get(username , "User not found") == password:
        return True
    else:
        return False
@app.route('/q1')
def q1():
    return render_template('q1.html' , score = 0)

@app.route('/q2' , methods = ['POST'])
def q2():
    p_score = session.get('score' , 0)
    c_score = p_score
    s_answer = request.form.get('answer')
    c_answer = request.form.get('ca')
    questions_attempted_dict = session.get('questions_attempted' , {})
    if s_answer == c_answer:
        marks = 10
        if questions_attempted_dict.get('1' , False) == False:
            c_score = p_score + marks 
            session['score'] = c_score
    questions_attempted_dict['1'] = True
    return render_template('q2.html' , score = c_score)

@app.route('/q3' , methods = ['POST'])
def q3():
    p_score = session.get('score' , 0)
    c_score = p_score
    s_answer = request.form.get('answer')
    c_answer = request.form.get('ca')
    questions_attempted_dict = session.get('questions_attempted' , {})
    if s_answer == c_answer:
        marks = 10
        if questions_attempted_dict.get('2' , False) == False:
            c_score = p_score + marks 
            session['score'] = c_score
    questions_attempted_dict['2'] = True
    return render_template('q3.html' , score = c_score)

@app.route('/q4' , methods = ['POST'])
def q4():
    p_score = session.get('score' , 0)
    c_score = p_score
    s_answer = request.form.get('answer')
    c_answer = request.form.get('ca')
    questions_attempted_dict = session.get('questions_attempted' , {})
    if s_answer == c_answer:
        marks = 10
        if questions_attempted_dict.get('3' , False) == False:
            c_score = p_score + marks 
            session['score'] = c_score
    questions_attempted_dict['3'] = True
    return render_template('q4.html' , score = c_score)

@app.route('/q5' , methods = ['POST'])
def q5():
    p_score = session.get('score' , 0)
    c_score = p_score
    s_answer = request.form.get('answer')
    c_answer = request.form.get('ca')
    questions_attempted_dict = session.get('questions_attempted' , {})
    if s_answer == c_answer:
        marks = 10
        if questions_attempted_dict.get('4' , False) == False:
            c_score = p_score + marks 
            session['score'] = c_score
    questions_attempted_dict['4'] = True
    return render_template('q5.html' , score = c_score)

@app.route('/q6' , methods = ['POST'])
def q6():
    p_score = session.get('score' , 0)
    c_score = p_score
    s_answer = request.form.get('answer')
    c_answer = request.form.get('ca')
    questions_attempted_dict = session.get('questions_attempted' , {})
    if s_answer == c_answer:
        marks = 10
        if questions_attempted_dict.get('5' , False) == False:
            c_score = p_score + marks 
            session['score'] = c_score
    questions_attempted_dict['5'] = True
    return render_template('q6.html' , score = c_score)

@app.route('/q7' , methods = ['POST'])
def q7():
    p_score = session.get('score' , 0)
    c_score = p_score
    s_answer = request.form.get('answer')
    c_answer = request.form.get('ca')
    questions_attempted_dict = session.get('questions_attempted' , {})
    if s_answer == c_answer:
        marks = 10
        if questions_attempted_dict.get('6' , False) == False:
            c_score = p_score + marks 
            session['score'] = c_score
    questions_attempted_dict['6'] = True
    return render_template('q7.html' , score = c_score)

@app.route('/q8' , methods = ['POST'])
def q8():
    p_score = session.get('score' , 0)
    c_score = p_score
    s_answer = request.form.get('answer')
    c_answer = request.form.get('ca')
    questions_attempted_dict = session.get('questions_attempted' , {})
    if s_answer == c_answer:
        marks = 10
        if questions_attempted_dict.get('7' , False) == False:
            c_score = p_score + marks 
            session['score'] = c_score
    questions_attempted_dict['7'] = True
    return render_template('q8.html' , score = c_score)

@app.route('/q9' , methods = ['POST'])
def q9():
    p_score = session.get('score' , 0)
    c_score = p_score
    s_answer = request.form.get('answer')
    c_answer = request.form.get('ca')
    questions_attempted_dict = session.get('questions_attempted' , {})
    if s_answer == c_answer:
        marks = 10
        if questions_attempted_dict.get('8' , False) == False:
            c_score = p_score + marks 
            session['score'] = c_score
    questions_attempted_dict['8'] = True
    return render_template('q9.html' , score = c_score)

@app.route('/q10' , methods = ['POST'])
def q10():
    p_score = session.get('score' , 0)
    c_score = p_score
    s_answer = request.form.get('answer')
    c_answer = request.form.get('ca')
    questions_attempted_dict = session.get('questions_attempted' , {})
    if s_answer == c_answer:
        marks = 10
        if questions_attempted_dict.get('9' , False) == False:
            c_score = p_score + marks 
            session['score'] = c_score
    questions_attempted_dict['9'] = True
    return render_template('q10.html' , score = c_score)

@app.route('/endquiz' , methods = ['POST'])
def endquiz():
    p_score = session.get('score' , 0)
    c_score = p_score
    s_answer = request.form.get('answer')
    c_answer = request.form.get('ca')
    questions_attempted_dict = session.get('questions_attempted' , {})
    if s_answer == c_answer:
        marks = 10
        if questions_attempted_dict.get('10' , False) == False:
            c_score = p_score + marks 
            session['score'] = c_score
    questions_attempted_dict['10'] = True

    return render_template('endquiz.html' , score = c_score)


def addition(num1 , num2):
    add_num = num1 + num2
    return add_num

def subtraction(num1,num2):
    sub_num = num1 - num2
    return sub_num

def multiplication(num1,num2):
    multiply_num = num1*num2
    return multiply_num
    
def division(num1,num2):
    divide_num = num1/num2
    return divide_num

@app.route('/calc')
def calculator():
    return render_template("calc.html")

@app.route('/verify_calc', methods = ['post'])
def verify_calc():
    num1 = request.form.get("number1")
    num2 = request.form.get("number2")
    operator = request.form.get("operator")
    num1 = int(num1)
    num2 = int(num2)
    if operator == 'Addition':
        result = addition(num1 , num2)

    elif operator == 'Subtraction':
        result = subtraction(num1 , num2)

    elif operator == 'Multiply':
        result = multiplication(num1 , num2)

    elif operator == "Division":
        result = division(num1 , num2)

    return render_template('verify_calc.html' ,result = result , num1 = num1 , num2 = num2 , operator = operator)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))
    



if __name__ == '__main__': 
    app.run(debug=True)
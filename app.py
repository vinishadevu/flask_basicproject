from flask import Flask


FAI=Flask(__name__)

@FAI.route('/wish/<name>')
def wish(name):
    return f'hello {name} how are you'


if __name__=='__main__':
    FAI.run(debug=True,port=5001,host='192.168.59.152')
 
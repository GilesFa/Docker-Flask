import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
import mod

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'hello'

@app.route('/test', methods=['POST'])
def postinput():
		#定義接收資料的格式為json
    instervalues = request.get_json()
    x1=instervalues['a']
    x2=instervalues['b']
    x3=instervalues['c']
    x4=instervalues['d']

    #接收前端輸入對應的資料，然後存入numpy array
    input = np.array([[x1, x2, x3 ,x4]])
    #將資料輸出到後端終端機
    print(input)
		
		#將array的資料放到mod模組中運行
    result = mod.max_num(input)
		
		#以json方式返回result的結果
    return jsonify({'return max value': str(result)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) #debug=True flask將會自動重啟

from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
app = Flask(__name__)
CORS(app) 
API_KEY = "7vwLRNs7rNgUWFcpTtUA1Zmcwe0iV6jNwVCiv0wp"
headers = {"Authorization": f"Token {API_KEY}"}

@app.route('/search_sound', methods=['GET'])
def search_sound():
    query = request.args.get('query', default='Water', type=str)

    search_url = "https://freesound.org/apiv2/search/text/"
    params = {
        "query": query,
        "filter": "duration:[1.0 TO 5.0]",
        "fields": "id,name,previews",
        "page_size": 1
    }

    response = requests.get(search_url, headers=headers, params=params)
    results = response.json()
    print(response.text)
    if results.get('results'):
        sound = results['results'][0]
        preview_url = sound['previews']['preview-hq-mp3']
        return jsonify({'success': True, 'sound': preview_url})
    else:
        return jsonify({'success': False, 'message': 'No sound found'})

if __name__ == '__main__':
    app.run(debug=True)
app.run(debug=True, host='0.0.0.0', port=5000)

import json

NLP_data = {
    'tone': 'Person',
    'text': 'Wayne',
    'relevance': 0.3
}


tone_analysis = {
    'emotion': '',
    'writing': '',
    'social': ''

}

tone_analysis_emotion = {
    'anger': '',
    'disguist': '',
    'fear': '',
    'joy': '',
    'saddness': ''
}
tone_analysis_writing = {
    'analytical': '',
    'confident': '',
    'tennetative': ''
}

tone_analysis_social = {
    'openness': '',
    'Conscientiousness': '',
    'extroversion': '',
    'agreeableness': '',
    'emotional range': ''
}

tone = {
    'analysis' : tone_analysis,
    'emotion': tone_analysis_emotion,
    'writing' : tone_analysis_writing,
    'social' : tone_analysis_social
}

data = {
    'NLP' : NLP_data,
    'tone' : tone

}

json_str = json.dumps(data)

# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)

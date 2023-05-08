from flask import Flask, render_template
import os

app = Flask(__name__)

userinfo = {'name': 'Michael Rudy',
    'shortIntro': 'Information Mangement Specialist at United States Department of State',
    'longIntro': 'I am currently self-learning computer science and software development through research and development. I have taken software development post-graduate classes at UPenn and cybercrime classes at Michigan State University.',
    'work': [{'jobTitle': 'Information Management Specialist', 'desc': "Developed cpu-intense post-processing toolkits using Python", "year": "2021 - Present", 'link':'./static/img/space.jpg'},],
    'skills': ['./static/img/skillicons/c-.png','./static/img/skillicons/css-3.png', './static/img/skillicons/html-5.png',
    './static/img/skillicons/js.png','./static/img/skillicons/python.png'],
    'education': [{'type': 'Bachelors of Business Administration', 'from': 'The George Washington University', 'when': '2018 - 2021', 'desc': 'Major: Information Systems; Minor: Economics', 'link': './static/img/OSU.jpg'}],
    'email': 'michael4rudy@gmail.com',
    'hobbies':  [{'name': 'Golf', 'caption': 'golf', 'img': './static/img/hobbies_gallery/basketball.jpeg', 'active': 'active'},
    			],
    'project_rows': [[{'name': 'Birdify', 'tag': 'Gamified golf scorecard keeping app.', 'tools': 'Xcode, SwiftUI', 'link': 'https://github.com/MichaelRudy/Birdify', 'img': './static/img/hobbies_gallery/R.R.png'},
    ],
    ],
    'facebook': 'facebook.com',
    'github': 'github.com',
    'instagram': 'instagram.com',
    'linkedin':'linkedin.com' ,
    'twitter':'twitter.com'
 }

@app.route('/')
def home():
	return render_template('index.html', title='The Rudy Corp.', url=os.getenv('URL'), name=userinfo['name'],
    shortIntro=userinfo['shortIntro'], longIntro = userinfo['longIntro'], work = userinfo['work'], skills = userinfo['skills'],
    education = userinfo['education'], email=userinfo['email'], facebook = userinfo['facebook'], instagram = userinfo['instagram'],
    github=userinfo['github'], linkedin=userinfo['linkedin'], twitter = userinfo['twitter'], profilepic='./static/img/profile_pic.jpg',)


if __name__ == '__main__':
	app.run(debug=True)



from flask import Flask, render_template
import os

app = Flask(__name__)
info = {
    'name': 'The Rudy Corp.',
    'desc': """I am currently self-learning computer science and software development through research and development. 
    I have taken formal post-graduate courses at UPenn and Michigan State University. I am currently interested in bulding 
    a platform for scalable web-applications; a place to host all of my interests and projects.""",
    'education': """I earned a Bachelors degree from The George Washington University in information systems; minor in economics. 
	During undergrad, I took a few classes that focused on systems development, python, and database management. 
	Fast-forward a little, my passions and interests in computer science grew after spending a lot of time learning data analysis frameworks for automation. 
	Professionally, I have built a number of cpu-intense post-processing toolkits; a long way of saying - Python multiprocessing, pooling, and mapping.
	This led me into exploring scalable CI-CD pipelines, deployment archiecture, and other DevOps-related technologies.""",
	'interests': """Deployment technologies, CI-CD pipelines, iOS application development using SwiftUI, writing optimized code (always in progress...)"""
	}

works = [
	{
	'title': 'Birdify iOS App',
	'desc': "A scorecard app designed using SwiftUI and xCode with the eventual goal of providing meaningful analytics to golfers. The goal behind this application was to simplify and gamify the scorecard experience.",
	'count': '001/006'
	},
	{
	'title': 'test',
	'desc': "A scorecard app designed using SwiftUI and xCode with the eventual goal of providing meaningful analytics to golfers. The goal behind this application was to simplify and gamify the scorecard experience.",
	'count': '002/006'
	}
]

@app.route('/')
def index():
	return render_template('index.html', title='The Rudy Corp.', info=info)

# routing converter
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name, info=info, works=works)
	
if __name__ == '__main__':
	app.run(debug=True)



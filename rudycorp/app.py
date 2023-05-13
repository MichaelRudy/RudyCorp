import json
from rudycorp.utils import request
from rudycorp import app, render_template

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


# Github API request
with open('/Users/michaelrudy/Desktop/Tokens/gh.txt', 'r') as in_file:
        token = in_file.readlines()
args = {
        'host': 'https://api.github.com/',
        'endpoint': 'users/michaelrudy/repos',
        'headers': {"Accept": "application/vnd.github.inertia-preview+json"},
        'username': 'michaelrudy',
        'token': token[0],
    }

github_data = request(**args)

# For Viewing Purposes
with open('view.json', 'w') as output:
	output.write(json.dumps(github_data, indent=4))

# Github Parser
works = []
for proj in github_data:
	works.append(
		{
			'title': proj['name'],
			'url': proj['url'],
			'short_desc': proj['description'],
			'language': '' if proj['language'] is None else proj['language'],
		}
	)

# For Viewing Purposes
with open('works.json','w') as output:
	output.write(json.dumps(works, indent=4))

@app.route('/')
def index():
	return render_template('index.html', title='The Rudy Corp.', info=info)


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name, info=info, works=works)
	
if __name__ == '__main__':
	app.run(debug=True)



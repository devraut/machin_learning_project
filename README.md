# machine_learning_project
I am trying to build my first ML project.

Software Requirement:
1. [Github Account](https://github.com)
2. [VS code](https://code.visualstudio.com/download)
3. [Heroku Account](https://id.heroku.com/login)
4. [GIT CLI](https://www.git-scm.com/downloads)


Creating conda environment
'''
conda create -p venv python==3.7 -y
'''

Activating conda environment
'''
conda activate venv/
'''

Installaling required packages
'''
pip install -r requirements.txt
'''

To add files/folder in git
'''
git add .
'''
OR
'''
git add <filename>
'''

To check status of updated files in git
'''
git status
'''
 
To know the log about updation 
'''
git log
'''

To create commit/version all changes by git 
'''
git commit -m "message"
'''

To send version/changes to github
'''
git push origin main
'''

To check remote url
'''
git remote -v
'''

BUILD DOCKER IMAGE
'''
docker build -t <image_name>:<tagname> .
'''
Note:Image name for docker must be on lowercase

To list docker images
'''
docker images
'''

Run docker image
'''
docker run -p 5000:5000 -e PORT=5000 <imageid>
'''

To check running container in docker
'''
docker ps
'''

To stop docker container
'''
docker stop <container_id>
'''

TO INSTALL REQUIRED LIBRARIES
'''
python setup.py install
'''
OR
'''
pip install -e .
'''

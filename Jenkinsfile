pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building..'
      }
    }
    stage('Test') {
      steps {
        echo 'Testing..'
        sh '''cd ..
virtualenv venv --python=python3
source venv/bin/activate
cd property-manager_master-C4ADQGFICO4CDDFCNKWH3FRY2RIPHU23SYFLOZWPJSZ7HAMOSMJQ
pip install -r requirements.txt
python manage.py test
yes
'''
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying....'
        echo 'Finished deploying'
      }
    }
  }
}
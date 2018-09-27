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
source venv/bin/activate
cd property-manager_master-C4ADQGFICO4CDDFCNKWH3FRY2RIPHU23SYFLOZWPJSZ7HAMOSMJQ
python manage.py test
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
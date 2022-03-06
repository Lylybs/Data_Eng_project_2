pipeline {
  agent any
  stages {
    stage('error') {
      steps {
        git(url: 'https://github.com/Lylybs/Data_Eng_project_2.git', branch: 'test_app')
      }
    }

    stage('Run app') {
      steps {
        sh '''bat "python website/toxic_app.py"
  '''
      }
    }

  }
}
pipeline {
  agent any
  stages {
    stage('Git') {
      steps {
        git(url: 'https://github.com/Lylybs/Data_Eng_project_2.git', branch: 'main')
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
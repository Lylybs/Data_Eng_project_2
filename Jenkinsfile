pipeline {
  agent any
  stages {

        stage('Merge branch'){
            steps{
                git([url:"https://github.com/Lylybs/Data_Eng_project_2.git", branch: 'main'])
            }
        }
        stage('run app') {
            steps{
                    bat "python website/toxic_app.py"
                }
        }
        stage('test branch'){
            steps{
                git([url:"https://github.com/Lylybs/Data_Eng_project_2.git", branch: 'test_app'])
            }
        }

        stage('unit test') {
            steps{
                    bat "pytest"
                }
        }
  }
}
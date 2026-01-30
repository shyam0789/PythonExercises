First is to initialize git
-> git init
Second rename the Master to main
->git branch -m master main
Before pushing the code to main first time, we need to set the path to the URL
->git remote add origin https://github.com/shyam0789/PythonExercises.git
Now create a Dev branch in github and pull
->git pull
->git checkout Dev
->git branch -a (should now point to Dev)
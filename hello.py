print("Hello from Binder!") 
echo "# my_firs_binder" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/rspezia/my_firs_binder.git
git push -u origin main

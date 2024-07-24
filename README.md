# icap-to-mne
```echo "# icap-to-mne" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:drpyae/icap-to-mne.git
git push -u origin main
```
## Create a Virtual Environment:
```python -m venv myenv```
replace *myenv* with desire environmet name.
## Activate the Virtual Environment:
### Windows:
```.\myenv\Scripts\activate```
### macOS/Linux:
```source myenv/bin/activate ```

## Select the Python Interpreter:
Once the virtual environment is activated, open the Command Palette by pressing `Ctrl+Shift+P`and type "Python: Select Interpreter." Choose the interpreter located in your virtual environment (it will look something like `.myenv\Scripts\python.exe` or `.myenv/bin/python`).


## install requirements 
``` pip install -r requirements.txt ```

## Create a .vscode Directory (Optional):
To ensure VSCode always uses the virtual environment, you can create a `.vscode` directory in your project root and add a `settings.json` file with the following content:
``` {
    "python.pythonPath": "myenv/bin/python"
}
```
Adjust the path according to your operating system and virtual environment directory.
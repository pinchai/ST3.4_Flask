## Creating Python Virtual Environment (venv)
### **macOS**

1. **Ensure Python is Installed**:
   - macOS comes with Python pre-installed, but it's recommended to install the latest version via [Homebrew](https://brew.sh/) or [Python.org](https://www.python.org/).

2. **Create the Virtual Environment**:
   ```bash
   python3 -m venv myenv
   ```

3. **Activate the Virtual Environment**:
   ```bash
   source myenv/bin/activate
   ```

4. **Deactivate the Virtual Environment**:
   ```bash
   deactivate
   ```

---

### **Windows**

1. **Ensure Python is Installed**:
   - Download and install Python from [Python.org](https://www.python.org/).
   - During installation, ensure the option **"Add Python to PATH"** is selected.

2. **Create the Virtual Environment**:
   Open Command Prompt or PowerShell and run:
   ```cmd
   python -m venv myenv
   ```

3. **Activate the Virtual Environment**:
   - Command Prompt:
     ```cmd
     myenv\Scripts\activate
     ```
   - PowerShell:
     ```powershell
     .\myenv\Scripts\Activate.ps1
     ```

4. **Deactivate the Virtual Environment**:
   ```cmd
   deactivate
   ```

---

### **Linux**

1. **Ensure Python is Installed**:
   - Most Linux distributions have Python pre-installed.
   - For the latest version, use your package manager (e.g., `apt`, `yum`) or download from [Python.org](https://www.python.org/).

2. **Create the Virtual Environment**:
   ```bash
   python3 -m venv myenv
   ```

3. **Activate the Virtual Environment**:
   ```bash
   source myenv/bin/activate
   ```

4. **Deactivate the Virtual Environment**:
   ```bash
   deactivate
   ```

---

**_Install Dependencies_**
````
pip install -r requirements.txt
````

### Start Production server
```
flask run --host=0.0.0.0 --port=5050
```

## Start development server
```
flask run --debug --host=0.0.0.0 --port=5050
```

**_pip freeze_**
```
pip3 freeze > requirements.txt  # Python3
pip freeze > requirements.txt  # Python2
```

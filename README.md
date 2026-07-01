### <img src="logo_transparent.png" width="35" align="center" alt="MarkRow Icon" />  MarkRow

MarkRow is a CLI tool designed to parse Markdown test cases into structured Excel files. This utility streamlines the process for QA engineers to convert human-readable test case specifications into standardized spreadsheet formats.

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.9+** (Check with `python3 --version` or `python --version`)
- **Git** (Check with `git --version`)
- **pip** (Python package installer)

## 🚀 Getting Started

### 1. Clone the Repository

Clone the project from the very beginning using the following command:

```bash
git clone https://github.com/hanifrazin/MarkRow.git
cd MarkRow
```

### 2. Install the CLI Command

MarkRow comes with automated installation scripts that make the `markrow` command available globally on your system. These scripts also automatically handle virtual environment setup and dependency installation on the first run.

**🍎 macOS & 🐧 Linux:**

Run the installation shell script from the project root. This will create a global command in `/usr/local/bin`:

```bash
chmod +x src/executable_scripts/install.sh
./src/executable_scripts/install.sh
```

**🪟 Windows:**

Run the installation batch script via Command Prompt/PowerShell. This will automatically add the MarkRow scripts folder to your Windows `PATH`.

```cmd
.\src\executable_scripts\install.bat
```

*(Note: On the first run of the `markrow` command, it will automatically set up the Python virtual environment and install all required dependencies like `pydantic` and `openpyxl`.)*

## 📖 How to Use

The MarkRow CLI provides a straightforward way to process Markdown files. You can run the CLI natively using the `markrow` command, or via the Python entry script `src/main.py`.

**Using the `markrow` executable (Recommended):**

```bash
markrow -i <input_path> [-o <output_path>] [-c <config_path>]
```

**Using Python:**

```bash
python src/main.py -i <input_path> [-o <output_path>] [-c <config_path>]
```

### Arguments:

- `-i`, `--input` **(Required)**: Path to a specific Markdown file (`.md`) or a directory containing Markdown files.
- `-o`, `--output` *(Optional)*: Path to the output Excel file (`.xlsx`) or directory. If omitted, files will be saved to the default output directory configured in `config.json`.
- `-c`, `--config` *(Optional)*: Path to the configuration file (defaults to `config.json`).

### Examples:

**1. Process a single Markdown file:**

```bash
markrow -i samples/input/login.md -o samples/output/login_test_cases.xlsx
```

**2. Process all Markdown files in a directory:**

```bash
markrow -i samples/input/ -o samples/output/
```

**3. Run using fallback default paths (as defined in config.json):**

```bash
markrow -i login.md
```

## 🛠 Troubleshooting

Here are some common issues you might encounter and how to fix them:

### 1. "Command not found: python3" or "python3 is not recognized"

- **Solution:** Ensure Python is added to your system's PATH during installation. On Windows, you might need to use `python` instead of `python3`.

### 2. Virtual environment activation fails (`source venv/bin/activate`)

- **Solution (macOS/Linux):** Ensure you created the venv with the exact name `venv`. Check your current directory is the project root.
- **Solution (Windows):** If you receive a script execution policy error in PowerShell, run `Set-ExecutionPolicy Unrestricted -Scope CurrentUser` as an Administrator, or use Command Prompt to run `venv\Scripts\activate.bat`.

### 3. `ModuleNotFoundError: No module named 'pydantic'` (or openpyxl)

- **Solution:** This means the dependencies are not installed or your virtual environment is not active. Make sure you activate the virtual environment (`source venv/bin/activate`) and run `pip install -r requirements.txt` again.

### 4. `Error: Input path '...' does not exist` when running the CLI

- **Solution:** Verify the path to your Markdown file is correct relative to your current terminal working directory. You can also provide an absolute path to the file.

### 5. `markrow` command not found or does not execute

If you try to run `markrow` and get an error, ensure you have run the installation script first (`install.sh` for Mac/Linux, `install.bat` for Windows). If issues persist, follow these manual fixes:

**🍎 macOS & 🐧 Linux:**

* **Issue A: Permission Denied**
  The scripts need execution permissions.
  **Fix:** Run the following command from the project root:

  ```bash
  chmod +x src/executable_scripts/markrow
  chmod +x src/executable_scripts/install.sh
  ```
* **Issue B: Command not found (`markrow: command not found`)**
  The `install.sh` might have failed to write to `/usr/local/bin` due to permission issues or restricted environments.
  **Fix 1 (Manual Symlink):**

  ```bash
  sudo ln -s "$(pwd)/src/executable_scripts/markrow" /usr/local/bin/markrow
  ```

  **Fix 2 (Add to PATH):** Add the folder to your `~/.zshrc` or `~/.bashrc`.
  ```bash
  echo 'export PATH="$PATH:'"$(pwd)"'/src/executable_scripts"' >> ~/.zshrc
  source ~/.zshrc
  ```

**🪟 Windows:**

If you ran `install.bat` but `markrow` still isn't recognized in PowerShell or Command Prompt:

* **Issue: PATH environment variable didn't refresh**
  **Fix:** Restart your PowerShell or Command Prompt window. The PATH changes applied by `install.bat` take effect in new terminal sessions.
* **Issue: Script Execution Disabled (PowerShell)**
  **Fix:** Open PowerShell as Administrator and run:

  ```powershell
  Set-ExecutionPolicy Unrestricted -Scope CurrentUser
  ```
* **Alternative for Git Bash Users:**
  If you prefer Git Bash instead of PowerShell, Git Bash reads the bash `markrow` file instead of `markrow.bat`. You can alias it by running:

  ```bash
  echo "alias markrow='bash $(pwd)/src/executable_scripts/markrow'" >> ~/.bash_profile
  source ~/.bash_profile
  ```

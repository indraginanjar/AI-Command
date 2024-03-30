# AI Command

## Description

Executor scripts that runs a python script to generate powershell/pwsh (or any other supported executor/shell) command and execute it.

### Supported language

AI operation is done through OpenAI, so all supported language  by OpenAI can be used in with **aicommand** and **aiprompt**.

### Supported command language/executor

Supported executor:

1. powerShell, default executor on Windows system used by **aicommand.ps1**

2. pwsh, default executor on  non-Windows systems (like Linux or MacOS) used by **aicommand.ps1**

3. bash (Bourne Again SHell), default executor used by **aicommand.sh**

4. zsh (Z shell)

5. cmd (DOS/Windows Command Prompt)

6. python

7. sh, default executor for any case of invalid executor argument inputed

## Installation

### Manual install

Steps:

1. clone the **aicommand** from <https://github.com/indraginanjar/AI-Command.git>

2. Enter the **aicommand** project directory in commandline (assumed powershell or pwsh)

3. [Optional] Create virtual environment using `python -m venv .venv`

4. [Optional] Activate the created virtual environment, `.\.venv\Script\Activate.ps1`

5. Install the required modules, `pip install -r requirements.txt`

6. Include the **aicommand** project directory into system/user path on environment variable, so you could access it from any directory.

### Scripted install

Step:

1. clone the **aicommand** from <https://github.com/indraginanjar/AI-Command.git>

2. Enter the **aicommand** project directory in commandline (assumed powershell or pwsh)

3. Run install script

    ```powershell
    install.ps1
    ```

### Environment Variable

#### Necessary environment variable

```ini
AI_COMMAND_OPENAI_API_KEY=<Your OpenAI API Key>
```

#### Optional environment variable

Default executor for **aicommand.ps1** is **powershell** on Windows operating system. For any other operating system, aicommand will use **pwsh** as default executor.

To define any other executor, set it on evironment variable:

```ini
AI_COMMAND_EXECUTOR=<executor to use>
```

Currently, this environment variable only affecting **aicommand.ps1** and **aicommand.py**

## Usage

To use **aicommand.ps1**, open powershell or pwsh terminal

Syntax:

```powershell
aicommand.ps1 "your prompt describing task/command to produce and execute."
```

Example:

```powershell
PS C:\Program Files> aicommand.ps1 "get current directory name"
Prompt:
 get current directory name
Generated command:
 $CurrentDirectory = Get-Location
$DirectoryName = Split-Path -Path $CurrentDirectory -Leaf
$DirectoryName
Do you want to execute the generated command? (y)es/(n)o: y
Executing generated command ...
Program Files

PS C:\Program Files>
```

### Usage by directly running aicommand python

Currently running **aicommand.py** directly is the only way for using all types of supported executors without setting the executor on AI_COMMAND_EXECUTOR environment variable.

```powershell
.\.venv\Script\Activate.ps1
python aicommand.py --executor your_executor "your prompt describing task/command to produce and execute."
deactivate
```

#### Notes on using non existing executor

Most of the time choosing non existing executor will just show error message in console.

For example  if you bash as the executor on Windows:

```powershell
PS C:\> aicommand.ps1 --executor bash "get current local datetime"
Prompt:
get current local datetime
Generated command:
date +%Y%m%d%H%M%S;
Do you want to execute the generated command? (y)es/(n)o: y
Executing generated command ...
/bin/bash: date +%Y%m%d%H%M%S;: command not found
```

Actually if you only want to get the command without executing it, you could safely choose **no** on question `Do you want to execute the generated command? (y)es/(n)o`.

```powershell
PS C:\> aicommand.ps1 --executor bash "get current local datetime"
Prompt:
get current local datetime
Generated command:
date +"%Y-%m-%d %H:%M:%S";
Do you want to execute the generated command? (y)es/(n)o: n
You choose not to execute the generated command.
```

### Changing directory

Current executor location is not affected by  the `cd` or `Set-Location` command. To change the current directory could only effective if you start a new session after changing directory, so the directory change is only happen in new session.

Example:

```powershell
aicommand.ps1 "change directory to program files then open a new shell"
Prompt:
change directory to program files then open a new shell
Generated command:
cd "C:\Program Files"
Start-Process powershell
Do you want to execute the generated command? (y)es/(n)o: y
Executing generated command ...
```

### Running from within Git Bash on Git for Windows

For running inside git bash, type powershell before the aicommand.ps1

Syntax:

```powershell
powershell aicommand.ps1 "your prompt describing task/command to produce and execute."
```

### Running from Bash

Syntax:

```bash
powershell aicommand.sh "your prompt describing task/command to produce and execute."
```

Currently **aicommand.sh** could only targetting bash as the executor.

## AI Prompt

A powershell script that runs a python script for receiving AI response based on inputed prompt text.

### AI Prompt usage

### AI Prompt usage on powershell

AI Prompt usage syntax:

```powershell
aiprompt.ps1 "your prompt to be answered by AI"
```

AI Prompt usage example:

````powershell
aiprompt.ps1 "how to remove an environment variable on powershell"
Prompt:
how to remove an environment variable on powershell
Response:
To remove an environment variable on PowerShell, you can use the following command:

```powershell
Remove-Item env:VariableName
```

Replace "VariableName" with the name of the environment variable you want to remove. For example, to remove an environment variable named "MyVar", you would use:

```powershell
Remove-Item env:MyVar
```
````

### AI Prompt usage on bash

AI Prompt usage on bash example:

````bash
aiprompt.sh "how to remove an environment variable on bash"
Prompt:
how to remove an environment variable on bash
Response:
To remove an environment variable in the bash shell, you can use the `unset` command followed by the variable name.

For example, if you want to remove an environment variable called `MY_VARIABLE`, you can do so by typing the following command:

```bash
unset MY_VARIABLE
```

After running this command, the `MY_VARIABLE` environment variable will be removed and no longer accessible in the current executor session.
````

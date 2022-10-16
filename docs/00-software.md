# Software {#software}
For this book and seminar, we will need to install

* PsychoPy that comes bundled with Python.
* IDE of your choice. My instructions will be for Visual Studio Code, which has a very good Python support.
* Jupyter Notebook for trying out small snippets of code.

I will not give detailed instructions on how to install the necessary software but rather point you to official manuals. This makes this text more future-proof as specific details might easily change^[If you are part of the seminar, ask me whenever you have problems or are unsure about how to proceeed].

## PsychoPy {#install-psychopy}
Download and install [Standalone PsychoPy](https://www.psychopy.org/download.html) version. Use whatever the latest (and greatest) PsychoPy version is suggested to you (PsychoPy 2022.2.4 using Python 3.8 as of time of writing) and follow instructions.

Note that you can also install PsychoPy as a anaconda package or install an official Python distribution and add PsychoPy via pip. However, I find the standalone easier to use as it has all necessary additional libraries. Plus, it has additional tools for GUI-based experiment programming and integration with [Pavlovia.org](https://pavlovia.org/).

## VS Code {#install-vs-code}
[Visual Studio Code](https://code.visualstudio.com/) is a free lightweight open-source editor with strong support for Python. Download the installer for your platform and follow the instructions.

Next, follow [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial) tutorial. **Skip** the _Install a Python interpreter_ section, as you already have Python installation bundled with PsychoPy. This is the interpreter that you should use in the _Select a Python interpreter_ section. In my case the path is `C:\Program Files\PsychoPy3\python.exe`.

Install and enable a linter, software that highlights syntactical and stylistic problems in your Python source code. Follow the [manual](https://code.visualstudio.com/docs/python/linting) at VS Code website.


## Jupyter Notebooks {#jupyter-notebooks}
[Jupyter Notebooks](https://jupyter.org/) offer a very convenient way to mix text, figure and code in a single document. They also make it easy to play with various small snippets in parallel without running scripts. We will rely on them for our first chapter and for an occasional exercises or code testing later on. There are two way you can use them: 1) in VS Code using Jupyter extension, 2) in your browser using classical interface.

### Jupyter Notebooks in VS Code
Follow [the manual](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) on how to install Jupyter package and use notebooks in VS Code.

### Jupyter Notebooks in Anaconda
The simplest way to use Jupyter Notebooks along with a lot of other useful data science tools is via [Anaconda](https://www.anaconda.com/products/individual) toolkit. However, note that this will introduce a _second_ Python distribution to your system. This, in turn, could lead to some confusion when working with scripts in VS Code if you accidentally have Anaconda interpreter active instead of the PsychoPy one. Do not panic, follow [Select a Python interpreter](https://code.visualstudio.com/docs/python/python-tutorial#_select-a-python-interpreter) instructions and make sure that you have PsychoPy interpreter as the active one.

Otherwise, download and install Anaconda. The website has an excellent [Getting started](https://docs.anaconda.com/anaconda/user-guide/getting-started/) section.

## Keeping things tidy {#files-folder}
Before we start, I suggest that you create a folder called _games-with-python_ (or something along these lines). If you opted to use Jupyter Notebooks via Anaconda, you should create it in your user folder because this is where Anaconda would expects to find them. Then, create a new subfolder for each chapter / game. For the seminar, you would need to zip and upload a folder with all the files.

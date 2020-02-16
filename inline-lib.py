import argparse
import re


def remove_file_extension(file: str):
    # Check if file type has been given, if so remove.
    file = re.sub("\.[a-z]+$", '', file)
    return file


class TemplateGenerator:
    """
    Methods to generate inline script templates
    """

    def __init__(self, file_type, input_file_name):
        self.script_type = file_type
        self.input_file = input_file_name
        self.output_file = f"{remove_file_extension(input_file_name)}.yml"

    def get_script_model(self, script_type: str):
        # Self made switch statement, runs the function given by the 'switcher'
        switcher = {
            "python": self.get_python_header
        }
        # Get the function from switcher dictionary
        func = switcher.get(self.script_type, lambda: "Type not implemented")
        # Execute the function
        return func()

    def get_python_header(self, arguments='', fail_on_stderr='false'):
        return f"""template:
- task: PythonScript@0
  inputs:
    scriptSource: 'inline'
    arguments: ''
    #pythonInterpreter: '3.5'
    workingDirectory: '$(Build.SourcesDirectory)'
    failOnStderr: 'false'
    script: |
"""

    def write_header(self):
        fo = open(self.output_file, "a")
        fo.write(self.get_script_model(self.script_type))
        fo.close()

    def write_script_content(self):
        fo = open(self.output_file, "a")
        with open(self.input_file) as fp:
            line = fp.readline()
            while line:
                line = f"        {line}"
                fo.write(line)
                line = fp.readline()
        fp.close()
        fo.close()


def write_python_template(script_name: str):
    generator = TemplateGenerator("python", script_name)
    generator.write_header()
    generator.write_script_content()


if __name__ == "__main__":
    write_python_template("testscript.py")

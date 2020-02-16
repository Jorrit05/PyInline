import argparse


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file", help="File to transform to YAML inline", required=True)
    parser.add_argument("-a", "--arguments", help="Arguments to inline script, defaults to none")
    parser.add_argument("-f", "--fail_on_stderr", help="Fail on standard error")
    return parser.parse_args()


def get_header(arguments='', fail_on_stderr='false'):
    return f"""template:
- task: PythonScript@0
  inputs:
    scriptSource: 'inline'
    arguments: f"{arguments}"
    #pythonInterpreter: '3.5'
    workingDirectory: '$(Build.SourcesDirectory)'
    failOnStderr: f"{fail_on_stderr}"
    script: |
"""


if __name__ == "__main__":
    args = init_args()

    input_file = f"{args.input_file}.py"
    output_file = f"{args.input_file}.yml"
    fo = open(output_file, "a")
    fo.write(get_header())

    with open(input_file) as fp:
        line = fp.readline()
        while line:
            line = f"        {line}"
            fo.write(line)
            line = fp.readline()

    fp.close()
    fo.close()
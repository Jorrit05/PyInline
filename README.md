# PyInline
## Introduction

Convert your Python script to a Azure DevOps YAML Template. 

I ran in to the use case where as a central team we were building a template repository to be used by other teams. For some of the functionality we where using 'inline' scripts. This has the huge downside that Inline scripts can't be unittested easily. 

This script is intended to take a normal Python script and convert it to a Python inline script template for Azure DevOps.  This is the first MVP, so not much functionally added. 

Eventually I'd like to make a pipeline which:

1. Unit testst script(s)
2. Converts the script to YAML
3. Uploads the script to our template repository

## Usage

Call script with source python script as parameter. Type -h for argument helper. 
import subprocess

insert_text = '''
<link rel="shortcut icon" type="image/png" href="https://s3.amazonaws.com/jedwebster.com/static/47.png"/>
<script type="text/javascript" id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>
'''

def update():
    bashCommand = "jemdoc index"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

def write(file):
    with open(file, 'r+') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith('<head>'):
                lines[i] = lines[i] + insert_text
            elif line.__contains__('latex'):
                lines[i] = line.replace('latex', '\(\LaTeX\)')
        f.truncate()
        f.seek(0)
        for line in lines:
            f.write(line)

# next: auto upload site to object storage

if __name__ == '__main__':
    update()
    write('index.html')

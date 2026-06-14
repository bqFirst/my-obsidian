import os
files = os.listdir('pdf')
i = 0
for file in files:
    file = os.path.join('/work/github/my-obsidian','pdf', file)
    print(f' {file}')
    #file_new = 'file_{i}'
    #cli = f'mv  {file} {file_new}'
    #i+=0
    #os.system(cli)
    cli = 'chandra'+f' {file}'+ ' ./output' + ' --include-headers-footers' + ' --method hf'
    os.system(cli)

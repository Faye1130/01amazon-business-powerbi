"""Configure the bundled data folder. Python 3, standard library only."""
from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
p=root/'Amazon.SemanticModel/model.bim'
m=json.loads(p.read_text(encoding='utf-8'))
count=0
for table in m['model']['tables']:
    for partition in table.get('partitions',[]):
        source=partition['source']
        e=source.get('expression')
        if e is None: continue
        text=e if isinstance(e,str) else '\n'.join(e)
        def replace(match):
            global count
            filename=match.group(1).replace('\\','/').split('/')[-1]
            path=root/'data'/filename
            if not path.is_file(): raise FileNotFoundError(path)
            count+=1
            return 'File.Contents("'+path.as_posix().replace('"','""')+'")'
        text=re.sub(r'File\.Contents\("([^"\r\n]+)"\)',replace,text)
        source['expression']=text if isinstance(e,str) else text.splitlines()
p.write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
print('Configured',count,'CSV queries. Open amazon-business.pbip and refresh.')

import json, sys
p = r"c:\IOT_XR_EL\models\soil_sensor.gltf"
with open(p, 'r', encoding='utf-8') as f:
    g = json.load(f)
for i, node in enumerate(g.get('nodes', [])):
    name = node.get('name', '')
    if isinstance(name, str) and name.lower() == 'sensor':
        print(i)
        sys.exit(0)
print('NOT_FOUND')
sys.exit(1)

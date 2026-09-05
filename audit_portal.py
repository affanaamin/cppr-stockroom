import re

with open('portal.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all handler calls in HTML
handlers = re.findall(r'(?:onclick|onchange|onsubmit|oninput)="([^"]+)"', html)
calls = set()
for h in handlers:
    # multiple statements might be separated by semicolon
    for part in h.split(';'):
        part = part.strip()
        m = re.match(r'([a-zA-Z0-9_]+)\s*\(', part)
        if m:
            calls.add(m.group(1))

print('Handlers called in HTML:', sorted(list(calls)))

# Find all function definitions in <script>
defs = set(re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', html))
print('\nFunctions defined in script:', sorted(list(defs)))

builtins = {'alert', 'fetch', 'setTimeout', 'clearTimeout', 'parseInt', 'parseFloat'}
missing = (calls - defs) - builtins
print('\nMISSING FUNCTIONS:', missing)

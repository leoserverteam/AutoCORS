import json

with open('domains.json', 'r') as f:
    domains = json.load(f)

content = "map $http_origin $cors_header {\n    default \"\";\n"
for domain in domains:
    # Экранируем точки для regex и добавляем формат как на скрипте
    safe_domain = domain.replace('.', '\\.')
    content += f'    "~^{safe_domain}$" "$http_origin";\n'
content += "}"

with open('cors.conf', 'w') as f:
    f.write(content)

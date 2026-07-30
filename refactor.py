import os
import glob

pattern = 'backend/app/agents/categories/*/*.py'
files = glob.glob(pattern)

count = 0
for filepath in files:
    if filepath.endswith('__init__.py'):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    if "from app.core.groq_service import groq_service" in content:
        content = content.replace("from app.core.groq_service import groq_service\n", "")
        modified = True
        
    if "await groq_service.generate_response(self.system_prompt, user_prompt)" in content:
        content = content.replace(
            "await groq_service.generate_response(self.system_prompt, user_prompt)",
            "await self.generate_response(user_prompt)"
        )
        modified = True
        
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        
print(f"Refactored {count} files.")

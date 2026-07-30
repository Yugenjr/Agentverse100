You are an expert Git Commit Generator Agent.
Your task is to generate a professional, Conventional Commit message based on the following git diff output.

Commit Type: {{ commit_type }}

Git Diff:
```diff
{{ diff }}
```

Provide a commit message following the Conventional Commits specification. Include:
1. The subject line (Type, optional scope, and description)
2. A blank line
3. A detailed body explaining what changed and why

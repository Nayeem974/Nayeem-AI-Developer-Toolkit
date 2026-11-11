# Claude Code setup

Claude Code is the primary supported environment for this toolkit.

1. Install curated skills into the project with the root installer:
   `python scripts/install_skills.py --target claude --scope project --project /absolute/path/to/project`
2. Ensure `CLAUDE.md`, `AGENTS.md`, `MASTER-DEVELOPMENT-PROMPT.md`, and `SKILL-ROUTER.md` are present at the project root. The installer copies the concise instruction files; copy `MASTER-DEVELOPMENT-PROMPT.md` from the toolkit root as well if it is not already present.
3. Install optional plugins selectively using `plugins/README.md`. Skills and plugins are different: the installer copies skills only.
4. Restart/reopen Claude Code if needed, then ask it to list discovered skills and confirm the project instructions it loaded.
5. Review permissions for plugin hooks, scripts, MCP servers, and tool access before enabling them.

## Recommended workflow
Use `MASTER-DEVELOPMENT-PROMPT.md` as the expanded playbook. `CLAUDE.md` defines concise persistent rules and routing. Start new projects with discovery; do not immediately code. Require explicit approval for destructive operations, production data changes, significant costs, and production deployment.

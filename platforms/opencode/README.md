# OpenCode

Use `.agents/skills/` for portable Agent Skills where supported by your OpenCode version, and place `AGENTS.md` plus `SKILL-ROUTER.md` at the repository root. OpenCode plugin configuration differs between V1 and V2; do not copy Claude plugin settings into OpenCode.

Run: `python scripts/install_skills.py --target opencode --scope project --project /path/to/repo`. For Superpowers, consult the included upstream `.opencode/INSTALL.md` in `plugins/superpowers/`.
